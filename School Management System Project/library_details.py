# If the user enters 4 then the program will be directed to - library details
# We have various sub-options in our Library-Menu - 1: Book Issue
#                                                   2: Book Return
#                                                   3: Exit

def LIB_MENU():
    print()
    print()
    print()
    while True:
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t\tWELCOME")
        print("\t\t\t\t\t\t  To")
        print("\t\t\t\tSCHOOL MANAGEMENT SYSTEM")
        print("\t\t\t\t GNPS School - LIBRARY DETAILS ")
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t1 : Book Issue")
        print("\t\t\t\t\t2 : Book Return")
        print("\t\t\t\t\t3 : Exit")
        choice = int(input("Enter Your Choice (1 - 3): "))

        # Aplying condition on user choice
        if choice == 1:
            print("Fill Details: ")
            roll_no = int(input("Enter Student Roll Number: "))
            stu_name = input("Enter Student Name: ")
            book_name = input("Enter Book Name: ")
            # Formatted print statement in such a way we can show the user input in the corresponding output, so we used variables(book_name, stu_name, roll_no) in our print statement
            print(book_name, "Book Successfully Issued by:", stu_name, "with Roll Number:", roll_no)
            break


        if choice == 2:
            book_name = input("Enter Book Name: ")
            print(book_name, "Book Successfully Returned")
            break

        if choice == 3:
            import main_menu



LIB_MENU()
