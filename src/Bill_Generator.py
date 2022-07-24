import mysql.connector
from mysql.connector import Error


def Bill_():
    try:

        my_data = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="nothing_26",
            database="hospital"
        )

        my_cursor = my_data.cursor()

        bill_for = int(input("\nEnter The Id Of Patient : "))

        my_cursor.execute("""select * from patient where p_id = %s""" % bill_for)
        row = my_cursor.fetchone()


        if row is None:
            print("\nINVALID ID PLEASE CHECK AND INSERT AGAIN...\n")
            Bill_()

        else:

            print("----------------------------------------------------------------")
            print("yAyA HOSPITAL\nyAyA BUILDING,\nyAyA GALI,\nCHANDKHEDA  ")
            print("----------------------------------------------------------------")
            print("MEDICAL INVOICE")
            print("----------------------------------------------------------------")
            print("----------------------------------------------------------------")
            print("Patient Name : ", row[1])
            print("Patient Mobile_no: ", row[3])
            print("Patient Address: ", row[4] , "\n")
            print("----------------------------------------------------------------")
            print("\t\t\t\t\t\tDescription ")
            print("----------------------------------------------------------------")
            print("----->", row[2], "\n\n\n\n")
            print("----------------------------------------------------------------")
            print("Total Bill Amount :\t\t\t\t\t", row[5])



    except Error as e:
        print("Error reading data from MySQL table : ", e)


    finally:
        if my_data.is_connected():
            my_data.close()
            my_cursor.close()


# Bill_()
