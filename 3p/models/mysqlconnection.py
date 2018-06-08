import settings
import pymysql


def openConMysql():
    con = pymysql.connect(settings.HOST_MM["host"], settings.HOST_MM["user"], settings.HOST_MM["passwd"], settings.HOST_MM["db"])

    return con

def openConMysqlHome():
    con = pymysql.connect(settings.HOST_HOME["host"], settings.HOST_HOME["user"], settings.HOST_HOME["passwd"], settings.HOST_HOME["db"])

    return con



def closeConMysql(con):
    con.close()


if (__name__ == "__main__"):
    openConMysql()
