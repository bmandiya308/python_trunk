import MySQLdb as db
import sys
import pandas as pd
def mysql_connect():
    try:
        dbh = db.connect("localhost","root","root","govt")
        dbh.autocommit(False)
        print("connected sucessfully")
    except:
        print("Can't connect to database")
        sys.exit()
    return dbh

dbh = mysql_connect()
cursor = dbh.cursor(db.cursors.DictCursor)
cursor.execute("select * from users")
records = cursor.fetchall()
#df = pd.DataFrame(records,columns=['one', 'two','three','four','five'])
df = pd.DataFrame(records)
#print(records)
'''
for record in records:
    print(record['first_name'])
'''
print(df)
print(df['id'] * 2)
cursor.close()
dbh.close()
