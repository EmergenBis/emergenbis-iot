from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
import db_config as database


class Arduinos(Resource):
    """ Get all posts """
    def get(self):
        response = list(database.db.arduino.find())

        for doc in response:
            doc['_id'] = str(doc['_id'])

        return jsonify(response)

    def delete(self):
        return database.db.arduino.delete_many({}).deleted_count