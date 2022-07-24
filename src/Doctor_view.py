import mysql.connector
from mysql.connector import Error


def Doc_view():
    try:

        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="nothing_26",
            database="hospital"
        )

        my_cursor = my_data.cursor()

        sql_select_query = "select * from doctors;"

        my_cursor.execute(sql_select_query)
        records = my_cursor.fetchall()
        print("Total number of rows in is: ", my_cursor.rowcount)

        print("\nPrinting each record\n")
        for row in records:
            print("Id : ", row[0], )
            print("Name : ", row[1])
            print("Mobile_no  : ", row[2])
            print("Email  : ", row[3])
            print("Types : ", row[4], "\n")


    except Error as e:
        print("Error reading data from MySQL table : ", e)


    finally:
        if my_data.is_connected():
            my_data.close()
            my_cursor.close()

