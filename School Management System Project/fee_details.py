# If the user enters 3 then the program will be directed to - fee menu
# We have various sub-options in our Fee-Menu - 1: Fee Deposit
#                                               2: Fee Details
#                                               3: Exit

# Here we need another database to store the fee details

import sqlite3 as sql

print()
print()
print()
def FEE_MENU():
    while True:
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t\tWELCOME")
        print("\t\t\t\t\t\t  To")
        print("\t\t\t\tSCHOOL MANAGEMENT SYSTEM")
        print("\t\t\t\t GNPS School - FEE DETAILS ")
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t1 : Fee Deposit")
        print("\t\t\t\t\t2 : Fee Details")
        print("\t\t\t\t\t3 : Exit")
        choice = int(input("Enter Your Choice (1 - 3): "))

        # Connecting to our new database - school_mgmt_fee
        connect = sql.connect('school_mgmt_fee.db')
        cursor = connect.cursor()

        # Created table into database - fee_details
        cursor.execute("""CREATE TABLE IF NOT EXISTS fee_details(Roll_no integer,Stu_name text,Fee_amount integer)""")

        # Created functions to store and retrieve fee details
        def fee_deposit():
            roll_no = int(input("Enter your Roll Number: "))
            stu_name= input("Enter Student Name: ")
            fee_amount = int(input("Enter Fee Amount: "))

            cursor.execute("INSERT INTO fee_details VALUES (:Roll_no, :Stu_name, :Fee_amount)",{'Roll_no': roll_no, 'Stu_name' : stu_name, 'Fee_amount' : fee_amount})
            print("Fee Successfully Paid")
            connect.commit()
            connect.close()


        def show_fee_details():
            print()
            print("Your Fee Details: ")
            cursor.execute("SELECT * FROM fee_details")
            print(list(cursor.fetchall()))
            connect.commit()
            connect.close()

        # Applied conditions on user choice and called above created functions

        if choice == 1:
            print("Successfully Connected to Database")
            fee_deposit()
            break


        if choice == 2:
            print("Successfully Connected to Database")
            show_fee_details()
            break


        if choice == 3:
            import main_menu

        else:
            print("Invalid Input!!")



FEE_MENU()
