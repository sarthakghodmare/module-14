import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_table values(123,'sarthak',21.3,31,'ghodmare')")
mycursor.execute("insert into test2.test_table values(123,'sarthak',21.3,31,'ghodmare')")
mycursor.execute("insert into test2.test_table values(123,'sarthak',21.3,31,'ghodmare')")
mycursor.execute("insert into test2.test_table values(123,'sarthak',21.3,31,'ghodmare')")
mydb.commit()
mydb.close()