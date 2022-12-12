import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "Wilson",  # root
    "password": "admin",  # root_password
    "host": "127.0.0.1",
    "database":"Finance",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    print("Average Asset Value")
    cursor.execute("select sum(transaction_amount) / count(distinct customer_id) from transaction_table;")
    rows = cursor.fetchall()
    for row in rows:
        for col in row:
            print(round(col, 2), end=" ")
        print()

    cursor = db.cursor()
    print("Clients with more than 10 transactions a month")
    cursor.execute("select customer_table.name, count(transaction_table.transaction_amount) from transaction_table inner join customer_table on customer_table.customer_id=transaction_table.customer_id group by customer_table.name having count(transaction_table.transaction_amount) >= 10;")
    rows = cursor.fetchall()
    for row in rows:
        for col in row:
            print(col, end=" ")
        print()

    cursor = db.cursor()
    print("New Clients added for each month in the past six months")
    cursor.execute("WITH CTE AS (SELECT transaction_table.customer_id, MIN(transaction_table.DATETIME) AS datetimecol FROM transaction_table GROUP BY customer_id) SELECT date_format(datetimecol, '%Y-%m') as mnth, count(distinct customer_id) as num_joined FROM CTE GROUP BY date_format(datetimecol, '%Y-%m') order by mnth desc limit 6;")
    rows = cursor.fetchall()
    for row in rows:
        for col in row:
            print(col, end=" ")
        print()

    # Close connection
    db.close()


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password is invalid")

    elif err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()