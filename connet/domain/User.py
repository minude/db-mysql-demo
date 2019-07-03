from connet.db.DBUtil import DBUtil


class User:

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def create(cls, username, password):
        return cls(None, username, password)


class UserDao:

    def __init__(self):
        self.db_util = DBUtil()
        self.mapper = UserMapper()

    def list(self):
        sql = "select id, username, password from `t_user`"
        return self.db_util.list(sql, self.mapper)

    def find_by_id(self, id):
        sql = "select id, username, password from `t_user` where id = %s"
        return self.db_util.find_one(sql, self.mapper, [id])

    def insert(self, user):
        sql = "insert into `t_user`(username, password) values (%s, %s)"
        return self.db_util.modify(sql, [user.username, user.password])

    def find_by_name(self, name):
        sql = "select id, username, password from `t_user` where username like '%%%s%%'" % name
        return self.db_util.list(sql, self.mapper)

    def find_by_id_in(self, ids):
        sql = "select id, username, password from `t_user` where id in (%s)" % ','.join(['%s'] * len(ids))
        return self.db_util.list(sql, self.mapper, ids)

    def delete(self, id):
        sql = "delete from `t_user` where id = %s"
        return self.db_util.modify(sql, id)

    def delete_by_ids(self, ids):
        sql = "delete from `t_user` where id in (%s)" % ','.join(['%s'] * len(ids))
        return self.db_util.modify(sql, ids)

    def update(self, user):
        sql = "update `t_user` set username = %s, password = %s where id = %s"
        return self.db_util.modify(sql, [user.username, user.password, user.id])


class UserMapper:

    @staticmethod
    def map(row):
        return User(row[0], row[1], row[2])
