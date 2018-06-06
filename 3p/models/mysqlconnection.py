import settings
import pymysql


def openConMysql():
    con = pymysql.connect(settings.HOST["host"], settings.HOST["user"], settings.HOST["passwd"], settings.HOST["db"])

    return con


def closeConMysql(con):
    con.close()


if (__name__ == "__main__"):
    openConMysql()
