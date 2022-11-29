# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 3
# Description:
# Use the while loop to output the largest, smallest, and average number
# among all the numbers user inputs until they input -1.

# use the while loop to repeat the program until user inputs n/N
another = "y"
while another == "y":
    # ask for the first input of the user
    print("Input an integer greater than or equal to 0 or -1 to quit: ")
    num1 = int(input("> "))

    # initialize the variable for counting the number of numbers user inputs
    count = 0

    # initialize the variable to store the largest and smallest numbers
    largest = num1
    smallest = num1

    # initialize the variable for summing all the numbers user inputs
    numSum = 0

    # keep asking for numbers until user inputs -1
    while num1 != -1:
        count = count + 1
        numSum = numSum + num1
        if num1 > largest:
            largest = num1
        if num1 < smallest:
            smallest = num1
        num1 = int(input("> "))
    if numSum != 0:
        print("The largest number is", str(largest))
        print("The smallest number is", str(smallest))
        print("The average number is", str(numSum / count))
        print("")

    # ask user if they would like to enter another set of numbers
    another = input("Would you like to enter another set of numbers? (y/n): ").lower()
# Goodbye message
print("")
print("Goodbye!")
