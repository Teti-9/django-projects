from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.environ.get("MONGODB_URL"))
db = client.Cluster0