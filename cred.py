import urllib
import pymongo
from pymongo import MongoClient

mango_url = "mongodb+srv://npranavx:" + urllib.parse.quote_plus("Pr@nav123") + "@npxbot-bfw7s.mongodb.net/test"
cluster = MongoClient(mango_url)
db = cluster["npx-bot"]
collection = db["search_results"]
Token = 'NzE1Mjc4NjEwOTk0NDMwMDEz.Xs65zg.W6WLVTM7qgVJY80EYG1uu3A06lA'
