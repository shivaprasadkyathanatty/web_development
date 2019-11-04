import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["tutorial"]
mycol = mydb["tutorial_table"]
myresult = mycol.find().limit(10).explain();
print(myresult)
