import pymysql as mysql
import settings


def openConMysql(host, user, pwd, db):
    con = mysql.connect(host=host, user=user, passwd=pwd, db=db, cursorclass=mysql.cursors.SSDictCursor)
    cur = con.cursor()
    return cur


def closeConMysql(con):
    con.close()

print(settings.HOST["user"], settings.HOST["host"], settings.HOST["db"], settings.HOST["pwd"])
if (__name__=="__main__"):
    openConMysql(settings.HOST["host"], settings.HOST["user"], settings.HOST["db"], settings.HOST["pwd"])

