# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 6
# Description:
# Develop the automated reservations system including assigning seats by class,
# printing seat map and printing boarding pass by name or seat number

import random

# create variable of total seats in the plane and total seats in the First Class
TOTAL_SEATS = 10
TOTAL_First_Seats = 4

# create variable of number of filled First Class seats and filled Economy Class seats
numFirstFilled = 0
numEconomyFilled = 0

# create the list of string to assign seats to passengers
passengersList = []

# assign empty string ten times to passengersList indicate nobody assigned to that seat
for num in range(TOTAL_SEATS):
    passengersList.append("")
# outside the for loop with number of TOTAL_Seats empty seats

# print out the menu page
print(" 1: Assign Seat")
print(" 2: Print Seat Map")
print(" 3: Print Boarding Pass")
print("-1: Quit\n")

# get user input for menu option
menuOption = int(input("> "))

# while loop to keep asking for user option until -1 is inputted (quit the system)
while menuOption != -1:
    # check if the user input for the menu option is valid
    if menuOption == 1 or menuOption == 2 or menuOption == 3:
        # when user choose to assign seat (option 1)
        if menuOption == 1:
            # check if the flight is full
            # if the flight is not full, assign seats based on the class
            if numFirstFilled + numEconomyFilled < TOTAL_SEATS:
                # ask for passenger's first name
                passengerName = input("Please enter your first name: ")
                # print out instruction for assigning seats based on the class
                print("Type 1 for First Class or Type 2 for Economy.")
                # get user input for the class to assign seat
                firstOrEconomy = int(input(""))
                # if the user choose assign First Class seat
                if firstOrEconomy == 1:
                    # check if the First Class is full
                    # if the First Class is not full, assign passengers to First Class seat
                    if numFirstFilled < TOTAL_First_Seats:
                        # generate a random First Class seat number for the passenger
                        randomNum = random.randrange(TOTAL_First_Seats)
                        # check if that First Class seat number is already assigned
                        while passengersList[randomNum] != "":
                            # if that random First Class seat is assigned, get another random number
                            randomNum = random.randrange(TOTAL_First_Seats)
                        # assign the passenger to that First Class random seat
                        passengersList[randomNum] = passengerName
                        # increment the numFirstSeats when First Class seat is assigned
                        numFirstFilled = numFirstFilled + 1
                    # if the First Class is full
                    else:
                        # ask if passenger would like to be placed in Economy Class
                        replacement = input("If it is acceptable to place you in the Economy class? (y/n): ")
                        # if passenger doesn't want to be placed in the Economy Class
                        # print out message "Next flight leaves in 3 hours."
                        if replacement.lower() == "n":
                            print("Next flight leaves in 3 hours.")
                        # if passenger wants to be placed in the Economy Class, assign them Economy Class seat
                        else:
                            # generate a random Economy Class seat number for the passenger
                            randomNum = random.randrange(TOTAL_SEATS - TOTAL_First_Seats) + TOTAL_First_Seats
                            # check if that Economy Class seat number is already assigned
                            while passengersList[randomNum] != "":
                                # if that random Economy Class seat is assigned, get another random number
                                randomNum = random.randrange(TOTAL_SEATS - TOTAL_First_Seats) + TOTAL_First_Seats
                            # assign the passenger to that Economy Class random seat
                            passengersList[randomNum] = passengerName
                            # increment the numEconomySeats when Economy Class seat is assigned
                            numEconomyFilled = numEconomyFilled + 1
                # if the user choose assign Economy Class seat
                else:
                    # if the Economy Class is not full, assign passengers to Economy Class seat
                    if numEconomyFilled < TOTAL_SEATS - TOTAL_First_Seats:
                        # generate a random Economy Class seat number for the passenger
                        randomNum = random.randrange(TOTAL_SEATS - TOTAL_First_Seats) + TOTAL_First_Seats
                        # check if that Economy Class seat number is already assigned
                        while passengersList[randomNum] != "":
                            # if that random Economy Class seat is assigned, get another random number
                            randomNum = random.randrange(TOTAL_SEATS - TOTAL_First_Seats) + TOTAL_First_Seats
                        # assign the passenger to that Economy Class random seat
                        passengersList[randomNum] = passengerName
                        # increment the numEconomySeats when Economy Class seat is assigned
                        numEconomyFilled = numEconomyFilled + 1
                    # if the Economy Class is full
                    else:
                        # ask if passenger would like to be placed in First Class
                        replacement = input("If it is acceptable to place you in the First class? (y/n): ")
                        # if passenger doesn't want to be placed in the First Class
                        # print out message "Next flight leaves in 3 hours."
                        if replacement.lower() == "n":
                            print("Next flight leaves in 3 hours.")
                        # if passenger wants to be placed in the First Class, assign them First Class seat
                        else:
                            # generate a random First Class seat number for the passenger
                            randomNum = random.randrange(TOTAL_First_Seats)
                            # check if that First Class seat number is already assigned
                            while passengersList[randomNum] != "":
                                # if that random First Class seat is assigned, get another random number
                                randomNum = random.randrange(TOTAL_First_Seats)
                            # assign the passenger to that First Class random seat
                            passengersList[randomNum] = passengerName
                            # increment the numFirstSeats when First Class seat is assigned
                            numFirstFilled = numFirstFilled + 1
            # if the fligt is full, print "Next flight leaves in 3 hours."
            else:
                print("Next flight leaves in 3 hours.")
        # when user choose to print seat map (option 2)
        elif menuOption == 2:
            # print the opening format line
            print("***************************************")
            # use for loop print the seat map
            for index in range(TOTAL_SEATS):
                # print the headline for First Class and Economy Class
                if index == 0:
                    print("First Class:")
                elif index == TOTAL_First_Seats:
                    print("Economy Class:")
                # format the seat map
                # for the tenth seat, align the passengers' name with other 9 seats
                if index != TOTAL_SEATS - 1:
                    # print the message of seat number
                    print("     Seat #" + str(index + 1) + ":    ", end="")
                else:
                    # print the message of seat number
                    print("     Seat #" + str(index + 1) + ":   ", end="")

                # if the seat is empty, print "Empty"
                if passengersList[index] == "":
                    print("Empty")
                # else, print the name of the passenger in that seat
                else:
                    print(passengersList[index])
            # print the ending format line
            print("***************************************\n")
        # when user choose to print boarding pass (option 3)
        elif menuOption == 3:
            # print out the instructions
            print("Type 1 to get Boarding Pass by seat number")
            print("Type 2 to get Boarding Pass by name")
            # ask user which way to print boarding pass
            searchWay = int(input(""))
            # if user want to print boarding pass by giving seat number
            if searchWay == 1:
                seatNumber = int(input("What is the seat number: "))
                if seatNumber >= 1 and seatNumber <= TOTAL_SEATS:
                    # check if the seat is empty
                    # if the seat is empty, print "No passenger has been assigned to this seat"
                    if passengersList[seatNumber - 1] == "":
                        print("No passenger has been assigned to this seat\n")
                    # if the seat is not empty, print out the boarding pass
                    else:
                        print("\n======= BOARDING PASS =======")
                        print("     Seat #:", seatNumber)
                        print("     Passenger Name:", passengersList[seatNumber - 1])
                        print("=============================\n")
                else:
                    print("Invalid number--no boarding pass found\n")
            # if user want to print boarding pass by giving passenger name
            else:
                nameToSearch = input("Enter passenger name: ")
                # make a copy of passengersList of lower cases
                passengersListLower = []
                # append the lower case of every elements in passengersList into passengersListLower
                for item in passengersList:
                    passengersListLower.append(item.lower())
                # check if the passenger has been assigned to a seat ignoring cases
                # if passenger has been assigned to a seat, then print the boarding pass
                if nameToSearch.lower() in passengersListLower:
                    print("\n======= BOARDING PASS =======")
                    print("     Seat #:", passengersListLower.index(nameToSearch.lower()) + 1)
                    print("     Passenger Name:", nameToSearch)
                    print("=============================\n")
                # if the passenger are not assigned to a seat, print out the corresponding message
                else:
                    print("No passenger with name", nameToSearch, "was found\n")
        # update the menuOption
        print(" 1: Assign Seat")
        print(" 2: Print Seat Map")
        print(" 3: Print Boarding Pass")
        print("-1: Quit\n")
        menuOption = int(input("> "))
    # if the user input invalid menu option, ask the option again
    else:
        # update the menuOption
        menuOption = int(input("Please enter choice: "))
# out of while loop

# print out the ending message when user quit the program
print("Have a nice day!")
