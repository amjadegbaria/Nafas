import time
import asyncio
import logging
from functools import wraps
from collections import defaultdict
import statistics

logger = logging.getLogger(__name__)

class PerformanceMonitor:
    def __init__(self):
        self.response_times = defaultdict(list)
        self.active_requests = 0
        self.max_concurrent_requests = 0
        self._lock = asyncio.Lock()
    
    async def track_request(self, operation_name):
        start_time = time.time()
        async with self._lock:
            self.active_requests += 1
            self.max_concurrent_requests = max(self.max_concurrent_requests, self.active_requests)
        
        try:
            return start_time
        finally:
            async with self._lock:
                self.active_requests -= 1
    
    async def record_response_time(self, operation_name, start_time):
        response_time = time.time() - start_time
        self.response_times[operation_name].append(response_time)
        
        # Log slow operations
        if response_time > 1.0:  # Log operations taking more than 1 second
            logger.warning(f"Slow operation detected: {operation_name} took {response_time:.2f}s")
    
    def get_stats(self):
        stats = {}
        for operation, times in self.response_times.items():
            if times:
                stats[operation] = {
                    'count': len(times),
                    'avg': statistics.mean(times),
                    'median': statistics.median(times),
                    'max': max(times),
                    'min': min(times),
                    'p95': statistics.quantiles(times, n=20)[18] if len(times) >= 20 else max(times)
                }
        return stats
    
    def get_concurrency_stats(self):
        return {
            'current_active': self.active_requests,
            'max_concurrent': self.max_concurrent_requests
        }

# Global performance monitor
performance_monitor = PerformanceMonitor()

def monitor_performance(operation_name):
    """Decorator to monitor function performance"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = await performance_monitor.track_request(operation_name)
            try:
                result = await func(*args, **kwargs)
                return result
            finally:
                await performance_monitor.record_response_time(operation_name, start_time)
        return wrapper
    return decorator
