# CSV FILE WITH INSTRUCTORS WHO HAVE ACTIVE COURSE FROM UNIVERSITY OF COLORADO DENVER
# import MongoClient
# import datetime for date handling
import csv
import datetime
from pymongo import MongoClient
#Create a connection
# establish iclicker prod connection
# credentials for prod
produser='shiva'
prodpwd='Intellus-022'
client = MongoClient(host='mongodb://192.178.1.28:27017/',username=produser,password=prodpwd,authSource='reef',authMechanism='SCRAM-SHA-1')
with client:
    # connect to a database in prod
    db=client.reef
    # aggregate query
    agr=[\
          { "$match":{\
           "$and":[\
              { "institutionName":{ "$eq":"University of Colorado Denver" } },\
              { "endDate":{ "$gte":datetime.datetime(2019,8,22) } }\
                     ]\
           }\
          }\
        ,\
          { "$lookup":\
             { "from":         "user",\
               "localField":   "userId",\
               "foreignField": "_id",\
               "as":           "userInfo"\
             }\
          },\
          { "$unwind":  "$userInfo" },\
          { "$lookup":\
             { "from":         "credentials",\
               "localField":   "userId",\
               "foreignField": "userId",\
               "as":           "credentialsInfo"\
             }\
          },\
          { "$unwind":  "$credentialsInfo" },\
          { "$match":{\
                "credentialsInfo.access.role":{ "$eq":"facilitator" }\
           }\
          }\
        ,\
          { "$project": { \
                  "instructorName": 1  ,  \
                  "userInfo.email": 1  \
                 }\
          },\
          { "$group":{ "_id":{ "instructorName":"$instructorName" ,"userInfo_email":"$userInfo.email"  },\
             "count":{"$sum":1}\
             }\
             },\
        ]    \
    # storing the result as list
    data=list(db.course.aggregate(agr))
    # define output file path
    fileName='iclicker_denver_instructors.csv'
    # define output headers
    # headers=['InstructorName','email']
    # open output file and write the output
    with open(fileName,'w',newline="") as csvfile:
        # define csv writer
        writer=csv.writer(csvfile,delimiter=' ', quotechar='|',quoting=csv.QUOTE_MINIMAL)
        fieldnames=['InstructorName','|','email']
        # write output headers
        writer.writerow(fieldnames)
        # writer output rows
        for x in data:
            print(x['_id']['instructorName'],":",x['_id']['userInfo_email'])
            writer.writerow([x['_id']['instructorName'],x['_id']['userInfo_email']])
            # writer.writerow([])
