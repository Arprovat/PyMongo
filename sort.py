from create import get_database

dbname = get_database()
collection = dbname["info"]
print("descending order")
for i in collection.find().sort("mark",-1):
    print(i)
print("ascending order")
for i in collection.find().sort("mark"):
    print(i)
