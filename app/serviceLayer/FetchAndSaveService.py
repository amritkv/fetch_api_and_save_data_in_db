import os
import logging
import requests
from dotenv import load_dotenv, find_dotenv


class FetchAndSaveService:

    def __init__(self, fetchAndSaveDataLayer):
        self.fetchAndSaveDataLayer = fetchAndSaveDataLayer
        print("Initialized 'Fetch and Save Data' service....!")
        load_dotenv(find_dotenv('./../../config/.env'))
        self.APP_ID = os.getenv('APP_ID')
        self.USERS_DATA_URL = os.getenv('USERS_DATA_URL')
        self.USERS_POSTS_DATA = os.getenv('USERS_POSTS_DATA')
    
    # This service layer method calls the external API to get the users data
    def fetchAndSaveUersDataService(self):
        
        try:
            request_header = {"Content-Type": "application/json", "app-id" : self.APP_ID}
            response = requests.get(url=self.USERS_DATA_URL, headers=request_header)
            fetch_and_save_data_status = self.fetchAndSaveDataLayer.saveUsersData(response)
            return fetch_and_save_data_status

        except Exception as error:
            print("Error in fetching users data :", error)
            print(error.__class__, "occurred.")
            logging.exception(str(error))
        
    # This service layer methos calls data layer method to get all the user-ids stored 
    # in users table and on the basis of each user-ids, it calls external api to get
    # users post data
    def fetchAndSaveUsersPostDataService(self):

        try:
            user_id_list = self.fetchAndSaveDataLayer.retrieveUsersDataFromDb()
            request_header = {"Content-Type": "application/json", "app-id" : self.APP_ID}
            for single_user_id in user_id_list:
                updated_url = self.USERS_POSTS_DATA.replace('{{user_id}}', single_user_id)
                response = requests.get(url=updated_url, headers=request_header)
                users_post_data = {single_user_id : response.json()['data']}
                self.fetchAndSaveDataLayer.saveUsersPostData(users_post_data)
            return 1

        except Exception as error:
            print("Error in fetching users post data :", error)
            print(error.__class__, "occurred.")
            logging.exception(str(error))



        