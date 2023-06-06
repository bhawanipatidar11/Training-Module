import mysql.connector as ms

mydb = ms.connect(host = "localhost",user = "root" ,password = "Webkorps@111222",database = "youtube")

cursor = mydb.cursor()

cursor.execute("insert into yt (videos,salery,suscribe) values(11,1200,3000)")

mydb.commit()

print("row inserted")
