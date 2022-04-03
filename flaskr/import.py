import sqlite3
import csv

con = sqlite3.connect('../menu.sqlite')
cur = con.cursor()

create_menu = \
    'CREATE TABLE IF NOT EXISTS menu (id INTEGER, name STRING, category STRING, type STRING, price INTEGER)'
cur.execute(create_menu)

delete_menu = 'DELETE FROM MENU'
cur.execute(delete_menu)

open_csv = open('./utils/menu.csv')

read_csv = csv.reader(open_csv)

next_row = next(read_csv)

rows = []
for row in read_csv:
    rows.append(row)

cur.executemany(
    'INSERT INTO menu (id, name, category, type, price) VALUES (?,?,?,?,?)',
    rows
)

con.commit()
open_csv.close()

con.close
