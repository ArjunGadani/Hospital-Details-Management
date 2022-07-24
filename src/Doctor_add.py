import mysql.connector
from mysql.connector import Error


def Doc_add():
    try:

        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="nothing_26",
            database="hospital"
        )

        my_cursor = my_data.cursor()


        d_name = input("Name : ")
        d_mob_no = input("Mob_no : ")
        d_email = input("Email : ")
        d_type = input("Type : ")
        query = """INSERT INTO doctors(name, mob_no, email, type) VALUES(%s,%s,%s,%s)"""

        data_doctor = (d_name, d_mob_no, d_email, d_type)
        my_cursor.execute(query, data_doctor)


    except Error as e:
        print("Error reading data from MySQL table : ", e)


    finally:
        if my_data.is_connected():
            my_data.commit()
            print("\n------Data Inserted Successfully------\n")
            my_data.close()
            my_cursor.close()


