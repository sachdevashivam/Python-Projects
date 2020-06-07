# If the user enters 5 then the program will be directed to - student performance chart
# To create array using mathematical operation we used numpy library as short name - np(just to make it easy to remember)
import numpy as np

# We need to show the array created by numpy as a chart(bar graph) so we used matplotlib as short name - plt
import matplotlib.pyplot as plt

#  Here we created a time array to show our time gap between each term marks x-axis
time = np.array([2, 4, 6, 8, 10])

# Taken input from user for total marks in each term to plot it on a bar graph on y-axis
marks1 = int(input("Enter First-Term Marks: "))
marks2 = int(input("Enter Second-Term Marks : "))
marks3 = int(input("Enter Third-Term Marks: "))
marks4 = int(input("Enter Fourth-Term Marks: "))
marks5 = int(input("Enter Fifth-Term Marks: "))

# converting the user inputs in an array to keep in a particular order and effectively plot on bar graph
marks = [marks1, marks2, marks3, marks4, marks5]

# Here we created a bar graph based on time duration - student marks in each term
bar = plt.bar(time, marks, label= "Student Performance Chart")

# Here we defined labels on x-axis and y-axis to make it more clear to the user
plt.xlabel("Duration (In months)")
plt.ylabel("Marks Obtained")

# Legend() function is used to print the labels
plt.legend()

# show() function is used to display the bar graph
plt.show()



# <------------------------------END OF THE PROJECT--------------------------------------->