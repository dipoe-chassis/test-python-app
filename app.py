import os
import logging
from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import generate_password_hash, check_password_hash
#from sqlalchemy import inspect
#from dotenv import load_dotenv
from typing import Optional
from flask_cors import CORS
#load_dotenv() 


app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# logger.info(f'postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('POSTGRES_HOST')}/{os.environ.get('POSTGRES_DB')}')

# app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('POSTGRES_HOST')}/{os.environ.get('POSTGRES_DB')}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)


@app.route('/')
def myhome():
    return jsonify({'deployment' : 'success! ogogogogogo'})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == "admin" and password == "admin":

        return jsonify({'message': 'User registered successfully!'}), 201
    else:
        return jsonify({"message": "NOPE!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username=="admin" and password=="admin":
        return jsonify({'message': 'Logged in successfully'}), 200
    else:
        return jsonify({"message": "NOOOPE!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3656)
