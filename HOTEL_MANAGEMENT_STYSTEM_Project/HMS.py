import numpy as np
import matplotlib.pyplot as plt
import random

def HMS():



    while True:
        print()

        print("------------------Welcome to 5 star Hotel---------------------")


        print()

        print("-----------------------MAIN MENU------------------------")
        print()
        print()
        print("1. ----> Customer Details")

        print("2. ----> Room Rent")

        print("3. ----> Restaurant Bill")

        print("4. ----> Laundry Bill")

        print("5. ----> Rating & Feedback")
        print()

        main_menu_choice = int(input("Enter Your Choice: "))





        def customer_details():

            name = input("\nEnter your name: ")
            address = input("\nEnter your address: ")
            check_in = input("\nEnter your check in date(DD MM YYYY): ")
            check_out = input("\nEnter your checkout date(DD MM YYYY): ")
            print()



            print("Please Check Your Details: ")
            print()
            print("Customer Name:", name)
            print("Customer Address:", address)
            print("Customer Check-in Date:", check_in)
            print("Customer Check-out Date:", check_out)




        def room_rent():

            print()
            print()
            print("We have the following rooms for you:-")

            print("1.  type A---->Rs 6000/night")

            print("2.  type B---->Rs 5000/night")

            print("3.  type C---->Rs 4000/night")

            print("4.  type D---->Rs 3000/night")

            print("5.  Exit")
            print()

            while True:
                print()
                choice = int(input("Enter your choice:"))
                print()
                allloted_room = random.randint(100, 200)


                if choice == 1:
                    print("you have opted room type A")
                    print()
                    print("You are allotted room number:", allloted_room)
                    print()

                    nights = int(input("Enter number of night stays: "))

                    total = 6000 * nights
                    print()
                    print("Your Room Rent is: ", total)



                elif choice == 2:
                    print("you have opted room type B")
                    print()
                    print("You are allotted room number:", allloted_room)
                    print()

                    nights = int(input("Enter number of night stays: "))

                    total = 5000 * nights
                    print()
                    print("Your Room Rent is: ", total)



                elif choice == 3:

                    print("you have opted room type C")
                    print()
                    print("You are allotted room number:", allloted_room)
                    print()

                    nights = int(input("Enter number of night stays: "))

                    total = 4000 * nights
                    print()
                    print("Your Room Rent is: ", total)



                elif choice == 4:
                    print("you have opted room type B")
                    print()
                    print("You are allotted room number:", allloted_room)
                    print()

                    nights = int(input("Enter number of night stays: "))

                    total = 3000 * nights
                    print()
                    print("Your Room Rent is: ", total)



                elif choice == 5:
                    break


                else:
                    print("Invalid Input!!")





        def restaurant_bill():

            print()
            print()
            print("--------------------RESTAURANT MENU--------------------")

            print("1. Water----->Rs 20")
            print("2. Tea----->Rs 20")
            print("3. Breakfast----->Rs 110")
            print("4. Lunch----->Rs 100")
            print("5. Dinner----->Rs 120")
            print("6. Exit")


            while True:
                print()
                choice = int(input("Enter your choice:"))


                if choice == 1:

                    quantity = int(input("Enter Quantity: "))
                    total = 20 * quantity
                    print("Your Restaurant bill is Rs:", total)




                elif choice == 2:

                    quantity = int(input("Enter Quantity: "))
                    total = 20 * quantity
                    print("Your Restaurant bill is Rs:", total)




                elif choice == 3:

                    quantity = int(input("Enter Quantity: "))
                    total = 110 * quantity
                    print("Your Restaurant bill is Rs:", total)



                elif choice == 4:

                    quantity = int(input("Enter Quantity: "))
                    total = 100 * quantity
                    print("Your Restaurant bill is Rs:", total)




                elif choice == 5:

                    quantity = int(input("Enter Quantity: "))
                    total = 120 * quantity
                    print("Your Restaurant bill is Rs:",total)



                elif choice == 6:
                    break



                else:
                    print("Invalid Input!!")




        def laundry_bill():

            print()
            print()
            print("---------------------LAUNDRY MENU--------------------------")

            print("1.  Shorts---->Rs 6")
            print("2.  Trouser---->Rs 10")
            print("3.  Shirt/T-shirt---->Rs 8")
            print("4.  Jeans---->Rs 12")
            print("5.  Exit")
            print()

            while True:
                choice = int(input("Enter your choice:"))
                print()

                if choice == 1:
                    quantity = int(input("Enter Quantity: "))
                    print()
                    total = 6 * quantity
                    print("Your Laundry Bill is Rs:", total)
                    print()


                elif choice == 2:
                    quantity = int(input("Enter Quantity: "))
                    print()
                    total = 10 * quantity
                    print("Your Laundry Bill is Rs:", total)
                    print()


                elif choice == 3:
                    quantity = int(input("Enter Quantity: "))
                    print()
                    total = 8 * quantity
                    print("Your Laundry Bill is Rs:", total)
                    print()



                elif choice == 4:
                    quantity = int(input("Enter Quantity: "))
                    print()
                    total = 12 * quantity
                    print("Your Laundry Bill is Rs:", total)
                    print()


                elif choice == 5:
                    break


                else:
                    print("Invalid Input!!")



        def rating_feedback():



            print()
            room_rating = int(input("Rate your room out of 10: "))
            print()

            room_feedback = input("Write your room feedback(optional): ")
            print()


            restaurant_rating = int(input("Rate your food out of 10: "))
            print()

            restaurant_feedback = input("Write your restaurant feedback(optional): ")
            print()

            laundry_rating = int(input("Rate your laundry out of 10: "))
            print()

            laundry_feedback = input("Write your laundry Feedback(optional): ")
            print()

            overall_rating = int(input("Please provide overall Hotel Rating out of 10: "))
            print()

            overall_feedback = input("Write your feedback for our Hotel(optional): ")
            print()

            ratings = {'Room Rating': room_rating,
                       'Restaurant Rating': restaurant_rating,
                       'Laundry Rating': laundry_rating,
                       'Overall Rating': overall_rating}

            a = np.array([1, 2, 3, 4])

            rating_values = list(ratings.values())

            labels = list(ratings.keys())

            plt.bar(a, rating_values, tick_label=labels, label="Customer Feedback Chart", width=0.5, color=['r', 'b'])

            plt.legend()

            plt.show()



        if main_menu_choice == 1:


            customer_details()



        elif main_menu_choice == 2:

            room_rent()




        elif main_menu_choice == 3:

            restaurant_bill()



        elif main_menu_choice == 4:

            laundry_bill()



        elif main_menu_choice == 5:

            rating_feedback()


        else:

            print("Invalid Input!!")



HMS()



































