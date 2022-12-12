import mysql
from mysql import

config = {
    "user": "Wilson",  # root
    "password": "Test123!",  # root_password
    "host": "127.0.0.1",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Finance;")
    cursor.execute("use Finance;")
    cursor.execute("""CREATE TABLE customer_table (
            customer_id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(255),
            address VARCHAR(255),
            PRIMARY KEY (customer_id)
            );""")

    cursor.execute("""CREATE TABLE transaction_table (
            transaction_id INT NOT NULL AUTO_INCREMENT,
            transaction_amount DECIMAL(13,2),
            customer_id integer,
            DATETIME DATETIME,
            PRIMARY KEY (transaction_id)
            );""")
    db.commit()

    sql = "INSERT INTO customer_table (name, address) VALUES (%s, %s)"

    val = [
        ("John Smith", "444 First St."),
        ("Frank Johnson", "333 Second St."),
        ("Wayne Johnson", "111 Third St."),
        ("Steven Ramos", "222 Fourth St"),
        ("Rylie Quinn", "1234 Transatlantic Rd."),
        ("Sue Yoo", "555 Valley Blvd."),
    ]

    cursor.executemany(sql, val)
    print(cursor.rowcount, "was inserted.")

    sql = "INSERT INTO transaction_table (transaction_amount, customer_id, DATETIME) VALUES (%s, %s, %s)"
    val = [("15000.00", "1", "2022-06-01"),
        ("35000.00", "2", "2022-06-12"),
        ("-2000.00", "2", "2022-06-15"),
        ("8000.00", "3", "2022-06-16"),
        ("-1000.00", "3", "2022-06-18"),
        ("50000.00", "4", "2022-06-27"),
        ("-500.00", "1", "2022-07-01"),
        ("2000.00", "3", "2022-07-05"),
        ("-10000.00", "4", "2022-07-18"),
        ("-2000.00", "2", "2022-07-24"),
        ("45000.00", "5", "2022-07-27"),
        ("100000.00", "6", "2022-07-28"),
        ("-1000.00", "3", "2022-08-04"),
        ("15000.00", "3", "2022-08-05"),
        ("-3500.00", "6", "2022-08-06"),
        ("-4000.00", "5", "2022-08-06"),
        ("-1000.00", "1", "2022-08-07"),
        ("-27000.00", "6", "2022-08-07"),
        ("-3400.00", "6", "2022-08-10"),
        ("-2000.00", "6", "2022-08-11"),
        ("-1000.00", "6", "2022-08-12"),
        ("-5000.00", "6", "2022-08-14"),
        ("-2500.00", "4", "2022-08-15"),
        ("75000.00", "4", "2022-08-15"),
        ("-2000.00", "6", "2022-08-17"),
        ("-2000.00", "4", "2022-08-19"),
        ("5000.00", "1", "2022-08-19"),
        ("-1000.00", "6", "2022-08-20"),
        ("-1000.00", "6", "2022-08-21"),
        ("3500.00",  "1", "2022-08-22"),
        ("-5500.00", "3", "2022-08-22"),
        ("-1500.00", "6", "2022-08-25"),
        ("-6000.00", "5", "2022-09-02"),
        ("-1500.00", "2", "2022-09-04"),
        ("4000.00",  "3", "2022-09-15"),
        ("15000.00", "6", "2022-09-21"),
        ("1000.00", "2", "2022-09-30"),
        ("-1500.00", "1", "2022-10-06"),
        ("-3200.00", "6", "2022-10-15"),
        ("2500.00", "4", "2022-10-21"),
        ("-2500.00", "2", "2022-10-30"),
        ("2100.00", "5", "2022-11-09"),
        ("25000.00", "3", "2022-11-17"),
        ("-10000.00", "3", "2022-11-29"),
        ("-5000.00", "3", "2022-12-01"),
        ("9000.00", "1", "2022-12-02"),
        ("-400.00", "4", "2022-12-02"),
        ("-12500.00", "5", "2022-12-04"),
        ("2300.00", "6", "2022-12-10"),
        ("-2500.00", "1", "2022-12-15"),
    ]
    cursor.executemany(sql, val)
    print(cursor.rowcount, "was inserted.")

    # Commit changes
    db.commit()
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

