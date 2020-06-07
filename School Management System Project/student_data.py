# If the user enters 2 then the program will be directed to - student data menu
# We have various sub-options in our Admission-Menu - 1: Fill Student Details
#                                                     2: Show Student Details
#                                                     3: Search
#                                                     4: Delete
#                                                     5: Update Student Details
#                                                     6: Exit

# Here we need another database to store the student details
import sqlite3 as sql

print()
print()
print()
def STU_MENU():
    while True:
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t\tWELCOME")
        print("\t\t\t\t\t\t  To")
        print("\t\t\t\tSCHOOL MANAGEMENT SYSTEM")
        print("\t\t\t\t GNPS School - Student Data")
        print("\t----------------------------------------------------")
        print("\t\t\t\t\t1 : Add Student Record")
        print("\t\t\t\t\t2 : Show Student Details")
        print("\t\t\t\t\t3 : Search")
        print("\t\t\t\t\t4 : Delete")
        print("\t\t\t\t\t5 : Update Student Details")
        print("\t\t\t\t\t6 : Exit")
        choice = int(input("Enter Your Choice (1 - 6): "))

        # Here we are connecting to a new database - school_mgmt2
        connection = sql.connect('school_mgmt2.db')
        cursor = connection.cursor()

        # Created a new table into our database - student_details
        cursor.execute("""CREATE TABLE IF NOT EXISTS student_details(
                               Roll_no integer,
                               Stu_name text,
                               Address text,
                               Std integer,
                               Stream text)""")

        # Below created functions to store, retrieve, delete, update student details
        # Student Details input from user
        def fill_details():
            roll_no = int(input("Enter Roll number: "))
            stu_name = input("Enter Student Name: ")
            address = input("Enter your Address: ")
            std = int(input("Enter Standard: "))
            stream = input("Enter Stream: ")

            # Inserting these details into student
            cursor.execute("INSERT INTO student_details VALUES (:Roll_no, :Stu_name, :Address, :Std, :Stream)",
                           {'Roll_no': roll_no, 'Stu_name': stu_name, 'Address':address, 'Std':std, 'Stream':stream})

            connection.commit()
            connection.close()

        def show_details():
            cursor.execute("SELECT * FROM student_details")
            print(list(cursor.fetchall()))
            connection.commit()
            connection.close()


        def search():
            stu_name = input("Enter Student Name: ")
            cursor.execute("SELECT * FROM student_details WHERE Stu_name=?", (stu_name,))
            print(list(cursor.fetchone()))
            connection.commit()
            connection.close()


        def delete():
            roll_no = int(input("Enter Roll number as your password: "))
            cursor.execute("DELETE from student_details WHERE Roll_no= roll_no")
            print("Data Successfully Deleted")
            connection.commit()
            connection.close()


        def update():
            roll_no = int(input("Enter Roll number as your password: "))
            print("Enter Updated Details:- ")
            stu_name = input("Enter Student Name: ")
            address = input("Enter Address: ")
            std = int(input("Enter Standard: "))
            stream = input("Enter Stream: ")

            cursor.execute("UPDATE student_details set Stu_name= stu_name where Roll_no= roll_no")
            print("Data Successfully Updated")
            connection.commit()
            connection.close()

        # Applied conditions on user choice and called above functions
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

        elif choice == 6:
            import main_menu

        else:
            print("Invalid Input!!")



STU_MENU()