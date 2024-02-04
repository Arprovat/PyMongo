from create import get_database
dbname=get_database()
collections=dbname["info"]

mark={"mark":90}

for i in collections.find(mark):
    print(i)
for i in collections.find(mark):
    print(i["name"])