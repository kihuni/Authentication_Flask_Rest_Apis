from flask import Flask
from json import jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__) # Creating a flask application

auth = HTTPBasicAuth() # Creating a new instance AUTH from HTTPBasicAuth

@app.route('/rest-auth') # Decorator(associate url with function in flask) "creates a new route for the flask app"

@auth.login_requred # Decorator "ensures only logged in users access the resources"

def get_response():
    return jsonify('You are authorised to see this message')

if __name__ == "__main__":
    app.run()