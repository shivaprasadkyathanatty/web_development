# https://macmillanlearning.atlassian.net/browse/ITO-182
# XLSX FILE WITH DISTINCT DISCIPLINES
# import MongoClient
# import excel writer
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
          { "$group":{     "_id":{ "discipline":"$discipline"  }, \
                     "count":{"$sum":1} \
              }\
          },\
          { "$project": { \
                  "_id.discipline": 1  \
                 }\
          },\
        ]\
    # storing the result as list
    data=list(db.course.aggregate(agr))
    # define output file path
    fileName='disciplines.xls'
    # define output sheet name
    sheetName='disciplines'
    # open output file and write the output
    workbook = xlsxwriter.Workbook(fileName)
    worksheet=workbook.add_worksheet(sheetName)
    bold = workbook.add_format({'bold':True})
    # write header row
    worksheet.write(0,0,'Disciplines',bold)
    row = 1
    col = 0
    # write value cells
    for x in data:
        worksheet.write(row,col,x['_id']['discipline'])
        row+=1
    workbook.close()
