# https://macmillanlearning.atlassian.net/browse/ITO-182
# XLSX FILE WITH CHEMISTRY DISCIPLINE CURATED COURSE INSTRUCTORS DETAILS
# import MongoClient
# import Excel writer
import xlsxwriter
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
              { "discipline":{ "$eq":"Chemistry" } },\
              { "name":{ "$regex":"Chem" } }\
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
          { "$project": {\
                  "institutionName": 1  ,\
                  "instructorName": 1  ,\
                  "userInfo.email": 1  ,\
                  "discipline": 1  ,\
                  "name": 1\
                 }\
          },\
        ]\

    # storing the result as list
    data=list(db.course.aggregate(agr))
    # define output file path
    fileName='chemistryInstructors.xlsx'
    # open output file and write the output
    # define output sheet name
    sheetName='chemistryInstructors'
    # define output headers
    headers=['InstitutionName','Discipline','CourseName','InstructorName','Email']
    # open output file and sheet for writing the output
    workbook = xlsxwriter.Workbook(fileName)
    worksheet=workbook.add_worksheet(sheetName)
    # define bold setting for any cells you may want to use in future (ex:header row)
    bold = workbook.add_format({'bold':True})
    # write header row
    row=0
    col=0
    for x in headers:
        worksheet.write(row,col,x,bold)
        col+=1
    # write value rows
    row = 1
    col = 0
    for x in data:
        worksheet.write(row,col,x['institutionName'])
        worksheet.write(row,col+1,x['discipline'])
        worksheet.write(row,col+2,x['name'])
        worksheet.write(row,col+3,x['instructorName'])
        worksheet.write(row,col+4,x['userInfo']['email'])
        row+=1
    workbook.close()
