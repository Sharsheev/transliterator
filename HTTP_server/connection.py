import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='sodle260800',
                             db='post_request',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

