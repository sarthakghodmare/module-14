import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("select c1,c5 from test2.test_table")
for i in mycursor.fetchall():
    print(i)
mydb.commit()
mydb.close()