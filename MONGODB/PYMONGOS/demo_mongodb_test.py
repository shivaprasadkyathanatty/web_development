# sudo systemctl stop mongodb
# sudo systemctl status mongodb
# sudo systemctl start mongodb
# sudo systemctl restart mongodb
# TO ALLOW REMOTE SERVER ACCESS MONGODB
# sudo vi /etc/mongodb.conf
# bind_ip = 127.0.0.1,your_server_ip)
# import pymongo to start working on mongodb
import pymongo
import pandas as pd

# establish client connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# create database named "mydatabase"
mydb=myclient["tutorial"]
#mydb = myclient["mydatabase"]
# print all databases in myclient
# print(myclient.list_database_names())
# # check if the new database "mydatabase" exists
# # MongoDB wont create database unless collection is created
# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#     print("The database exists.")
# else:
#     print("The database doesnt exists.")
# # create collection "customers"
# # In MongoDB, a collection is not created until it gets content
mycol = mydb["tutorial_table"]
# print(mydb.list_collection_names())
# collist = mydb.list_collection_names()
# if "customers" in collist:
#     print("The collection exists.")
# else:
#     print("The collection doesnt exists.")
# #A document in MongoDB is the same as a record in SQL databases.
# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
# #Insert another record into mycol
# mydict = { "name": "Peter", "address": "Lowstreet 27" }
# x = mycol.insert_one(mydict)
# #Insert many records into mycol
# mylist=[
# {
#    'title': 'MongoDB Overview',
#    'description': 'MongoDB is no sql database',
#    'by_user': 'tutorials point',
#    'url': 'http://www.tutorialspoint.com',
#    'tags': ['mongodb', 'database', 'NoSQL'],
#    'likes': 100
# },
# {
#    'title': 'NoSQL Overview',
#    'description': 'No sql database is very fast',
#    'by_user': 'tutorials point',
#    'url': 'http://www.tutorialspoint.com',
#    'tags': ['mongodb', 'database', 'NoSQL'],
#    'likes': 10
# },
# {
#    'title': 'Neo4j Overview',
#    'description': 'Neo4j is no sql database',
#    'by_user': 'Neo4j',
#    'url': 'http://www.neo4j.com',
#    'tags': ['neo4j', 'database', 'NoSQL'],
#    'likes': 750
# }
# ]
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = mycol.insert_many(mylist)

# print(x.inserted_ids)
# #Insert with specific ids
# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
#
# x = mycol.insert_many(mylist)
# #print list of the _id values of the inserted documents:
# print(x.inserted_ids)
# find the first document in the collection "customers"
# x = mycol.find_one()
# print(x)

#find all documents in the collection "customers"
# for x in mycol.find():
#     print(x)
#return only specific fields and not the id
# for x in mycol.find({},{"_id":0,"name":1}):
#     print(x)
#return all fields except id
# for x in mycol.find({},{"_id":0}):
#     print(x)
#to return exclusive fields one of the field should be _id and the value it contains 0/1 should not be matched
# the below will give error
# for x in mycol.find({},{"_id":0,"name":0,"address":1}):
#     print(x)
# query with exclusive value
# myquery = { "address": "Park Lane 38" }
# mydoc = mycol.find(myquery)
# for x in mydoc:
#   print(x)

# to find the documents where the "address" field starts with the letter "S" or higher (alphabetically), use the greater than modifier: {"$gt": "S"}:
# myquery = { "address": { "$gt": "S" } }
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#   print(x)

#To find only the documents where the "address" field starts with the letter "S", use the regular expression {"$regex": "^S"}:
# myquery = { "address": { "$regex": "^S" } }
#
# mydoc = mycol.find(myquery)
#
# for x in mydoc:
#   print(x)

# The sort() method takes one parameter for "fieldname" and one parameter for "direction" (ascending is the default direction).
# mydoc = mycol.find().sort("name")
# for x in mydoc:
#   print(x)
# Use the value -1 as the second parameter to sort descending.
# sort("name", 1) #ascending
# sort("name", -1) #descending
# mydoc = mycol.find().sort("name", -1)
#
# for x in mydoc:
#   print(x)
#To delete one document, we use the delete_one() method.
# The first parameter of the delete_one() method is a query object defining which document to delete.
# Note: If the query finds more than one document, only the first occurrence is deleted.
# Delete the document with the address "Mountain 21":
# myquery = { "address": "Mountain 21" }
# mycol.delete_one(myquery)
# Delete all documents were the address starts with the letter S:
# To delete more than one document, use the delete_many() method.
# The first parameter of the delete_many() method is a query object defining which documents to delete.
# myquery = { "address": {"$regex": "^S"} }
# x = mycol.delete_many(myquery)
# print(x.deleted_count, " documents deleted.")
# Delete All Documents in a Collection
# To delete all documents in a collection, pass an empty query object to the delete_many() method:
# Delete all documents in the "customers" collection:
# x = mycol.delete_many({})
# print(x.deleted_count, " documents deleted.")
# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
# Delete the "customers" collection:
# mycol.drop()

# Lowstreet 27

# Apple st 652
# Update Collection
# You can update a record, or document as it is called in MongoDB, by using the update_one() method.
# The first parameter of the update_one() method is a query object defining which document to update.
# Note: If the query finds more than one record, only the first occurrence is updated.
# The second parameter is an object defining the new values of the document.
# myquery = { "address": "Apple st 652" }
# newvalues = { "$set": { "address": "Apple st 662" } }
# mycol.update_one(myquery, newvalues)
# Update Many
# To update all documents that meets the criteria of the query, use the update_many() method.
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

myresult = mycol.find().limit(5)
#print the result:
#Aggregation
#Basic syntax of aggregate() method is as follows −
#db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
#db.mycol.aggregate([{$group:{_id:"$by_user",num_tutorial:{$sum:1}}}])
#db.mycol.aggregate([{$group : {_id : "$by_user", num_tutorial : {$sum : 1}}}])

# myresult=mydb.mycol.aggregate(
#             [
#                 {"$group" :
#                     {"_id" : "$by_users",
#                         "num_tutorial" : {"$sum" : 1}
#                     }
#                 }
#             ]
#         );
#
df = pd.DataFrame(list(myresult))
col_3=df.iloc[1:3]
# first = df["title"]
print (col_3)

# for x in myresult:
#   print(x)

for i,j in df.iterrows():
    print(i,j)
    print()

# print (df.nunique(axis=1))
print(df.shape)
print(df.ndim)

name=['shiva','ssv','palani','buddha','mukul']
id=[21,25,100,101,22]
emplist=list(zip(id,name))

empdf=pd.DataFrame(emplist,columns=["EmpID","EmpName"])

print(empdf)

n_tutorials=mydb.mycol.count_documents()
print(n_tutorials)
