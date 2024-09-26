from pymongo import MongoClient
from config import MONGO_URI
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://amjad123:amjad123@dev.q9log.mongodb.net/?retryWrites=true&w=majority&appName=dev", server_api=ServerApi('1'))
db = client["Nafas"]
