import sqlite3
with sqlite3.connect('data.db') as connect:
    cursor = connect.cursor()
    
    id = input('ID : ')

    sql = 'DELETE FROM topics WHERE id = ?'
    cursor.execute(sql, (id))
