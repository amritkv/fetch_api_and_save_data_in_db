# Steps to run the application : 

**Step - 1 :** Install mongodb, python 3.x

**Step - 2 :** Open cmd/terminal and run mongodb using `mongod` command

**Step - 3 :** Create a python virtual environment using `python -m venv ./venv` command

**Step - 4 :** Activate the virtual environment --> 
        
        1. ./venv/Sripts/activate.ps1 (for power shell)
        2. ./venv/Sripts/activate (for cmd/terminal)


**Step - 5 :** Install the required packages --> `python -m pip install -r requirements.txt`

**Step - 6 :** Run `python run.py`

**Step - 7 :** Hit the url `localhost:5000/fetchAndSaveUsersData` to fetch and save users data into mongo db

**Step - 8 :** Hit the url `localhost:5000/fetchAndSaveUsersPostData` to fetch and save users post data based on user-id obtained from last step