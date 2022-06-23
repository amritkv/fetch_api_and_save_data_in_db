import os
from flask import Flask, request
from dotenv import load_dotenv

app = Flask("FetchData")
load_dotenv()
api_id = os.getenv('API_ID')

@app.route('/fetchData', methods=['GET'])
def fetchData():
    
    headers = {"Content-type": "application/json", "api-id" : api_id}
    
    
    return "Hello World....!"