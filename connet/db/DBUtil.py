import pymysql


class DBUtil:

    def __init__(self):
        self.conn = pymysql.connect(host="13.59.116.136", user='root', database='minude', password='root')

    def query(self, sql, args):
        cursor = self.conn.cursor()
        cursor.execute(sql, args)
        cursor.close()
        return cursor

    def list(self, sql, mapper, args=None):
        cursor = self.query(sql, args)
        result = cursor.fetchall()
        rtv = []
        for row in result:
            rtv.append(mapper.map(row))
        return rtv

    def find_one(self, sql, mapper, args=None):
        cursor = self.query(sql, args)
        result = cursor.fetchone()
        return mapper.map(result)

    def modify(self, sql, args=None):
        cursor = self.conn.cursor()
        affect_row_count = cursor.execute(sql, args)
        cursor.close()
        self.conn.commit()
        return affect_row_count
