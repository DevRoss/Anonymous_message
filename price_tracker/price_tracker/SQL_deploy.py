import pymysql

'''
This py script is used to create a mysql database, a table and a new user
'''


# 登录mysql
def db_setup(host='127.0.0.1', user='root', passwd='root',
             db_name='price_tracker', db_table='item',
             new_user='price_tracker', new_user_password='123456')
    conn = pymysql.connect(host=host, user=user, passwd=passwd)

    try:
        with conn.cursor() as cursor:

            # 新建数据库
            cursor.execute('create database if not exists %s' % db_name)
            print('created database price_tracker!')

            # 切换到数据库
            cursor.execute('USE price_tracker')
            print('USE database price_tracker!')

            # 新建数据表
            sql = r'''CREATE TABLE `%s` (
      `site` varchar(255) NOT NULL,
      `id` varchar(200) NOT NULL,
      `name` varchar(255) NOT NULL,
      `price` decimal(10,2) NOT NULL,
      `time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;''' % db_table
            cursor.execute(sql)
            print('created table item!')

            # 新建用户
            '''
            CREATE USER username IDENTIFIED BY 'password'
            '''
            cursor.execute("CREATE USER %s@localhost IDENTIFIED BY '%s'" % (new_user, new_user_password))
            print('created %s, password is %s!' % (new_user, new_user_password))

            # 用户授权
            '''
            GRANT privileges ON databasename.tablename TO WITH GRANT OPTION;
            '''
            cursor.execute("GRANT SELECT, INSERT ON price_tracker.item TO '%s'@'localhost'" % new_user)
            cursor.execute('flush privileges')
            print('user price_tracker is granted!')


    except Exception as error:
        print(error)
        return False
    conn.commit()
    return True
if __name__ == '__main__':

    db_setup(host='127.0.0.1', user='root', passwd='root',
                 db_name='price_tracker', db_table='item',
                 new_user='price_tracker', new_user_password='123456')