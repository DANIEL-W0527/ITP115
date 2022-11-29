# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 8
# Description:
# Create a two player tic tac toe game

# import module
import TicTacToeHelper
import random

# function: isValidMove
# parameter 1: a list representing the board
# parameter 2: an integer corresponding to the index position that a user would like to place their letter on
# return: a boolean value, True if the spot is open or False if the spot is taken or out of range
def isValidMove(boardList, spot):
    # create and initialize the variable validMove as False
    validMove = False
    # only when the spot is in the range of boardList (0 to len(boardList) - 1, both included)
    # and the element corresponding to that spot is not "o" or "x" (the spot is open)
    # then assign validMove to have True value
    # when the spot is in the range of boardList (0 to len(boardList) - 1, both included)
    if spot in range(len(boardList)):
        # the element corresponding to that spot is not "o" or "x" (the spot is open)
        if boardList[spot] != "o" and boardList[spot] != "x":
            validMove = True
    # return the value
    return validMove

# function: updateBoard
# parameter 1: a list representing the board
# parameter 2: an integer corresponding to the index position that a user would like to place their letter on
# parameter 3: a string representing the user’s letter (“x” or “o”)
# return: none
# side effect: place the player’s letter in the specified spot on the board(into boardList)
def updateBoard(boardList, spot, playerLetter):
    # place the player’s letter in the specified spot on the board(into boardList)
    boardList[spot] = playerLetter

# function: playGame
# parameter: none
# return: none
def playGame():
    # initialize the list representing the board to a list of strings with the numbers 0-8
    boardList = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    # keep track of the total number of moves that have been made using a counter
    counter = 0

    # create a list variable playersList to store two players
    playersList = ["x", "o"]

    # create a int variable to represent the index of the current player
    # and initialize it as 0
    playerIndex = 0

    # ask the player if the player wants to play with computer
    playWithComputer = input("Do you want to play against computer? (y/n): ").lower()

    # while loop to get player's correct input until they entered "Y" or "y" or "N" or "n"
    while playWithComputer != "y" and playWithComputer != "n":
            # print out error message
            print("Invalid Option! Please enter Y(y) or N(n)")
            # get the player's input, update the variable playWithComputer
            playWithComputer = input("Do you want to play against computer? (y/n): ").lower()
    # outside the while loop, get user's correct output

    # ask the player which player the player choose to start the game
    # if the user choose to play against the computer, print out the corresponding message
    if playWithComputer == "y":
        playerToStart = input("Do you want which player to start the game? (x for You / o for Computer): ").lower()
    # if the user choose not to play against the computer, print out the corresponding message
    else:
        playerToStart = input("Do you want which player to start the game? (x for Player x / o for Player o): ").lower()

    # while loop to get user correct input until they entered "O" or "o" or "X" or "x"
    while playerToStart != "o" and playerToStart != "x":
        # print out error message
        print("Invalid Option! Please enter O(o) or X(x)")
        # get the player's input, update the variable playerToStart
        if playWithComputer == "y":
            playerToStart = input(
                "Do you want which player to start the game? (x for Player x / o for Computer): ").lower()
        # if the user choose not to play against the computer, print out the corresponding message
        else:
            playerToStart = input(
                "Do you want which player to start the game? (x for Player x / o for Player o): ").lower()
    # outside the while loop, get user's correct output
    # set the initial value for playerIndex
    if playerToStart == "o":
        playerIndex = 1

    # if the player wants to play against computer
    if playWithComputer == "y":
        # while loop to allow each player to take a turn until the game ends
        while TicTacToeHelper.checkForWinner(boardList, counter) == 'n':
            # print out the board
            TicTacToeHelper.printPrettyBoard(boardList)
            # ask the player to select a spot
            msg = playersList[playerIndex] + ", pick a spot: "
            # for the computer, generate the random number as the move
            if playerIndex == 1:
                spot = random.randrange(len(boardList))
                print(msg + str(spot))
            # for the player, ask for the player's input
            else:
                spot = int(input(msg))

            # check if it is a valid move
            # keep asking for a valid move if it is not a valid move
            while not isValidMove(boardList, spot):
                # print out invalid move messages
                print("Invalid move, please try again.")
                # ask for another input from user for the move, update variable spot
                # for the computer, generate the random number as the move
                if playerIndex == 1:
                    spot = random.randrange(len(boardList))
                    print(msg + str(spot))
                # for the player, ask for the player's input
                else:
                    spot = int(input(msg))
            # after getting a valid move
            # update the counter by incrementing it by one
            counter += 1
            # update the board
            updateBoard(boardList, spot, playersList[playerIndex])
            # update the player, take turn for players
            # if the player is "x" now then change to player "o"
            if playerIndex == 0:
                playerIndex = 1
            # if the player is "o" now then change to player "x"
            else:
                playerIndex = 0
    # if the player does not want to play against with the computer
    else:
        # while loop to allow each player to take a turn until the game ends
        while TicTacToeHelper.checkForWinner(boardList, counter) == 'n':
            # print out the board
            TicTacToeHelper.printPrettyBoard(boardList)
            # ask the player to select a spot
            msg = "Player " + playersList[playerIndex] + ", pick a spot: "
            spot = int(input(msg))
            # check if it is a valid move
            # keep asking for a valid move if it is not a valid move
            while not isValidMove(boardList, spot):
                # print out invalid move messages
                print("Invalid move, please try again.")
                # ask for another input from user for the move, update variable spot
                spot = int(input(msg))
            # after getting a valid move
            # update the counter by incrementing it by one
            counter += 1
            # update the board
            updateBoard(boardList, spot, playersList[playerIndex])
            # update the player, take turn for players
            # if the player is "x" now then change to player "o"
            if playerIndex == 0:
                playerIndex = 1
            # if the player is "o" now then change to player "x"
            else:
                playerIndex = 0
    # outside of the while loop (the game ends)
    # print out the final board
    TicTacToeHelper.printPrettyBoard(boardList)
    # print out the ending message for the game
    print("\nGame Over!")
    # print out the winner message
    # if player x is the winner
    if TicTacToeHelper.checkForWinner(boardList, counter) == 'x':
        # print different message depending on if the player play against computer
        # if the player plays against the computer
        if playWithComputer == "y":
            print("You are the winner!")
        # if the player plays against another player
        else:
            print("Player x is the winner!")
    # if the player o is the winner
    elif TicTacToeHelper.checkForWinner(boardList, counter) == 'o':
        # print different message depending on if the player play against computer
        # if the player plays against the computer
        if playWithComputer == "y":
            print("Computer is the winner!")
        # if the player plays against another player
        else:
            print("Player o is the winner!")
    # if there is a stalemate
    else:
        print("Stalemate reached!")

def main():
    # print out the welcoming message for the game
    print("Welcome to Tic Tac Toe!")
    # create a variable anotherRound to indicate if the player wants to play another round
    # initialize the variable anotherRound as "y"
    anotherRound = "y"
    # while loop to allow user keep playing a new round until they decide to stop
    while anotherRound == "y":
        # play the game for one round
        playGame()
        # asking if the player wants to play a new round (update the variable anotherRound)
        anotherRound = input("Would you like to play another round? (y/n): ").lower()
        # keep asking for inputs if the player enters something other than "Y", "y", "N", "n"
        while anotherRound != "y" and anotherRound != "n":
            # print out error message
            print("Invalid Option! Please enter Y(y) or N(n)")
            anotherRound = input("Would you like to play another round? (y/n): ").lower()
    # outside the while loop
    # print out the ending message
    print("Goodbye!")

# call main()
main()