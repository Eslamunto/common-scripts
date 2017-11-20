import json
from urllib.request import urlopen
import urllib
from pymongo import MongoClient
import config

# mongo config START
mongoClient = MongoClient()
mongoClient = MongoClient(config.IP_ADDRESS, config.PORT_NUMBER)
database = mongoClient[config.DATABASE_NAME]
collection = database[config.COLLECTION]

# fetch the json objects
response = urllib.request.urlopen(config.URL)
str_response = response.readall().decode('utf-8')
json_obj = json.loads(str_response)

for entry in json_obj['content']:
    # store in db
    collection.insert(entry)