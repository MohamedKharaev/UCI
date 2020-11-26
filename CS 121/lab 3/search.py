# Search.py
import pymongo
import json
import heapq
from scipy import spatial

def create_json_dict(file):
    with open(file) as f:
        data = json.load(f)
        f.close()
        return data
        
def retrieve_url(index, json_dict):
    return json_dict[index]

def print_search_results(token, json_dict):
    for word in set(token.split()):
        search_result = tokens.find_one({'token': word})
        if search_result is not None:
            for result in heapq.nlargest(10, search_result['URLs'], key=lambda e:e[1]):
                print(retrieve_url(result[0], json_dict))

if __name__ == "__main__":
    mongoclient = pymongo.MongoClient()
    db = mongoclient['index']
    tokens = db.tokens
    json_dict = create_json_dict("WEBPAGES_RAW/bookkeeping.json")
    while True:
        search = input("Search: ").lower()
        print_search_results(search, json_dict)
