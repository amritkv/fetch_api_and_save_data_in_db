import os
import json
import flask
import logging
import requests
from dotenv import load_dotenv, find_dotenv

class FetchAndSaveDataLayer:
    
    def __init__(self, dbConnection):

        self.dbConnection=dbConnection
        load_dotenv(find_dotenv('./../../config/.env'))
        self.APP_ID = os.getenv('APP_ID')
        self.USERS_DATA_URL = os.getenv('USERS_DATA_URL')
        self.USERS_POSTS_DATA = os.getenv('USERS_POSTS_DATA')
        self.DB_NAME = os.getenv('DB_NAME')
        self.USERS_COLLECTION_NAME = os.getenv('USERS_COLLECTION_NAME')
        self.USERS_POST_DATA_COLLECTION_NAME = os.getenv('USERS_POST_DATA_COLLECTION_NAME')
        logging.basicConfig( filename='log_file.log',
                        filemode='a',
                        level=logging.INFO,
                        format= '%(asctime)s - %(levelname)s - %(message)s',
                        )

    
    def fetchUsersData(self):

        db=self.dbConnection.getDbConnection()
        db_name = self.DB_NAME
        collection_name = self.USERS_COLLECTION_NAME
        try:
            request_header = {"Content-Type": "application/json", "app-id" : self.APP_ID}
            response = requests.get(url=self.USERS_DATA_URL, headers=request_header)
            
            try:
                for data in response.json()['data']:
                    db[self.DB_NAME][self.USERS_COLLECTION_NAME].insert_one(data)
                return response.status_code
            
            except Exception as excep:
                print("Could not save users data into database :", error)
                print(error.__class__, "occurred.")
                logging.exception(str(error))   
        
        except Exception as error:
            print("Error occurred :", error)
            print(error.__class__, "occurred.")
            logging.exception(str(error))

    def fetchUsersPostData(self):
        
        db=self.dbConnection.getDbConnection()
        db_name = self.DB_NAME
        collection_name = self.USERS_COLLECTION_NAME
        try:
            users_data = db[self.DB_NAME][self.USERS_COLLECTION_NAME].find()
            print(users_data)
            # for each_user_data in 
        except Exception as excep:
            print("Error occurred :", excep)
            print(excep.__class__, "occurred.")
            logging.exception(str(excep))