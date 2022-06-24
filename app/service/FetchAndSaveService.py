class FetchAndSaveService:
    def __init__(self, fetchAndSaveDataLayer):
        self.fetchAndSaveDataLayer = fetchAndSaveDataLayer
        print("Initialized 'Fetch and Save Data' service....!")
    
    def fetchUersData(self):

        fetch_and_save_data_status=self.fetchAndSaveDataLayer.fetchUsersData()
        return fetch_and_save_data_status