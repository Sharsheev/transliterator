import re
# from translit import translite
from connection import connection


def send_response(resp, conn, match):
    if match:
        conn.sendall(resp.encode())
        conn.close()

def write_to_db(match,data):
    if match:
        try:
            with connection.cursor() as cursor:
                sql = """
                INSERT INTO `post_request`.`request` (`first_name`, `last_name`) VALUES (%s,%s)
                """
                # for x in request:
                cursor.execute(sql,(data['firstname'],data['lastname']))
            connection.commit()
        finally:
            connection.close()

def find_form_data(text):
    res = re.search(r"\\r\\n\\r\\n((\w+\=\w+\&?)*)", text).groups()
    try:
        form_data = res[0]
        split_form_data = form_data.split('&')
        d = {}
        for x in split_form_data:
            split_x_data = x.split('=')
            d[split_x_data[0]] = split_x_data[1]
        return d
    except IndexError: pass


# orig = 'Аэропортко акыркы автобус канчада жөнөйт?'
# def translit(word, translit_table):
#     converted_word = ''
#     for char in word:
#         transchar = ''
#         if char in translit_table:
#             transchar = translit_table[char]
#         else:
#             transchar = char
#             converted_word += transchar
#     return converted_word
# print(translit(data, translite))


