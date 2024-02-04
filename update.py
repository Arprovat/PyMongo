from create import get_database

dbname = get_database()
collection = dbname["info"]

old_mark={"mark":90}
new_mark={"$set":{"mark":85}}
collection.update_many(old_mark,new_mark)
for i in collection.find():
    print(i)