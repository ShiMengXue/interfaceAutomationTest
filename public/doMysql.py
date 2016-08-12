# coding=utf-8


import mysql.connector


# 配置数据库连接信息
def mysql_conn():
    conn = mysql.connector.connect(
        host='',
        port='',
        user='',
        passwd='',
        db='db_order',
    )
    return conn

# 更新测试数据库
def update_order_queue():
    sql = ''
    conn = mysql_conn()
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()