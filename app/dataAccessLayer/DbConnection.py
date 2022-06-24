import os
import logging
import pymongo
from dotenv import load_dotenv, find_dotenv

class DbConnection:
    def __init__(self):
        logging.basicConfig( filename='log_file.log',
                        filemode='a',
                        level=logging.INFO,
                        format= '%(asctime)s - %(levelname)s - %(message)s',
                    )
        load_dotenv(find_dotenv('./../../config/.env'))
        self.DB_NAME = os.getenv('DB_NAME')
        self.USERS_COLLECTION_NAME = os.getenv('USERS_COLLECTION_NAME')
        self.USERS_POST_DATA_COLLECTION_NAME = os.getenv('USERS_POST_DATA_COLLECTION_NAME')

    # Establishing mongodb database connection on default host and port
    def getDbConnection(self):
        try:
            myClient = pymongo.MongoClient("mongodb://localhost:27017/")
            myDb = myClient[self.DB_NAME]
            myUsersCollection = myDb[self.USERS_COLLECTION_NAME]
            myPostDataCollection = myDb[self.USERS_POST_DATA_COLLECTION_NAME]
            return myClient
        except Exception as error:
            print('Database access error occured....!')
            print('Error :', error)
            logging.exception(str(error))