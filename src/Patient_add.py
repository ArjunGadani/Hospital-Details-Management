import mysql.connector
from mysql.connector import Error


def Pat_add():
    try:

        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="nothing_26",
            database="hospital"
        )

        my_cursor = my_data.cursor()



        p_name = input("Name : ")
        p_illness = input("Illness : ")
        p_mob = input("Mobile_no : ")
        p_address = input("Address : ")
        query = """INSERT INTO patient(p_name, illness, p_mob, address) VALUES(%s,%s,%s,%s)"""

        data_doctor = (p_name, p_illness, p_mob, p_address)
        my_cursor.execute(query, data_doctor)




        my_data.commit()

        print("\n------Data Inserted Successfully------\n")

    except Error as e:
        print("Error reading data from MySQL table : ", e)


    finally:
        if my_data.is_connected():
            my_data.commit()
            my_data.close()
            my_cursor.close()

