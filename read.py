import sqlite3
with sqlite3.connect('data.db') as connect:

    cursor = connect.cursor()

    sql = 'SELECT id,title,body FROM topics'
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2])