# lab3.py
# Mohamed Kharaev
from pathlib import Path
from bs4 import BeautifulSoup
import string
import pymongo
import nltk
import math
import datetime

def parse_for_text(page):
    text = open(page)
    try:
        soup = BeautifulSoup(text, "html.parser")
        text.close()
        print("put in")
        return str(soup.get_text())
    except:
        text.close()
        print("except")
        return ""

def tokenize(data):
    return nltk.tokenize.word_tokenize(data)

def index(filepath):
    return (str(filepath.parent.name) + "/" + str(filepath.name))



if __name__ == "__main__":
    starttime = datetime.datetime.now()
    folders = [folder for folder in Path("WEBPAGES_RAW").iterdir() if folder.is_dir()]
    mongoclient = pymongo.MongoClient()
    db = mongoclient['index']
    tokens = db.tokens
    for folder in folders:
    for page in folder.iterdir():
        p_index = index(page)
        tokenized_list = [token.lower() for token in tokenize(parse_for_text(page)) if len(token) > 3]
        document_len = len(tokenized_list)
        for token in set(tokenized_list):
            tf = tokenized_list.count(token)/document_len
            if tokens.find({"token": token}).count() > 0:
                tokens.update(
                    {'token': token},
                    {'$addToSet': {'URLs': [p_index, tf]}}
                    )
            else:
                t = {
                    'token': token,
                    'URLs': [[p_index, tf]],
                }
                tokens.insert_one(t)

    for token in tokens.find({}):
        for index in token['URLs']:
            index[1] = index[1] * (math.log(25) / len(token['URLs']))
            print(index)
    print(starttime)
    print(datetime.datetime.now())
 
# tf = (# of token in doc) / (# of docs)
# idf = ln( (# of docs) / (# of docs with token) )
# tfidf = tf * idf
