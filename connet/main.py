from connet.domain.User import User, UserDao

dao = UserDao()
# result = dao.list()
# for user in result:
#     print(user.id, user.username, user.password)

# user = dao.find_by_id(2)
# print(user.id, user.username, user.password)

# test = User.create("test ", "test")
# dao.insert(test)

# print("===========\n")
# users = dao.find_by_name("xixi")
# for user in users:
#     print(user.id, user.username, user.password)

# users = dao.find_by_id_in([1, 2, 4])
# for user in users:
#     print(user.id, user.username, user.password)

# effect_rows = dao.delete(4)
# print(effect_rows)

effect_rows = dao.delete_by_ids([6])
print(effect_rows)

# user = User(1, "minude", "123456")
# effect_rows = dao.update(user)
# print(effect_rows)

dao.db_util.conn.close()


