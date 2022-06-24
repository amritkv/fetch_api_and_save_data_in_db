from email import header
import os
import json
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv, find_dotenv
from app.container.Containers import ServiceLayer

app = Flask("FetchAndSaveData")

class fetchAndSave:
    def __init__(self):
        pass

    @app.route('/fetchAndSaveData', methods = ['GET'])
    def fetchData():

        fetch_data_status = ServiceLayer.fetchAndSaveService().fetchUersDataService()
        if fetch_data_status == 200:
            return json.dumps({"Message" : "Successfully saved users data into database....!"})

        else:
            return json.dumps({"Error" : fetch_data_status})

    @app.route('/fetchUsersPostData', methods = ['GET'])
    def fetchUsersPostData():

        fetch_posts_data_status = ServiceLayer.fetchAndSaveService().fetchUsersPostDataService()
        
