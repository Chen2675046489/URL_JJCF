import pymysql.cursors
import json
from conf.settings import *


class OperationMysql:

    def __init__(self):
        """使用构造函数对数据库进行全局连接"""
        try:
            self.conn = pymysql.connect(
                host=MYSQL_HOST,
                port=MYSQL_PORT,
                user=MYSQL_DB_USER,
                password=MYSQL_DB_PASSWORD,
                charset='utf8',
                db=MYSQL_DB_NAME,
                cursorclass=pymysql.cursors.DictCursor)
            self.cursor = self.conn.cursor()
            print('------连接成功------')
        except pymysql.err:
            print('------链接出错------')

    def search_one(self, sql):
        """查询数据，返回一条数据"""
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        return result

    def search_several(self, sql):
        """查询数据，返回多条"""
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def insert_sql(self, *sql):
        """插入sql语句"""
        try:
            for i in range(0, len(sql)):
                print(sql[i])
                self.cursor.execute(sql[i])
        except Exception as e:
            self.conn.rollback()
            print("事物执行失败", e)
        else:
            self.conn.commit()


if __name__ == '__main__':
    op_mysql = OperationMysql()
    sql = "INSERT INTO `g_qihuo_trade_time`(`exg`, `type_name`, `trade_time`, `minute_count`) VALUES ('DCE', 'LPP', '21:00-23:00 9:00-10:15 10:30-11:30 13:30-15:00', 346)"
    op_mysql.insert_sql(sql)

