from pymongo import MongoClient
from config import MONGO_URI
from pymongo.server_api import ServerApi
import certifi
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

ca = certifi.where()

# Synchronous client for backward compatibility
client = MongoClient(
    MONGO_URI, 
    server_api=ServerApi('1'), 
    tlsCAFile=ca,
    maxPoolSize=50,  # Connection pool size
    minPoolSize=10,  # Minimum connections
    maxIdleTimeMS=30000,  # Close idle connections after 30 seconds
    waitQueueTimeoutMS=5000,  # Wait queue timeout
    connectTimeoutMS=5000,  # Connection timeout
    serverSelectionTimeoutMS=5000  # Server selection timeout
)

# Async client for new async operations
async_client = AsyncIOMotorClient(
    MONGO_URI,
    server_api=ServerApi('1'),
    tlsCAFile=ca,
    maxPoolSize=50,
    minPoolSize=10,
    maxIdleTimeMS=30000,
    waitQueueTimeoutMS=5000,
    connectTimeoutMS=5000,
    serverSelectionTimeoutMS=5000
)

db = client["Nafas"]
async_db = async_client["Nafas"]
