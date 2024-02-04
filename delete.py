from create import get_database

dbname = get_database()
collection = dbname["info"]
for i in collection.find():
    print(i)
    
delet={"mark":70}
collection.delete_one(delet)
delet={"mark":45}
collection.delete_many(delet)
print("After delete")
for i in collection.find():
    print(i)