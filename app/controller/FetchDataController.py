from email import header
import os
import json
import requests
from flask import Flask
from dotenv import load_dotenv, find_dotenv

app = Flask("FetchAndData")
load_dotenv(find_dotenv('./config/.env'))
app_id = os.getenv('APP_ID')
URL = "https://dummyapi.io/data/v1/user"

@app.route('/fetchAndSaveData', methods=['GET'])
def fetchData():
    request_header = {"Content-Type": "application/json", "app-id" : app_id}
    response = requests.get(url=URL, headers=request_header)    
    return response.content

@app.route('')


