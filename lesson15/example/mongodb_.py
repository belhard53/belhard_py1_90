r"""

mongod --dbpath D:\PROGRAMS\mongoDB\bin\db\    
служба - C:\MongoDb\mongod.exe --config C:\MongoDb\mongo.config --install

 mongo.config
    dbpath=C:\MongoDb\data
    logpath=C:\MongoDb\log\mongo.log
"""


'''
консоль
use shop        // выбрать/создать базу
show dbs        // посмотреть базы



База данных
База данных (database) — это верхний контейнер, в котором лежит набор коллекций.​
В терминах SQL это примерно как «сама БД» с набором таблиц; обычно одно приложение работает со своей отдельной базой.​
Примеры имён баз: shop, blog, analytics.

Коллекция
Коллекция (collection) — это группа документов внутри базы, аналог таблицы в реляционной БД.​
Коллекция хранит документы с произвольной (необязательной общей) схемой — структура может различаться от документа к документу.​
Примеры коллекций: в базе shop могут быть users, orders, products.

'''        
        

from pymongo import MongoClient        

client = MongoClient()        
        
# client = MongoClient('localhost', 27017) # 127.0.0.1
# client = MongoClient('mongodb://localhost:27017/')        

db = client.test5 #если н ет создаст



print(1, db.list_collection_names())        

users = db.users4 # выбрать коллекцию или создать
users = db["users7"] # выбрать коллекцию или создать

# CRUD

# C -------------------------------------
d1 = {"name": "John0", "address": "Highway4"}
x = users.insert_one(d1)

docs = [
    {"name": "Bob", "age": 30, "city": "Chicago"},
    {"name": "Charlie", "age": 35},
    {"name": "David"}
]

x = users.insert_many(docs)
print(x)


# R -----------------------------

all_users = list(users.find())

for user in users.find(): # cursor
        print(user)


# for doc in users.find({"age": {"$gt": 27}}):
#     print("Filtered:", doc)
    
# alice = users.find_one({"name": "Alice"})
# print("Alice:", alice)    


# x = users.find({"address": "Highway2"})
# x = users.find({"address": "Highway2"}).limit(2)
# x = users.find({"address": "Highway2"}).skip(2).limit(2)
# x = users.find({"address": "Highway2"}).skip(2)
# x = users.find({},{"name": True}).sort('name')

# U ---------------------------------------
# users.update_one(
#     {"name": "Alice"},
#     {"$set": {"age": 26}}
# )

# users.update_many(
#     {"age": {"$lt": 30}},
#     {"$inc": {"age": 1}}
# )

# D -----------------------------

# users.delete_one({"name": "David"})
# # # users.delete_many({})

# count = users.count_documents({})
# print("Docs count:", count)


