#!/usr/bin/python3

import pymysql
def getData():

    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "root", "demoboot")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from auth_user")

    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    array=cursor.fetchall()


    #print(tuple(array))

    # 关闭数据库连接
    db.close()
    return array