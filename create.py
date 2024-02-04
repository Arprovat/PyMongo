from pymongo import MongoClient

def get_database():
    client=MongoClient("mongodb://localhost:27017")
    db= client["people"]
    return db

if __name__== "__main__":
    
    db=get_database()
    collection=db["info"]
    dic={'name':'john','mark':45}
    collection.insert_one(dic)
    dic1={'name':'provat','mark':70}
    dic2={'name':'proven','mark':90}
    dic3={'name':'nadim','mark':80}
    dic4={'name':'sahadat','mark':60}
    collection.insert_many([dic1,dic2,dic3 ,dic4])
    