# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:40:16 2020

@author: Chaos
"""

from pymongo import MongoClient

# Restful API command
client = MongoClient('mongodb://localhost:27017/')
db = client.jd
collection = db.jd_comments

# searching function
keyword = ''
while True:
    try:
        
        # input keyword with regular expression
        print('Please Type in Keyword: ')
        keyword = input()
        query = {'comment': {'$regex': '.*{}.*'.format(keyword)}}
        doc = collection.find(query)
        
        # output
        if collection.count_documents(query) > 0:
            for item in doc:
                print(item)
        else:
            print('No documents Found. \n')
    except Exception as e:
        print(e)
        break
    
    
    
    
    