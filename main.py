from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
from flask_cors import CORS
from bson.json_util import dumps, ObjectId
import db_config as database

#Resources
#from res.users import Users
from res.arduino import Arduino
from res.arduinos import Arduinos

app = Flask(__name__)
api = Api(app)

CORS(app)




api.add_resource(Arduino, '/new_trap/', '/<string:by>:<string:data>/')
api.add_resource(Arduinos, '/all_traps/', '/delete/all_traps/')


if __name__ == '__main__':
    app.run(load_dotenv = True)