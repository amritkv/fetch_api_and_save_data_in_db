import os
import json
import flask
import time
import logging
import requests
from dotenv import load_dotenv, find_dotenv

class FetchAndSaveDataLayer:
    
    def __init__(self, dbConnection):

        self.dbConnection=dbConnection
        load_dotenv(find_dotenv('./../../config/.env'))
        self.DB_NAME = os.getenv('DB_NAME')
        self.USERS_COLLECTION_NAME = os.getenv('USERS_COLLECTION_NAME')
        self.USERS_POST_DATA_COLLECTION_NAME = os.getenv('USERS_POST_DATA_COLLECTION_NAME')
        logging.basicConfig( filename='log_file.log',
                        filemode='a',
                        level=logging.INFO,
                        format= '%(asctime)s - %(levelname)s - %(message)s',
                        )

    # This method saves the users data, received from service layer, into db
    def saveUsersData(self, response):

        db=self.dbConnection.getDbConnection() 
        try:
            for data in response.json()['data']:
                db[self.DB_NAME][self.USERS_COLLECTION_NAME].insert_one(data)
            return response.status_code
        
        except Exception as excep:
            print("Could not save users data into database :", excep)
            print(excep.__class__, "occurred.")
            logging.exception(str(excep))   

    # This method extracts all the user-ids stored into db and send it back to service layer
    def retrieveUsersDataFromDb(self):

        db=self.dbConnection.getDbConnection()
        users_id_list = []

        try:
            users_data = db[self.DB_NAME][self.USERS_COLLECTION_NAME].find()
            for data in users_data:
                users_id_list.append(data['id'])
            return users_id_list

        except Exception as excep:
            print("Unable to fetch user ids from users collection :", excep)
            print(excep.__class__, "occurred.")
            logging.exception(str(excep))

    # This method saves the users post data, received from service layer, into db
    def saveUsersPostData(self, response_data):
        
        db=self.dbConnection.getDbConnection()
        try:
            db[self.DB_NAME][self.USERS_POST_DATA_COLLECTION_NAME].\
                            insert_one(response_data)

        except Exception as excep:
            print("Could not save users post data into database :", excep)
            print(excep.__class__, "occurred.")
            logging.exception(str(excep)) 