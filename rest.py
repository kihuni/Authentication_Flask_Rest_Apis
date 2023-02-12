from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__) # Creating a flask application

auth = HTTPBasicAuth() # Creating a new instance AUTH from HTTPBasicAuth

@app.route('/rest-auth') # Decorator(associate url with function in flask) "creates a new route for the flask app"

@auth.login_requred # Decorator "ensures only logged in users access the resources"

def get_response():
    return jsonify('You are authorised to see this message')

@auth.verify_password # Decorator "used to register a function that verifies username and password"
def authenticate(username, password):
    if username and password:
        if username == 'name' and password == "password":
            return True
        else:
            return False
        return False

if __name__ == "__main__":
    app.run()