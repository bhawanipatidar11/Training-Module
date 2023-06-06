import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Webkorps@111222"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("Use mydatabase")

# mycursor.execute("create table yt(name varchar(10), id int(5) ,salery int(10))")

mycursor.execute("Insert into yt(name , id , salery)values("Akash" , 01 , 1200)")

mydb.commit()

