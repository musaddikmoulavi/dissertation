# server.py

from flask import Flask, request, jsonify, send_from_directory
import util
import os
from flask_cors import CORS

app = Flask(__name__, static_folder='/template', static_url_path='', template_folder='/template')
CORS(app)

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_location_names/<city>', methods=['GET'])
def get_location_names(city):
    response = jsonify({
        'locations': util.get_location_names(city)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()
    city = data['city']
    area_sqft = float(data['area_sqft'])
    location = data['location']
    bedrooms = int(data['bedrooms'])
    bathrooms = int(data['bathrooms'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(city, location, area_sqft, bedrooms, bathrooms)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    print("To run the app you need to go to the 'template' folder and open 'app.html'")
    app.run(host='0.0.0.0', port=8000, debug=True)







# from flask import Flask, request, jsonify, send_from_directory
# import util
# from flask_cors import CORS

# app = Flask(__name__, static_folder='../client', static_url_path='', template_folder='../client')

# # app = Flask(__name__)
# CORS(app)

# @app.route('/')
# def home():
#     return send_from_directory(app.static_folder, 'index.html')


# @app.route('/get_location_names/<city>', methods=['GET'])
# def get_location_names(city):
#     response = jsonify({
#         'locations': util.get_location_names(city)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# @app.route('/predict_home_price', methods=['POST'])
# def predict_home_price():
#     data = request.get_json()
#     city = data['city']
#     area_sqft = float(data['area_sqft'])
#     location = data['location']
#     bedrooms = int(data['bedrooms'])
#     bathrooms = int(data['bathrooms'])

#     response = jsonify({
#         'estimated_price': util.get_estimated_price(city, location, area_sqft, bedrooms, bathrooms)
#     })
#     print(data)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


# if __name__ == '__main__':
#     print("Starting Python Flask Server For Home Price Prediction...")
#     util.load_saved_artifacts()
#     # app.run(host='0.0.0.0')
#     app.run()    

# if __name__ == '__main__':
#     print("Starting Python Flask Server For Home Price Prediction...")
#     util.load_saved_artifacts()
#     app.run(debug=True)



# # trial
# from flask import Flask, request, jsonify
# import util

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Welcome to the Home Price Prediction API"

# @app.route('/get_location_names/<city>', methods=['GET'])
# def get_location_names(city):
#     response = jsonify({
#         'locations': util.get_location_names(city)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# @app.route('/predict_home_price/<city>', methods=['POST'])
# def predict_home_price(city):
#     total_sqft = float(request.form['total_sqft'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])

#     response = jsonify({
#         'estimated_price': util.get_estimated_price(city, location, total_sqft, bhk, bath)
#     })
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


