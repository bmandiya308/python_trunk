# import module sys to get the type of exception
import sys
import MySQLdb as db

randomList = ['a', 0, 2, 6]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except ValueError:
        print("ValueError - Oops!",sys.exc_info()[0],"occured.")
        # handle ValueError exception
        pass
    except (TypeError, ZeroDivisionError):
        print("ZeroDivisionError - Oops!",sys.exc_info()[0],"occured.")
        # handle multiple exceptions
        # TypeError and ZeroDivisionError
        pass
    except:
        print("DAFAULT - Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
    finally:
        print("its a final block - randomList")

print("The reciprocal of",entry,"is",r)

try:
    print("in block")
    out = open('a2','r')
except:
    print("New statement - ops!",sys.exc_info()[0]," occured")
finally:
    print("its a final block - FILE OPEN")

## Sql exception
def mysql_connect():
    try:
        dbh = db.connect("localhost","root1","root","govt")
        dbh.autocommit(False)
        print("connected sucessfully")
    except db.Error:
        print("MySQLdb._exceptions.OperationalError - Oops!",sys.exc_info()[0],"occured.")
        sys.exit()
        # handle multiple exceptions
        # TypeError and ZeroDivisionError
        pass
    except:
        print("Can't connect to database - ",sys.exc_info()[0]," Occured")
        sys.exit()
    finally:
        print("its a final block - DB CONNECT")
    return dbh

dbh = mysql_connect()
try:
    cursor = dbh.cursor()
    cursor.execute("select * from users")
except:
    print("Sql Execution Failed - ",sys.exc_info()[0]," Occured")
finally:
    print("its a final block - DB EXECUTE")
records = cursor.fetchall()

for row in records:
    print(row)

