# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 10
# Description:
# simulates animal daycare, using class to represent animals
# interact with the animals based on selected menu options

# create a class called Animal
class Animal(object):
    # attributes: hunger, happiness, health, energy, age, name, species
    # hunger: an integer representing the animal’s hunger meter
    # happiness: an integer representing the animal’s happiness meter
    # health: an integer representing the animal’s health meter
    # energy: an integer representing the animal’s energy meter
    # age: an integer representing the animal’s age
    # name: a string representing the animal’s name
    # species: a string representing the animal’s species

    # function: __init__
    # input: seven attributes mentioned above
    # return: none
    # side effect: set each of the animal’s attributes to the corresponding inputs
    def __init__(self, hungerParam, happinessParam, healthParam, energyParam, ageParam, nameParam, speciesParam):
        self.hunger = hungerParam
        self.happiness = happinessParam
        self.health = healthParam
        self.energy = energyParam
        self.age = ageParam
        self.name = nameParam
        self.species = speciesParam

    # function: play
    # input: none
    # return: none
    # side effect: increase the animal’s happiness by 10 and hunger by 5
    def play(self):
        # check if happiness meter will go over 100 or below 0 after increase of 10
        if self.happiness + 10 > 100:  # if it will exceed 100 after play
            self.happiness = 100  # assign happiness with value of 100
        elif self.happiness + 10 < 0:  # if it will go below 0 after play
            self.happiness = 0  # assign happiness with value of 0
        else:  # if it is in the range 0 - 100 after play
            self.happiness += 10  # increase happiness by 10

        # check if hunger meter will go over 100 or below 0 after increase of 5
        if self.hunger + 5 > 100:  # if it will exceed 100 after play
            self.hunger = 100  # assign hunger with value of 100
        elif self.hunger + 5 < 0:  # if it will go below 0 after play
            self.hunger = 0  # assign hunger with value of 0
        else:  # if it is in the range 0 - 100 after play
            self.hunger += 5  # increase hunger by 5

    # function: feed
    # input: none
    # return: none
    # side effect: decrease the animal’s hunger by 10
    def feed(self):
        # check if hunger meter will go over 100 or below 0 after decrease of 10
        if self.hunger - 10 > 100:  # if it will exceed 100 after feed
            self.hunger = 100  # assign hunger with value of 100
        elif self.hunger - 10 < 0:  # if it will go below 0 after feed
            self.hunger = 0  # assign hunger with value of 0
        else:  # if it is in the range 0 - 100 after feed
            self.hunger -= 10  # decrease hunger by 10

    # function: giveMedicine
    # input: none
    # return: none
    # side effect: decrease the animal’s happiness by 20, increase the animal's health by 20
    def giveMedicine(self):
        # check if happiness meter will go over 100 or below 0 after decrease of 20
        if self.happiness - 20 > 100:  # if it will exceed 100 after giveMedicine
            self.happiness = 100  # assign happiness with value of 100
        elif self.happiness - 20 < 0:  # if it will go below 0 after giveMedicine
            self.happiness = 0  # assign happiness with value of 0
        else:  # if it is in the range 0 - 100 after giveMedicine
            self.happiness -= 20  # increase happiness by 20

        # check if health meter will go over 100 or below 0 after increase of 20
        if self.health + 20 > 100:  # if it will exceed 100 after giveMedicine
            self.health = 100  # assign health with value of 100
        elif self.health + 20 < 0:  # if it will go below 0 after giveMedicine
            self.health = 0  # assign health with value of 0
        else:  # if it is in the range 0 - 100 after giveMedicine
            self.health += 20  # increase health by 20

    # function: sleep
    # input: none
    # return: none
    # side effect: increase the animal’s energy by 20 and age by 1
    def sleep(self):
        # check if energy meter will go over 100 or below 0 after increase of 20
        if self.energy + 20 > 100:  # if it will exceed 100 after sleep
            self.energy = 100  # assign energy with value of 100
        elif self.energy + 20 < 0:  # if it will go below 0 after sleep
            self.energy = 0  # assign energy with value of 0
        else:  # if it is in the range 0 - 100 after sleep
            self.energy += 20  # increase energy by 20

        # check if age meter will go below 0 after increase of 1
        if self.age + 1 < 0:  # if it will go below 0 after sleep
            self.age = 0  # assign age with value of 0
        else:  # if it is in the range 0 - 100 after sleep
            self.age += 1  # increase age by 1

    # function: __str__
    # input: none
    # return: a string containing well formatted message with all information about the animal
    def __str__(self):
        # combine the information of the animal and form the string
        msg = "Name: " + self.name + " the " + self.species + "\n"
        msg += "Health: " + str(self.health) + "\n"
        msg += "Happiness: " + str(self.happiness) + "\n"
        msg += "Hunger: " + str(self.hunger) + "\n"
        msg += "Energy: " + str(self.energy) + "\n"
        msg += "Age: " + str(self.age) + "\n"
        msg += "********************************"

        # return the string
        return msg


# function: loadAnimals
# input: fileName, a string representing the name of the csv file
# return: a list of Animal objects
# read CSV file to create Animal objects and store them in a list to be returned
def loadAnimals(fileName="animals.csv"):
    # create an empty list
    animalsList = []
    # open the file
    fileIn = open(fileName, "r")

    # read the fileIn
    for line in fileIn:
        # get rid of new line ("\n") for each line
        line = line.strip()
        # split the line into a list
        dataList = line.split(",")
        # create an animal object using dataList
        animalObj = Animal(int(dataList[0]), int(dataList[1]), int(dataList[2]), int(dataList[3]), int(dataList[4]), dataList[5], dataList[6])
        # append the Animal object to animalsList
        animalsList.append(animalObj)
    # outside the for loop

    # close the fileIn
    fileIn.close()
    # return the list required
    return animalsList

# function: displayMenu
# input: none
# return: none
# side effect: print out a menu with all possible options to the user
def displayMenu():
    print("1) Play")
    print("2) Feed")
    print("3) Give Medicine")
    print("4) Sleep")
    print("5) Print an Animal's stats")
    print("6) View All Animals")
    print("7) Exit\n")

# function: selectAnimal
# input: animalsList,  a list of Animals
# return: the selected animal from the list
# side effect: print out a menu with each animal’s name and species, ask user to select from the list
def selectAnimal(animalsList):
    # print out a menu with each animal’s name and species
    for num in range(len(animalsList)):
        print(str(num + 1) + ") " + animalsList[num].name + " the " + animalsList[num].species)
    # outside the for loop
    # print out an empty line
    print()
    # ask user to select an animal
    animalSelection = int(input("Please select an animal from the list (enter the 1-5): "))
    # keep asking user for selection until the userselection is valid
    while animalSelection < 1 or animalSelection > 5:
        # print out the error message
        print("Invalid input, please try again!\n")
        # ask for user's selection again and update userSelection
        animalSelection = int(input("Please select an animal from the list (enter the 1-5): "))
    # outside the while loop

    # return the animal from the list corresponding to the user's selection
    return animalsList[animalSelection - 1]

# EXTRA CREDIT
# function: saveResultInFile
# input: animalsList, the list of all Animal objects
# return: none
# side effect: save all the information in a new CSV file in the same format
def saveResultInFile(animalsList):
    # create a file object and open the file
    fileOut = open("animalsResults.csv", "w")
    # write information in file
    for itemObj in animalsList:
        print(str(itemObj.hunger) + "," + str(itemObj.happiness) + "," + str(itemObj.health) + "," + str(itemObj.energy) + "," + str(itemObj.age) + "," + itemObj.name + "," + itemObj.species, file=fileOut)
    # outside the for loop

    # close the file object
    fileOut.close()

# function: main
# input: none
# return: none
def main():
    # create a list of Animals object by calling the loadAnimals function
    animalsList = loadAnimals()
    # print out the opening message for the program
    print("Welcome to the Animal Daycare! Here is what we can do:\n")
    # display the menu first by calling the displayMenu function
    displayMenu()
    # ask for user's menu selection for the first time
    menuSelection = int(input("Please make a selection: "))
    # use while loop to keep asking user's input for menu selection until they input 7 (Exit)
    while menuSelection != 7:
        # while loop to keep asking for user's selection of menu until the selection is valid
        while menuSelection < 1 or menuSelection > 7:
            # print out the error message
            print("*Invalid selection, please try again.\n")
            # display the menu by calling the displayMenu function
            displayMenu()
            # update the menu selection from user
            menuSelection = int(input("Please make a selection: "))
        # outside the while loop

        # after getting a valid menuSelection, run corresponding function
        # if the menuSelection is between 1 to 5
        if menuSelection in range(1, 6, 1):
            # ask user to select an animal by calling the function selectAnimal
            animalSelected = selectAnimal(animalsList)
            # perform different behaviors based on different menuSelection
            # if the user choose option 1: Play
            if menuSelection == 1:
                # call the Animal object method play for animalSelected
                animalSelected.play()
                # print out the message
                print("You played with " + animalSelected.name + " the " + animalSelected.species + "!\n")
            # if the user choose option 2: Feed
            elif menuSelection == 2:
                # call the Animal object method feed for animalSelected
                animalSelected.feed()
                # print out the message
                print("You fed " + animalSelected.name + " the " + animalSelected.species + "!\n")
            # if the user choose option 3: Give Medicine
            elif menuSelection == 3:
                # call the Animal object method giveMedicine for animalSelected
                animalSelected.giveMedicine()
                # print out the message
                print("You gave " + animalSelected.name + " the " + animalSelected.species + " some medicine!\n")
            # if the user choose option 4: Sleep
            elif menuSelection == 4:
                # call the Animal object method sleep for animalSelected
                animalSelected.sleep()
                # print out the message
                print(animalSelected.name + " the " + animalSelected.species + " took a nap!\n")
            # if the user choose option 5: Print an Animal's stats
            else:
                # print the animal stats (print the Animal Object)
                print(animalSelected)
                # print out the empty line
                print()
            # outside the inner if-else statements
        # if the menuSelection is 6
        elif menuSelection == 6:
                # use for loop print all the animal stats
                # print each Animal object in the animalsList
                for itemObj in animalsList:
                    print(itemObj)
                # outside the for loop
                # print out the empty line
                print()
        # outside to the outer if-else statements
        # display the menu by calling the displayMenu function
        displayMenu()
        # update the menuSelection
        menuSelection = int(input("Please make a selection: "))
    # outside the for loop
    # print out the ending message
    print("Goodbye!")

    # EXTRA CREDIT
    # call the function saveResultInFile to save all the information into a CSV file
    saveResultInFile(animalsList)

# call function main
main()
