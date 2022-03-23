import sqlite3

connection = sqlite3.connect("employee_list.db")

cursor = connection.cursor()

rows = cursor.execute("select id, name from list")
rows = list(rows)
print(rows)
rows = [{"id":row[0], "name":row[1]} for row in rows]
print(rows)

print("done.")