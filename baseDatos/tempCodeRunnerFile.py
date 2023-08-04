import mysql.connector

base=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    #database=""
)

print(type(base))
cursor=base.cursor()
cursor.execute("show databases")
print(cursor)
for data in cursor:
    print(data)