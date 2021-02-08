# __author__ = 'harshaltaware'
from flask import Flask
from flask import jsonify, request, Response,Blueprint
import logging
import json
import os
import sys
from AuthHandler import Auth


app = Flask(__name__)

# Get the custom logger instance for this utility

#testing microservices
@app.route('/test', methods=['GET'])
def print_hello():
    return "Hello"

#check return status and serialize it to json
@app.route('/get_status', methods=['GET'])
def get_status():
    status = {"status": "status OK"}
    return jsonify(status)

#authenticate user credentials
@app.route('/authenticate-user', methods=['POST'])
def authenticate_user():
    AuthObj = Auth()
    # request_data = request.get_data()
    request_data = '{"username": "user123", "password": "user123"}'
    request_data = json.loads(request_data)
    authentication_status = AuthObj.authenticate_username_pass(request_data)
    print(authentication_status)
    return jsonify(authentication_status)
