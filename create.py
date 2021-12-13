import sqlite3
# connect = sqlite3.connect('data.db')
with sqlite3.connect('data.db') as connect:

    cursor = connect.cursor()

    title = input('Title : ')
    body = input('Body : ')

    sql = 'INSERT INTO topics (title, body) VALUES(?,?)'
    cursor.execute(sql, (title, body))

    cursor2 = connect.cursor()
    sql = 'INSERT INTO topics (title, body) VALUES(?,?)'
    cursor2.execute(sql, (title, body))

    print('id', cursor.lastrowid)
    print('id', cursor2.lastrowid)
