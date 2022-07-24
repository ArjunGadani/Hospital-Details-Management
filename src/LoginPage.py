from getpass import getpass


def Login_h():
    uid = "admin"
    password = "admin"

    max_try = 0
    while max_try < 3:
        log_id = getpass("\nEnter Login Id : ")
        log_pass = getpass("Enter Password : ")

        if uid != log_id and password != log_pass:
            print("Enter Correct Id Or Pass !")
        else:
            print("\nLogin Successfully !\n\n")
            break

