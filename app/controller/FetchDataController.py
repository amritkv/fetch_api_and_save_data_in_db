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

    # This end-point is used to fetch users data from given url in .env file
    @app.route('/fetchAndSaveUsersData', methods = ['GET'])
    def fetchAndSaveUsersData():

        fetch_and_save_users_data_status = ServiceLayer.fetchAndSaveService() \
                                                       .fetchAndSaveUersDataService()
        if fetch_and_save_users_data_status == 200:
            return json.dumps({"Message" : "Successfully saved users data into database....!"})

        else:
            return json.dumps({"Error" : fetch_and_save_users_data_status})

    # This end-point is used to fetch users post data based on user-id from given url in .env file
    @app.route('/fetchAndSaveUsersPostData', methods = ['GET'])
    def fetchAndSaveUsersPostData():

        fetch_and_save_users_posts_data_status = ServiceLayer.fetchAndSaveService() \
                                                             .fetchAndSaveUsersPostDataService()
        if fetch_and_save_users_posts_data_status == 1:
            return json.dumps({"message" : "Successfully saved users post data into database....!"})
        else:
            return json.dumps({"Error" : fetch_and_save_users_posts_data_status})
        
