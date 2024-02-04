from create import get_database

dbname = get_database()
collection=dbname["info"]
dic={'name':'john','mark':45}
collection.insert_one(dic)
dic1={'name':'provat','mark':70}
dic2={'name':'proven','mark':90}
collection.insert_many([dic1,dic2])
print("successfully inserted collection")