#!/usr/bin/env python3
"""
Real-time performance monitoring for Nafas Telegram Bot
"""

import time
import psutil
import asyncio
import threading
from datetime import datetime
from collections import defaultdict

class PerformanceMonitor:
    def __init__(self):
        self.response_times = defaultdict(list)
        self.active_requests = 0
        self.max_concurrent_requests = 0
        self.start_time = time.time()
        self.request_count = 0
        
    def record_request(self, user_id, operation, response_time):
        """Record a request and its response time"""
        self.request_count += 1
        self.response_times[operation].append(response_time)
        
        # Log slow operations
        if response_time > 1.0:
            print(f"⚠️  Slow operation detected: {operation} took {response_time:.2f}s for user {user_id}")
    
    def get_stats(self):
        """Get current performance statistics"""
        current_time = time.time()
        uptime = current_time - self.start_time
        
        stats = {
            'uptime': uptime,
            'total_requests': self.request_count,
            'requests_per_second': self.request_count / uptime if uptime > 0 else 0,
            'max_concurrent': self.max_concurrent_requests,
            'current_active': self.active_requests
        }
        
        # Calculate response time statistics
        for operation, times in self.response_times.items():
            if times:
                stats[f'{operation}_avg'] = sum(times) / len(times)
                stats[f'{operation}_max'] = max(times)
                stats[f'{operation}_min'] = min(times)
        
        return stats
    
    def print_stats(self):
        """Print current performance statistics"""
        stats = self.get_stats()
        
        print("\n" + "="*60)
        print("📊 REAL-TIME PERFORMANCE MONITOR")
        print("="*60)
        print(f"⏱️  Uptime: {stats['uptime']:.1f} seconds")
        print(f"📈 Total Requests: {stats['total_requests']}")
        print(f"🚀 Requests/Second: {stats['requests_per_second']:.2f}")
        print(f"👥 Max Concurrent Users: {stats['max_concurrent']}")
        print(f"🔄 Currently Active: {stats['current_active']}")
        
        # Show response times for different operations
        print("\n⏱️  Response Times:")
        for operation, times in self.response_times.items():
            if times:
                avg_time = sum(times) / len(times)
                max_time = max(times)
                min_time = min(times)
                print(f"   {operation}: avg={avg_time:.3f}s, max={max_time:.3f}s, min={min_time:.3f}s")
        
        # System resources
        cpu_percent = psutil.cpu_percent()
        memory = psutil.virtual_memory()
        print(f"\n💻 System Resources:")
        print(f"   CPU Usage: {cpu_percent}%")
        print(f"   Memory Usage: {memory.percent}% ({memory.used // 1024 // 1024}MB / {memory.total // 1024 // 1024}MB)")
        
        print("="*60)

def monitor_system_resources():
    """Monitor system resource usage"""
    print("🔍 Starting system resource monitoring...")
    
    while True:
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            # Alert if resources are high
            if cpu_percent > 80:
                print(f"⚠️  High CPU usage: {cpu_percent}%")
            if memory.percent > 80:
                print(f"⚠️  High memory usage: {memory.percent}%")
                
            time.sleep(5)  # Check every 5 seconds
            
        except KeyboardInterrupt:
            print("\n🛑 System monitoring stopped")
            break

def simulate_load_test():
    """Simulate load testing"""
    print("🧪 Starting load test simulation...")
    
    monitor = PerformanceMonitor()
    
    async def simulate_user_load(user_id):
        """Simulate a user generating load"""
        operations = [
            "database_read",
            "database_write", 
            "file_read",
            "message_process",
            "callback_process"
        ]
        
        for i in range(10):  # 10 operations per user
            operation = operations[i % len(operations)]
            start_time = time.time()
            
            # Simulate operation time
            await asyncio.sleep(0.1 + (i * 0.05))
            
            response_time = time.time() - start_time
            monitor.record_request(user_id, operation, response_time)
            
            # Print stats every 5 operations
            if i % 5 == 0:
                monitor.print_stats()
    
    # Simulate multiple users
    async def run_load_test():
        tasks = []
        for i in range(3):  # 3 concurrent users
            task = asyncio.create_task(simulate_user_load(f"user_{i+1}"))
            tasks.append(task)
        
        await asyncio.gather(*tasks)
    
    asyncio.run(run_load_test())

if __name__ == "__main__":
    print("🚀 Nafas Bot Performance Monitor")
    print("="*50)
    
    # Start system monitoring in a separate thread
    system_thread = threading.Thread(target=monitor_system_resources, daemon=True)
    system_thread.start()
    
    # Run load test
    simulate_load_test()
    
    print("\n✅ Performance monitoring completed!")
    print("💡 To monitor real bot performance:")
    print("1. Start this script: python monitor_performance.py")
    print("2. Start your bot: python bot.py")
    print("3. Have multiple users interact with the bot")
    print("4. Watch the performance metrics in real-time")
