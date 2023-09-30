from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv('.env')
username = os.getenv('username')
password = os.getenv('password')

DATABASE_NAME = "BunnyJeans"
# COLLECTION_NAME = "Data"
MONGO_DB_URL = f"mongodb+srv://{username}:{password}@cluster0.vpnjjt4.mongodb.net/"
MONGO_DB_PORT = 8080

client = MongoClient(f"{MONGO_DB_URL}:{MONGO_DB_PORT}")

db = client[DATABASE_NAME]

# collection = db[COLLECTION_NAME]

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
  return {"message": "Hello World"}

@app.get("/data", tags=["Data"])
def get_data():
  collection = db['Data']
  data = list(collection.find({}, {'_id': False}))
  return data

@app.get("/collections", tags=["Collections"])
def get_collections():
  collection = db['Collections']
  collectionList = list(collection.find({}, {'_id': False}))
  return collectionList