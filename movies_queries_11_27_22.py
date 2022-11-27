import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

cnx = mysql.connector.connect(user='movies_user', password='popcorn',
                              host='localhost',
                              database='movies')
# creating a new cursor on connection to host
cursor = cnx.cursor()
# storing the SELECT statement in the variable query
query = "SELECT * from studio"
# executing the operation stored in the query variable using the execute() method
cursor.execute(query)
# fetching all rows from the last executed statement on the cursor.
result = cursor.fetchall()
print("--DISPLAYING Studio RECORDS--")
# looping through the rows and printing required columns
for row in result:
    print("Studio ID:", row[0])
    print("Studio Name:", row[1])
    print(" ")

# displaying genre data
query = "SELECT * from genre"
cursor.execute(query)
result = cursor.fetchall()
print("--DISPLAYING Genre RECORDS--")
for row in result:
    print("Genre ID:", row[0])
    print("Genre Name:", row[1])
    print(" ")
# displaying films whose runtime is less than 120 minutes.
query = "SELECT film_name,film_runtime from film where film_runtime<120 "
cursor.execute(query)
result = cursor.fetchall()
print("--DISPLAYING Short Film RECORDS--")
for row in result:
    print("Film Name:", row[0])
    print("Runtime:", row[1])
    print(" ")
# displaying director's and their info in order.
query = "SELECT film_name,film_director from film order by film_director "
cursor.execute(query)
result = cursor.fetchall()
print("--DISPLAYING Director RECORDS in Order--")
for row in result:
    print("Film Name:", row[0])
    print("Director:", row[1])
    print(" ")
# close the cursor
cursor.close()
# close the connection
cnx.close()
