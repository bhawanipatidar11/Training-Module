import mysql.connector 

mydb  = mysql.connector.connect(host = "localhost" , user = "root" , password = "Webkorps@111222")

cursor = mydb.cursor()

# cursor.execute("Create database d1")
# print("Database created")

cursor.execute("use d1")
print("Used database")

# cursor.execute("create table T1(name varchar(10),age int(3),departement varchar(10),salery int(5))")
# print("Table created")

# cursor.execute("Insert into T1(name ,age,departement,salery) values ('Akash' , 12 , 'electro' , 1200)")
# cursor.execute("Insert into T1(name ,age,departement,salery) values ('Daksh' , 19 , 'machanic' , 13000)")
# cursor.execute("Insert into T1(name ,age,departement,salery) values ('Rohit' , 25 , 'engineer' , 12000)")
# cursor.execute("Insert into T1(name ,age,departement,salery) values ('Ansh' , 24 , 'developer' , 10000)")
mydb.commit()