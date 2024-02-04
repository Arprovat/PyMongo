from create import get_database
dbname = get_database()
collection =dbname["info"]
for i in collection.find():
    print(i)
for i in collection.find({},{"_id":0}):
    print(i)
for i in collection.find({},{"_id":0,"name":0}):
    print(i)
for i in collection.find({},{"_id":0}):
    print(i["name"])
