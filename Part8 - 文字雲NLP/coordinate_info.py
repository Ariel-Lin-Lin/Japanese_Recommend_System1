import pymongo 
from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://crawler:!QAZ2wsx@cluster0.k1oua.mongodb.net/wear?retryWrites=true&w=majority')
db = cluster['wear']
collection = db['Mondel_M']
feature = []
for rank in range(90,101):
    results = collection.find({'Mondel_Rank': str(rank)})
    for result in results: 
        for sets in result['SET']:
            feature.append(sets['Set_Discription'])
        

f = open('./coordinate_info_M.txt', 'a', encoding="utf-8")
for i in feature:
    f.write(i)
f.close()