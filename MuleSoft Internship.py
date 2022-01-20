import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user = "root",passwd = "1234",database = "movies")

mycursor = mydb.cursor()

mycursor.execute("select * from favmovies")

result= mycursor.fetchall()

for i in result:
    print(i)
