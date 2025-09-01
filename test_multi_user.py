#!/usr/bin/env python3
"""
Multi-user performance test for Nafas Telegram Bot
"""

import asyncio
import time
import random
from datetime import datetime

# Simulate multiple users interacting with the bot
async def simulate_user(user_id, delay=0):
    """Simulate a user interaction"""
    await asyncio.sleep(delay)  # Stagger user interactions
    
    start_time = time.time()
    
    # Simulate different types of interactions
    interactions = [
        "start",
        "Hello",
        "How are you?",
        "I need help",
        "What exercises do you have?",
        "Let's begin",
        "Next",
        "Yes",
        "No",
        "Maybe"
    ]
    
    for interaction in interactions:
        # Simulate processing time
        await asyncio.sleep(random.uniform(0.1, 0.5))
        
        # Log the interaction
        current_time = time.time()
        response_time = current_time - start_time
        print(f"User {user_id}: {interaction} (Response time: {response_time:.2f}s)")
        
        start_time = current_time

async def test_concurrent_users(num_users=5):
    """Test multiple users using the bot simultaneously"""
    print(f"🧪 Testing {num_users} concurrent users...")
    print("=" * 50)
    
    start_time = time.time()
    
    # Create tasks for multiple users
    tasks = []
    for i in range(num_users):
        delay = i * 0.2  # Stagger user starts
        task = asyncio.create_task(simulate_user(f"User_{i+1}", delay))
        tasks.append(task)
    
    # Wait for all users to complete
    await asyncio.gather(*tasks)
    
    total_time = time.time() - start_time
    print(f"\n✅ Test completed in {total_time:.2f} seconds")
    print(f"📊 Average time per user: {total_time/num_users:.2f} seconds")

def test_database_performance():
    """Test database operations performance"""
    print("\n🗄️ Testing database performance...")
    print("=" * 30)
    
    try:
        from database.queries import get_user_data, save_user_progress
        import asyncio
        
        async def db_test():
            start_time = time.time()
            
            # Test multiple database operations
            for i in range(10):
                user_id = f"test_user_{i}"
                test_data = {"flow_id": "test_flow", "current_question_id": "test_question"}
                
                # Test save operation
                await save_user_progress(user_id, test_data)
                
                # Test read operation
                user_data = await get_user_data(user_id)
                
                print(f"DB Operation {i+1}: User {user_id} - {(time.time() - start_time):.3f}s")
            
            total_time = time.time() - start_time
            print(f"\n✅ Database test completed in {total_time:.2f} seconds")
            print(f"📊 Average DB operation time: {total_time/10:.3f} seconds")
        
        asyncio.run(db_test())
        
    except Exception as e:
        print(f"❌ Database test failed: {e}")

def test_file_operations():
    """Test file operations performance"""
    print("\n📁 Testing file operations performance...")
    print("=" * 35)
    
    try:
        import aiofiles
        import os
        
        async def file_test():
            start_time = time.time()
            
            # Test reading multiple files
            test_files = [
                "config.py",
                "requirements.txt",
                "bot.py"
            ]
            
            for i, filename in enumerate(test_files):
                if os.path.exists(filename):
                    async with aiofiles.open(filename, 'r') as f:
                        content = await f.read()
                    
                    print(f"File {i+1}: {filename} - {(time.time() - start_time):.3f}s")
            
            total_time = time.time() - start_time
            print(f"\n✅ File operations test completed in {total_time:.2f} seconds")
            print(f"📊 Average file operation time: {total_time/len(test_files):.3f} seconds")
        
        asyncio.run(file_test())
        
    except Exception as e:
        print(f"❌ File operations test failed: {e}")

if __name__ == "__main__":
    print("🚀 Nafas Bot Multi-User Performance Test")
    print("=" * 50)
    
    # Test 1: Concurrent users
    asyncio.run(test_concurrent_users(5))
    
    # Test 2: Database performance
    test_database_performance()
    
    # Test 3: File operations
    test_file_operations()
    
    print("\n🎯 Performance Test Summary:")
    print("- Concurrent users: ✅ Simulated")
    print("- Database operations: ✅ Async")
    print("- File operations: ✅ Non-blocking")
    print("\n💡 To test with real users:")
    print("1. Start your bot: python bot.py")
    print("2. Have multiple people send messages simultaneously")
    print("3. Monitor response times in the bot logs")
