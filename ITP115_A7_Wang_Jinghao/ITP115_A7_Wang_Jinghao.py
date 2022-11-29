# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 7
# Description:
# Use functions to simulate rock-paper-scissors game

# import module
import random

# function definitions

# function: displayMenu()
# parameter: None
# return: None
# side effect: display the game rules to the player
def displayMenu():
    # print out the welcoming message
    print("Welcome! Let's play rock, paper, scissors.")
    # print out the game rules
    print("The rules of the game are:")
    print("   Rock smashes scissors")
    print("   Scissors cut paper")
    print("   Paper covers rock")
    print("   If both the choices are the same, it's a tie")

# function: getComputerChoice()
# parameter: None
# return: random integer from 0(included) to 2(included)
# side effect: print out message about the choice
def getComputerChoice():
    # get random integer from 0 to 2 (both included) to represent the computer's choice
    computerChoice = random.randrange(3)
    # print out the message about what the computer chose
    if computerChoice == 0:
        print("The computer chose Rock.")
    elif computerChoice == 1:
        print("The computer chose Paper.")
    else:
        print("The computer chose Scissors.")
    # return the output
    return computerChoice

# function: getPlayerChoice()
# parameter: None
# return: integer to represent the choice from the player
# side effect: print out message about the choice
def getPlayerChoice():
    # get random integer from 0 to 2 (both included) to represent the player's choice
    playerChoice = int(input("Please choose (0) for rock, (1) for paper or (2) for scissors\n"))
    # print out the message about what the player chose
    if playerChoice == 0:
        print("You chose Rock.")
    elif playerChoice == 1:
        print("You chose Paper.")
    else:
        print("You chose Scissors.")
    # return the output
    return playerChoice

# function: playRound(computerChoice, playerChoice)
# parameter 1: integer representing the computer's choice(0, 1 or 2)
# parameter 2: integer representing the player's choice(0, 1 or 2)
# return: integer to represent the outcome of the game(-1 if computer wins, 1 if player wins, 0 if a tie)
# side effect: print out the game message and who wins
def playRound(computerChoice, playerChoice):
    # set the result to be 0
    result = 0
    # when there is not a tie
    if computerChoice != playerChoice:
        # if the computer chose rock(0)
        if computerChoice == 0:
            # if the player chose paper(1), the player won
            if playerChoice == 1:
                result = 1
                print("Paper covers rock. Player wins!")
            # else (the player chose scissors(2)), the computer won
            else:
                result = -1
                print("Rock smashes scissors. Computer wins!")
        # if the computer chose paper(1)
        elif computerChoice == 1:
            # if the player chose rock(0), the computer won
            if playerChoice == 0:
                result = -1
                print("Paper covers rock. Computer wins!")
            # else (the player chose scissors(2)), the player won
            else:
                result = 1
                print("Scissors cut paper. Player wins!")
        # if the computer chose scissors(2)
        else:
            # if player chose rock(0), the player won
            if playerChoice == 0:
                result = 1
                print("Rock smashes scissors. Player wins!")
            # else (the player chose paper(1)), the computer won
            else:
                result = -1
                print("Scissors cut paper. Computer wins!")
    else:
        print("Both the choices are the same, it's a tie!")
    # return the output
    return result

# function: continueGame()
# parameter: None
# return: boolean, true if player wants to continue, else return false
# side effect: None
def continueGame():
    # get player input y or n to decide if they want to continue the game
    playerAnswer = input("Do you want to continue playing (y or n)? ")
    # set the value of continueOrNot is False
    continueOrNot = False
    # if the player inputs y or Y, then change the value of continueOrNot to True
    if playerAnswer.lower() == "y":
        continueOrNot = True
    # return the output
    return continueOrNot

# define main() function
def main():
    # create three counters to count how many times in total that
    # the computer won, the player won, and there is a tie
    computerWonCounter = 0
    playerWonCounter = 0
    tieCounter = 0

    # create an variable to keep track if the player wants to continue the game
    continueOrNot = True

    # use while loop to keep asking the player if they wants to continue the game
    while continueOrNot:
        # call displayMenu() function to display the menu
        displayMenu()
        # call getPlayerChoice() to get the player's choice
        playerChoice = getPlayerChoice()
        # call getComputerChoice() to get the computer's choice
        computerChoice = getComputerChoice()
        # call playRound(computerChoice, playerChoice) to get the integer representing the game result
        result = playRound(computerChoice, playerChoice)
        # increment the counter correspondingly
        if result == 0:
            tieCounter += 1
        elif result == 1:
            playerWonCounter += 1
        else:
            computerWonCounter += 1
        # update continueOrNot by asking the player if they want to continue the game
        # call continueGame() to update the continueOrNot
        continueOrNot = continueGame()
        # print an empty line
        print()
    # outside the while loop
    # display the final results of all the games the player played
    print("You won", playerWonCounter, "game(s).")
    print("The computer won", computerWonCounter, "game(s).")
    print("You tied with the computer", tieCounter, "game(s).")

    # print out ending message
    print("Thanks for playing!")

# call main() function
main()
