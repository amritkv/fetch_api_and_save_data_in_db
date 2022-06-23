from flask_cors import CORS, cross_origin
from app.controller.FetchDataController import app

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

		
if __name__ == '__main__':
   app.run(debug = True)