import pymysql
import Get_Mongo
# import charts
# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "12345678",
    "db": "wear",
    "charset": "utf8"
}

try:
# 建立Connection物件
    conn = pymysql.connect(**db_settings)
    # 建立Cursor物件
    with conn.cursor() as cursor:
        UIs = Get_Mongo.Get_UserInfo('Mondel_ID','Mondel_Gender','Mondel_Hight','Mondel_Url','Mondel_Rank')
        UBs = Get_Mongo.Get_UseBrand('Mondel_ID','brands')
        SAs = Get_Mongo.Get_set('SET')
        STs = Get_Mongo.Get_style('SET')
        IIs = Get_Mongo.Get_Iteminfo('SET')
        ITs = Get_Mongo.Get_Item('SET')
        for UI in UIs:
            command = f"INSERT INTO userinfo(Uid, Gender, Height, UserURL, UserRanking)VALUES('{UI[0]}','{UI[1]}', '{UI[2]}', '{UI[3]}', '{UI[4]}');"
            cursor.execute(command)
        for UB in UBs:
            command = f"INSERT INTO oftenusebrand(Uid,brands)VALUES('{UB[0]}','{UB[1]}');"
            cursor.execute(command)
        for SA in SAs:
            command = f"INSERT INTO outfit(OutfitId, Uid, Likes, PicUploadTime, PicUrl)VALUES('{SA[0]}','{SA[1]}', '{SA[2]}', '{SA[3]}', '{SA[4]}');"
            cursor.execute(command)
        for ST in STs:
            command = f"INSERT INTO style(OutfitId,Style)VALUES('{ST[0]}','{ST[1]}');"
            cursor.execute(command)
        for II in IIs:
            command = f"INSERT INTO iteminfo(ItemId, purchaseUrl, ItemType, color, brand)VALUES('{II[0]}','{II[1]}', '{II[2]}', '{II[3]}', '{II[4]}');"
            cursor.execute(command)
        for IT in ITs:
            command = f"INSERT INTO item(OutfitId,ItemId)VALUES('{IT[0]}','{IT[1]}');"
            cursor.execute(command)    
        # 儲存變更
        conn.commit()
    
except Exception as ex:
    print(ex)