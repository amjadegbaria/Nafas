from pymongo import MongoClient
from config import MONGO_URI
from pymongo.server_api import ServerApi
import certifi
# ca = certifi.where()

client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db = client["Nafas"]
