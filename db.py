import mysql.connector

conn = mysql.connector.connect(
	host = "",
	user = "",
	password = "",
	database = "",
	port = 3306
)

print("it works")

cur = conn.cursor()
for i in range(100):
	cur.execute("insert into employees (id,name) values (%s,%s)", (i+10,f'name{i}'))
cur.execute("select id,name from employees ")
rows = cur.fetchall()
for row in rows:
	print(f"ID: {row[0]} and Name: {row[1]}")

conn.commit()
cur.close()
conn.close()
