# change source_id and run
import mysql.connector
cnx = mysql.connector.connect(user='root', password='aceuser123',
                              host='se-db.prod-se.aws.learningace.com',
                              database='centralized_content')
cur=cnx.cursor()
cur.execute('select attr_value from config_repo_arp.config_repo where attr_key = "ace_db";')
db_list = cur.fetchall()
counter=0
for db in db_list:
    # print(db[0])
    cur.execute("SELECT round(((data_length + index_length) / 1024 / 1024), 2) 'Size in MB' FROM information_schema.TABLES WHERE table_schema = '{0}' AND table_name = 'document_optional_fields_deprecate'".format(db[0]));
    reclist=cur.fetchall()
    for rec in reclist:
        if rec[0] is None:
            continue
        else:
            counter+=rec[0]
print ("Total Size: "+str(counter))
cnx.close()
