# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 5
# Description:
# Part 1: Word Jumble Game
# print out the jumbled version of pre-input word
# keep asking for user's guesses until they are right given hint if needed
# count attempts tried, and output the scores earned at the end

# import module
import random

# create the wordList to store pre-designed words
wordList = ["dog", "whale", "giraffe", "elephant", "python"]

# randomly generate a index number in the list
# use this variable to determine which word used in the program
wordIndex = random.randrange(len(wordList))

# create a list named jumbledList to store jumbled words (same order)
jumbledList = []

# for loop to jumble each word in the wordList
# store jumbled words into jumbledList (same order)
for item in range(len(wordList)):
    # convert the word in wordList into a list called tempList
    tempList = list(wordList[item])
    # create a list tempJumbledList to store jumbled tempList
    tempJumbledList = []

    # while loop to jumble the word until the tempList is empty
    while not len(tempList) == 0:
        # choose random item in tempList into tempJumbledList
        index = random.randrange(len(tempList))
        tempJumbledList.append(tempList[index])
        # remove that random item from tempList
        del tempList[index]
        # repeat doing this to jumble the word until tempList is empty
    # out of while loop

    # convert tempJumbledList into a string variable
    jumbledWord = "".join(tempJumbledList)
    # add jumbledWord into the jumbledList (same order)
    jumbledList.append(jumbledWord)
# out of for loop

# create a list named hintMsgList to store all the hint messages (same order)
hintMsgList = ["Human's best friend!", "The biggest mammal in world!"]
hintMsgList += ["The animal with long neck!", "The animal with long nose!"]
hintMsgList += ["The programming language you are learning!"]

# output the message, tell the user jumbled word to guess
print("The jumbled word is \"" + jumbledList[wordIndex] + "\"")

# Print out the game rule
print("\nYou will get 10 points off each guess after first guess.")
print("You will get 10 points off each time you asked for hints.")
print("You will get 10 points if you did not ask for hints until you get right answer.\n")

# prompt for user's input, store it into variable guess
guess = input("Please enter your guess: ")

# create variable to count attempts tried, times hints asked and the total score
attempCounter = 1
hintCounter = 0
totalScore = 100

# while loop to keep asking for guess until it is right
while not guess == wordList[wordIndex]:
    # out put the message to try again
    print("Try again.")
    # ask if the user needs hint
    hint = input("Would you like the hint (y/n): ")

    # if user needs hint, print out corresponding hints
    if hint.lower() == "y":
        print(hintMsgList[wordIndex])
        # if hint being used, hintCounter counts once
        hintCounter += 1
    # out of if-else statement

    # keep asking for guess and update variableguess
    guess = input("\nPlease enter your guess: ")

    # attemptCounter counts once ask for input again
    attempCounter += 1

# print out the message of ending game
print("\nYou got it!")
# summarize how many attempts used
print("It took you", attempCounter, "tries.")

# each attempt will deduct 10 point except for the first attempt
# each hint used will deduct 10 point
# calculate the total score
totalScore = totalScore - (attempCounter - 1) * 10 - (hintCounter * 10)

# reward for not using hint until get correct answer: add 30 points
if hintCounter == 0 and attempCounter > 1:
    totalScore += 30

# print out the total scores earned
print("You got", totalScore, "scores in total!")


# Part 2: Encrypt / Decrypt
# encrypt the message user inputs by shift each letter by a fixed number user inputs

# create variable to store all the alphabet letters
original = "abcdefghijklmnopqrstuvwxyz"
# convert the original into a list called originalList
originalList = list(original)
# create a variable called cipherList to store cipher alphabet letters
cipherList = []

# ask for the message to encrypt from user
originalMsg = input("\nEnter a message: ")

# ask for the shift value to be used from user
shiftValue = int(input("Enter a number to shift by (0-25): "))

# assign cipherList by shifting originalList by shiftValue number
cipherList += originalList[shiftValue:len(originalList)]
cipherList += originalList[0:shiftValue]

# create a variable called encryptedMsg to store the encrypted message
encryptedMsg = ""

# use for loop to find the encryptedMsg
for item in originalMsg:
    # if the character of the originalMsg could be found in originalList
    # then convert the letter to corresponding cipher alphabet
    # the corresponding cipher alphabet and original alphabet have the same index
    if item in originalList:
        # find the index
        index = originalList.index(item)
        # add the character to encryptedMsg
        encryptedMsg += cipherList[index]
    # if the character of the originalMsg could not be found in originalList
    # then add that character into encryptedMsg
    else:
        encryptedMsg += item
    # end of if-else statement
# out of for loop

# print out the encrypting message and the encryptedMsg
print("Encrypting message....")
print("     Encrypted message:", encryptedMsg)

# create a variable called decryptedMsg to store the decrypted message
decryptedMsg = ""

# use for loop to find the decryptedMsg
for item in encryptedMsg:
    # if the character of the encryptedMsg could be found in cipherList
    # then convert the letter to corresponding original alphabet
    # the corresponding cipher alphabet and original alphabet have the same index
    if item in cipherList:
        index = cipherList.index(item)
        decryptedMsg += originalList[index]
    # if the character of the encryptedMsg could not be found in cipherList
    # then add that character into decryptedMsg
    else:
        decryptedMsg += item
    # end of if-else statement
# out of for loop

# print out the decrypting message and the decryptedMsg
print("Decrypting message....")
print("     Decrypted message:", decryptedMsg)

# print out the original message
print("     Original message:", originalMsg)
