# This is the Main-Menu (front page) of School App
# We have various contents in our Main-Menu - 1: Admission
#                                             2: Student Data
#                                             3: Fee Details
#                                             4: Library Details
#                                             5: Student Performance Chart
# To get further into these contents user need to enter the corresponding number (eg - Press 1 for admission and so on.)

# Firstly, we defined a function to write our code more efficiently and get
# So, Let's create our Main_Menu - called if required in the entire project.

def MAIN_MENU():
    # Here we are doing some formatting using print() to make our output more attractive.
    # The entire formatting is done inside a while loop to keep the Main Menu(Output) continue until the user selects any option.
    print()
    print()
    print()
    while True:
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t\tWELCOME")
        print("\t\t\t\t\t\t  To")
        print("\t\t\t\tSCHOOL MANAGEMENT SYSTEM")
        print("\t\t\t\t GNPS School - MAIN MENU")
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t1 : Admission")
        print("\t\t\t\t\t2 : Student Data")
        print("\t\t\t\t\t3 : Fee Details")
        print("\t\t\t\t\t4 : Library Details")
        print("\t\t\t\t\t5 : Student Performance Chart")
# Taking input from user
        choice = int(input("Enter Your Choice (1 - 5): "))

# Conditions Applied if the user enters any number
        # Here we have imported self-created python modules (like - admission, student_data.....) to get into the corresponding content.
        if choice == 1:
            import admission
            break
        elif choice == 2:
            import student_data
            break
        elif choice == 3:
            import fee_details
            break
        elif choice == 4:
            import library_details
            break

        elif choice == 5:
            import student_performance


# Finally we have called our function to execute it.
MAIN_MENU()









