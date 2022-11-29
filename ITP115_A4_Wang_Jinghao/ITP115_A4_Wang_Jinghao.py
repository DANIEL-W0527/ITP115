# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 4
# Description:
# Part 1: count how many times each letter appears in the input sentence
# and how many special characters(not spaces and letters) occur
# Part 2: Roll a 20-sided dice for 10 times with random cases playing
# and tell the user what's the case they are playing and valid numbers to win
# and output the final score for 10 plays

import random

# Part 1
# create an variable to store all the english characters
letters = "abcdefghijklmnopqrstuvwxyz"

# print out the header of the program
print("PART 1 - Character Counter")

# get the sentence from the user
sentence = input("Please enter a sentence: ")

# print out the header of result message
print("\nHere is the character distribution:\n")

# create a variable to count how many special characters in the input sentence
specialCount = 0

# use for loop check every single character in the input sentence
for character in sentence:
    # if lowercase of the character is not in the letters
    # and if the character is not space
    # then count that character is a special character
    if character.lower() not in letters and character != ' ':
        specialCount = specialCount + 1
# outside the for loop
# print out the message about special characters
print("special characters:", "*" * specialCount)

# use for loop to count how many time each character appears in the sentence
# loop through every single alphabet letter
for letter in letters:
    # initialize the variable to count how many times each character appears
    # this count variable could be automatically updated for each character
    count = 0
    # loop through every single character in the input sentence
    for character in sentence:
        # if the lower case of the character in the sentence equals
        # the letter looping through, count once that letter appears
        if character.lower() == letter:
            count = count + 1
    # outside the inner for loop

    # print out the summary for character
    # if the letter does not appear in the sentence print "NONE"
    if count == 0:
        print((letter + ": NONE"))
    # if the letter appears in the sentence for count times
    # print "*" that many times
    else:
        print(letter + ":", "*" * count)
# outside the outer for loop

# print the separate empty line between Part 1 and Part 2
print("\n")


# Part 2
# create a variable score to keep track of the scores
score = 0

# print out the header of Part 2
print("PART 2 - D20 Dice Game\n\n")

# use the for loop to play the game for 10 times
for time in range(1, 11, 1):
    # randomly assign a case number from 1 to 5 for the play
    # this will be updated for each play
    caseNum = random.randrange(5)+1

    # generate a random number from 1 to 20 for the rolled number
    # this will be updated for each play
    rolledNum = random.randrange(20) + 1

    # create a variable checking if rolled number is in winning numbers
    # this will be updated for each play
    winOrNot = False

    # print out the message about what case is playing
    print("You are playing for CASE", str(caseNum))

    # print out the valid winning number for the case is playing
    print("You will win for the following numbers:")

    # use for loop for printing winning numbers for each case
    if caseNum == 1:
        # for loop printing winning numbers for case 1
        for winNum in range(2, 21, 2):
            # check if rolled number is in winning numbers
            if rolledNum == winNum:
                winOrNot = True
            print(str(winNum) + " ", end="")
        # outside the for loop
    elif caseNum == 2:
        # for loop printing winning numbers for case 2
        for winNum in range(1, 21, 2):
            # check if rolled number is in winning numbers
            if rolledNum == winNum:
                winOrNot = True
            print(str(winNum) + " ", end="")
        # outside the for loop
    elif caseNum == 3:
        # for loop printing winning numbers for case 3
        for winNum in range(5, 11, 1):
            # check if rolled number is in winning numbers
            if rolledNum == winNum:
                winOrNot = True
            print(str(winNum) + " ", end="")
        # outside the for loop
    elif caseNum == 4:
        # for loop printing winning numbers for case 4
        for winNum in range(10, 21, 2):
            # check if rolled number is in winning numbers
            if rolledNum == winNum:
                winOrNot = True
            print(str(winNum) + " ", end="")
        # outside the for loop
    else:
        # for loop printing winning numbers for case 5
        for winNum in range(3, 20, 3):
            # check if rolled number is in winning numbers
            if rolledNum == winNum:
                winOrNot = True
            print(str(winNum) + " ", end="")
        # outside the for loop

    # print out the message for rolled number
    print("\n\n\nNow rolling ...")
    print("You rolled a", str(rolledNum) + "!")

    # print out message whether the user wins the play
    if winOrNot:
        print("You won 50 points! :)\n\n")
        score = score + 50
    else:
        print("You didn't win :(\n\n")
# outside the outer for loop (singly play finishes)

# print out the score and the ending message
print("Your total score is:", str(score))
print("Thanks for playing!")
