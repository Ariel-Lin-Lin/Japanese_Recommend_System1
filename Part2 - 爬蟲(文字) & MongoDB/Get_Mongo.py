import pymongo 
from pymongo import MongoClient
def Get_UserInfo(x,y,z,a,b):
    cluster = MongoClient('mongodb+srv://crawler:!QAZ2wsx@cluster0.k1oua.mongodb.net/wear?retryWrites=true&w=majority')
    db = cluster['wear']
    collection = db['test4']
    results = collection.find({})
    feature = [[result[x].split('/')[1],result[y],result[z],result[a],result[b]] for result in results]
    return feature

# aa =Get_UserInfo('Mondel_ID','Mondel_Gender','Mondel_Hight','Mondel_Url','Mondel_Rank')
# print(aa)

def Get_UseBrand(Mondel_ID,brands):
    cluster = MongoClient('mongodb+srv://crawler:!QAZ2wsx@cluster0.k1oua.mongodb.net/wear?retryWrites=true&w=majority')
    db = cluster['wear']
    collection = db['test4']
    results = collection.find({})
    feature = [[result[Mondel_ID].split('/')[1],brand] for result in results for brand in result[brands]]
    return feature

def Get_set(SET_array):
    cluster = MongoClient('mongodb+srv://crawler:!QAZ2wsx@cluster0.k1oua.mongodb.net/wear?retryWrites=true&w=majority')
    db = cluster['wear']
    collection = db['test4']
    results = collection.find({})
    feature = [
        [sets['Set_Url'].split('/')[-3] + "_" + sets['Set_Url'].split('/')[-2],
         sets['Set_Url'].split('/')[-3],
         sets['Like_Num'],
         sets['Update_time'],
         sets['Img_Url']] 
    for result in results for sets in result[SET_array] ]
    return feature

def Get_style(SET_array):
    cluster = MongoClient('mongodb+srv://crawler:!QAZ2wsx@cluster0.k1oua.mongodb.net/wear?retryWrites=true&w=majority')
    db = cluster['wear']
    collection = db['test4']
    results = collection.find({})
    feature = [
        [sets['Set_Url'].split('/')[-3] + "_" + sets['Set_Url'].split('/')[-2],
         style]
    for result in results for sets in result[SET_array] for style in sets['Item_Tag']]
    return feature

def Get_Iteminfo(SET_array):
    cluster = MongoClient('mongodb+srv://crawler:!QAZ2wsx@cluster0.k1oua.mongodb.net/wear?retryWrites=true&w=majority')
    db = cluster['wear']
    collection = db['test4']
    results = collection.find({})
    exist=[]
    feature = []
    for result in results:
        for sets in result[SET_array]:
            for item in sets['ITEM']:
                uniqID = item['Item_Url'].split('/')[-3] + '_' + item['Item_Url'].split('/')[-2] 
                if uniqID not in exist:
                    exist.append(uniqID)
                    tempList = []
                    tempList.append(item['Item_Url'].split('/')[-3] + '_' + item['Item_Url'].split('/')[-2])
                    tempList.append(item['Shop_Url'])
                    tempList.append(item['Item_Type'].split('(')[0])
                    tempList.append(item['Item_Type'].split(')')[0].split('(')[1])
                    tempList.append(item['Item_Brand'])
                    feature.append(tempList)
    return feature


def Get_Item(SET_array):
    cluster = MongoClient('mongodb+srv://crawler:!QAZ2wsx@cluster0.k1oua.mongodb.net/wear?retryWrites=true&w=majority')
    db = cluster['wear']
    collection = db['test4']
    results = collection.find({})
    feature = [
        [sets['Set_Url'].split('/')[-3] + "_" + sets['Set_Url'].split('/')[-2],
         item['Item_Url'].split('/')[-3] + '_' + item['Item_Url'].split('/')[-2] ]
    for result in results for sets in result[SET_array] for item in sets['ITEM']]
    return feature

