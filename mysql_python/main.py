import pymysql.cursors

# Connect to the database
# Подключаемся к базе данных
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='sodle260800',
                             db='bancomat',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

connect_owner = ['asan']
try:
    with connection.cursor() as cursor:
        sql = """
        INSERT INTO `connect_owner` (`first_name`,`last_name`,`@mail`,`password`) VALUES (%s,%s,%s,%s)
        """
        for x in connect_owner:
            cursor.execute(sql, ('asan','azoaknkjs','IrinaShaike@mail.ru','123456789'))
    connection.commit()
# try:
    # with connection.cursor() as cursor:
        # Create a new record
        # Создаем новую запись
        # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()
# try:
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT * FROM `germany_cars` WHERE model LIKE 'Gelendwagen' or marka = 'BMW'"
#         cursor.execute(sql, ())
#         result = cursor.fetchall()
#         print(result)
finally:
    connection.close()
