from LoginPage import Login_h
from Doctor_view import Doc_view
from Doctor_add import Doc_add
from Patient_view import Pat_view
from Patient_add import Pat_add
from Bill_Generator import Bill_


def Verification():
    Login_h()


Verification()


def main_view():

    max_try = 1

    while max_try == 1:
        print("\n----- Welcome yAyA Hospital -----\n\n")

        print("1. Doctor's Details--->\n")
        print("2. Patient's Details--->\n")
        print("3. Exit--->\n")

        h_option = int(input("Select Any Option : "))

        if h_option == 1:

            print("\n1. View Doctor's Details--->\n")
            print("2. Add Doctor's Details--->\n")
            print("3. Go Back\n")

            d_option = int(input("Select Any Option : "))

            if d_option == 1:
                Doc_view()
                continue

            elif d_option == 2:
                Doc_add()
                continue

            elif d_option == 3:
                main_view()

            else:
                print("\nPlease Give Valid Input...\n")
                continue


        elif h_option == 2:
            print("\n1. View Patient's Details--->\n")
            print("2. Add Patient's Details--->\n")
            print("3. Generate Patient's Bill--->\n")
            print("4. Go Back\n")

            d_option = int(input("Select Any Option : "))

            if d_option == 1:
                Pat_view()

            elif d_option == 2:
                Pat_add()

            elif d_option == 3:
                Bill_()

            elif d_option == 4:
                main_view()

            else:
                print("\nPlease Give Valid Input...\n")
                continue

        elif h_option == 3:
            print("\n")
            exit()

        else:
            print("\nSorry Incorrect Input...\n")
            main_view()


main_view()

