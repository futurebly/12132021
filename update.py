import sqlite3
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()
    id = input('ID for Update : ')
    sql = 'SELECT id,title,body FROM topics WHERE id = ?'
    cursor.execute(sql, (id,))
    row = cursor.fetchone()
    title = row[1]
    body = row[2]
    input_title = input('Title ('+title+'):')
    input_body = input(f'Body ({body}):')

    sql = 'UPDATE topics SET title=?, body=? WHERE id=?'
    cursor.execute(sql, (input_title, input_body, id))