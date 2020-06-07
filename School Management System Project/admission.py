# If the user enters 1 then the program will be directed to this admission menu
# We have various sub-options in our Admission-Menu - 1: Fill Admission Details
#                                                     2: Show Admission Details
#                                                     3: Search
#                                                     4: Delete
#                                                     5: Update Admission Details
#                                                     6: Exit

# To store and retrieve our admission details we need a database so we used sql sub-module --> sqlite3
import sqlite3 as sql

print()
print()
print()


def ADM_MENU():
    while True:
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t\tWELCOME")
        print("\t\t\t\t\t\t  To")
        print("\t\t\t\t\t SCHOOL MANAGEMENT SYSTEM")
        print("\t\t\t\t\tABC School Admission Menu")
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t1 : Fill Admission Details")
        print("\t\t\t\t\t2 : Show Admission Details")
        print("\t\t\t\t\t3 : Search")
        print("\t\t\t\t\t4 : Delete")
        print("\t\t\t\t\t5 : Update Admission Details")
        print("\t\t\t\t\t6 : Exit")
        choice = int(input("Enter Your Choice (1 - 6): "))

        # Here we are establishing a connection with database named - school_mgmt
        connection = sql.connect('school_mgmt.db')

        # Here we created a cursor to make changes in our database by applying operations like insert, select, delete etc.

        cursor = connection.cursor()

        # Here we are creating a table(admission_details) with column names to store our data
        cursor.execute("""CREATE TABLE IF NOT EXISTS admission_details(
                       Adm_no integer,
                       Roll_no integer,
                       Stu_name text,
                       Address text,
                       Phn_num integer)""")

        # Creating functions to implement the sub-categories of content entered by user

        def fill_details():
            # Taking data as input from user to store into our database(school_mgmt)
            adm_no = int(input("Enter Admission number: "))
            roll_no = int(input("Enter Roll number: "))
            stu_name = input("Enter Student Name: ")
            address = input("Enter Address: ")
            phn_num = int(input("Enter Phone number: "))

            # Inserting the values input from user into our table.
            cursor.execute("INSERT INTO admission_details VALUES (:Adm_no, :Roll_no, :Stu_name, :Address, :Phn_num)",
                           {'Adm_no': adm_no, 'Roll_no': roll_no, 'Stu_name': stu_name, 'Address': address,
                            'Phn_num': phn_num})
            # We need to close the database connection after performing tasks.
            connection.commit()
            connection.close()
        #     Selecting and showing values entered by used
        def show_details():
            cursor.execute("SELECT * FROM admission_details")
            # Printing data into list format
            print(list(cursor.fetchall()))
            connection.commit()
            connection.close()
        # To select, search and show a particular user's data
        def search():
            stu_name = input("Enter Student Name: ")
            cursor.execute("SELECT * FROM admission_details WHERE Stu_name=?", (stu_name,))

            # cursor.execute("SELECT * FROM admission_details WHERE Stu_name= stu_name")
            print(list(cursor.fetchone()))
            connection.commit()
            connection.close()

        # To delete data
        def delete():
            roll_no = int(input("Enter Roll number as your password: "))
            cursor.execute("DELETE from admission_details WHERE Roll_no= roll_no")
            print("Data Successfully Deleted")
            connection.commit()
            connection.close()

        # To update data
        def update():
            roll_no = int(input("Enter Roll number as your password: "))
            print("Enter Updated Details:- ")
            adm_no = int(input("Enter Admission number: "))
            stu_name = input("Enter Student Name: ")
            address = input("Enter Address: ")
            phn_num = int(input("Enter Phone number: "))

            cursor.execute("UPDATE admission_details set Adm_no= adm_no where Roll_no= roll_no")
            print("Data Successfully Updated")
            connection.commit()
            connection.close()

        # Applied conditions and calling above created functions
        if choice == 1:
            print("Successfully Connected to Database")
            fill_details()

            print("Record Successfully Created")
            break


        elif choice == 2:
            print("Successfully Connected to Database")
            print(show_details())
            break

        elif choice == 3:
            print("Successfully Connected to Database")
            search()
            break

        elif choice == 4:
            print("Successfully Connected to Database")
            delete()
            break

        elif choice == 5:
            print("Successfully Connected to Database")
            update()
            break
        # If user enters 6(exit) the code will be redirected to Main-Menu
        elif choice == 6:
            import main_menu

        else:
            print("Invalid Input!!")


ADM_MENU()
