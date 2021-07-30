import MySQLdb as db
import sys
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
cursor = dbh.cursor()
cursor.execute("select * from users")
records = cursor.fetchall()
for row in records:
    print(row)
cursor.execute("insert into users values(3,'Sachin','Bairagi','sbairagi','sbairagi')")
cursor.execute("select * from users")
records = cursor.fetchall()
print("Second iteration")
for row in records:
    print(row)
cursor.execute("delete from users where id in (3)")
dbh.commit()
cursor.close()
dbh.close()
