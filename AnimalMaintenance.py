# CS-340 Client/Server Development
# Project One
# Marco Aldana
# 02/07/21

import pymongo
import urllib
import json


class AnimalMaintenance(object):

    def __init__(self, username, password):
        # Parse username and password to resolve error below
        # 'Username and Password must be escaped according to RFC 3986.
        parsed_username = urllib.parse.quote_plus(username)
        parsed_password = urllib.parse.quote_plus(password)

        # Setup Client, Database and Collection
        self.client = pymongo.MongoClient('mongodb://%s:%s@localhost:39450' % (parsed_username, parsed_password))
        self.database = self.client['AAC']
        self.collection = self.database['animals']

    # CREATE: Accepts a data object and inserts into collection using Mongo's Insert API function
    def create(self, data):
        if data is not None:
            inserted = self.collection.insert(data)

            if inserted:
                return "True"
            else:
                return "False"
        else:
            raise Exception("Nothing to save, data parameter is empty")

    # READ: Accepts a data object and uses Mongo's find API function to
    #       return a result set given the key/value specified.
    def read(self, data):
        if data is not None:
            return self.collection.find(data)
        else:
            raise Exception("Nothing to query, data parameter is empty")

    # UPDATE: Accepts query criteria to find an document and update query criteria to update the
    #         document specified. Returns a formatted JSON result set based on if the update
    #         is successful or not.
    def update(self, find_data, update_data):
        if find_data is not None:
            current_data = self.collection.find(find_data)

            if current_data is not None:
                return json.dumps(self.collection.update_one(find_data, update_data).raw_result, indent=4)
        else:
            raise Exception("Nothing to update, data parameter is empty")
            
    # DELETE: Accepts a data object to locate the desired document to delete and uses PyMongo's
    #         delete_one method to remove the document. Returns a formatted JSON result set based on if
    #         the deletion is successful or not.
    def delete(self, data):
        if data is not None:
            return json.dumps(self.collection.delete_one(data).raw_result, indent=4)
        else:
            raise Exception("Nothing to Delete, data parameter is empty")

