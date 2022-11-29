# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 9
# Description:
# Read a CSV file and translate the word to certain language based on user's choice
# Write the translated word in an output file until the user is done

# define functions

# function: getLanguages
# parameter: fileName, a string containing the name of a CSV file to read from
# parameter 1 fileName with default value of "languages.csv"
# return: a list of strings representing the languages in the header row
def getLanguages(fileName="languages.csv"):
    # create a file object fileIn to read the file
    fileIn = open(fileName,"r")
    # read the first line (header)
    line = fileIn.readline()
    # close the file
    fileIn.close()
    # get rid of whitespace in the line
    line = line.strip()
    # create a list by splitting the header line with ","
    langList = line.split(",")
    # return the required variable langList
    return langList

# function: getSecondLanguage
# parameter: langList, a list of the languages
# return: a string for the second language
# side effect 1: display to the user the languages that are available for translation
# side effect 2: get input from the user for the second language
# user must enter in a valid language, not case sensitive
def getSecondLanguage(langList):
    # print out the header for the program
    print("Language Translator")
    # print out the header message for languages available for translation
    print("Translate English words to one of the following languages:")
    # create a integer variable counter to count how many languages in the langList printed
    # initialize the variable counter with 0
    counter = 1
    # format the printing of languages available for translation
    print("    ", end=" ")
    # print out the first half languages available for translation
    while (counter < len(langList) / 2):
        print(langList[counter], end=" ")
        counter += 1
    # format the printing of languages available for translation
    print("\n    ", end=" ")
    # print out the rest of languages available for translation
    while (counter < len(langList)):
        print(langList[counter], end=" ")
        counter += 1

    # get input from the user for the second language
    langStr = input("\nEnter a language: ").lower()
    # keep asking for user's input until a valid language
    while langStr.capitalize() not in langList:
        print("This program does not support", langStr.capitalize())
        langStr = input("Enter a language: ").lower()
    # return the required variable lang.capitalize
    return langStr.capitalize()

# function: readFile
# parameter 1: langList, a list of the languages
# parameter 2: langStr, a string of containing the name of a language
# parameter 2 langStr with default value of "English"
# parameter 3: fileName, a string containing the name of a CSV file to read from
# parameter 3 fileName with default value of "languages.csv"
# return: a list of words in the language identified by the langStr parameter
def readFile(langList, langStr="English", fileName="languages.csv"):
    # create a file object fileIn to read the file
    # open the CSV file
    fileIn = open(fileName, "r")
    # read the header row to skip it
    fileIn.readline()
    # create a integer variable index and initialize it with value of the index of langStr in langList
    index = langList.index(langStr)
    # create a string list of words in the language of langStr
    secondList = []
    # loop through the rest of the file to create a list of words
    for line in fileIn:
        # get rid of whitespace in the line
        line = line.strip()
        # create a list by splitting the line with ","
        wordList = line.split(",")
        # append the word into secondList
        secondList.append(wordList[index])
    # close the file
    fileIn.close()
    # return the required variable secondList
    return secondList

# function: createResultsFile
# parameter 1: language, a string containing the name of the second language
# parameter 2: resultsFile is a string containing the name of the results file
# return: none
def createResultsFile(language, resultsFile):
    # create a file object fileOut to write to the file named resultsFile
    fileOut = open(resultsFile, "w")
    # write text to the file stating the second language
    print("Words translated from English " + "to " + language, file=fileOut)
    # close the file
    fileOut.close()

# function: translateWords
# parameter 1: englishList, a list of words in English
# parameter 2: secondList, a list of words in the second language
# parameter 3: resultsFile, a string containing the name of the text file
# return: none
def translateWords(englishList, secondList, resultsFile):
    # open the results file
    fileAppend = open(resultsFile, "a")
    # create a string variable continueOrNot to store if user want to continue translating another word
    # initialize the variable continueOrNot with the value of "y"
    continueOrNot = "y"
    # while loop keep asking the user if they want to translate another word until they answer "n" (case insensitive)
    while continueOrNot != "n":
        # get input from the user for the English word to translate
        englishWord = input("\nEnter a word to translate: ")
        # if englishWord.lower() is not in the englishList, display a message to the user
        if englishWord.lower() not in englishList:
            print(englishWord.lower(), "is not in the English list.")
        # if englishWord.lower() is in the englishList, display a message to the user
        # append the word and its translation to the fileAppend
        else:
            # create a integer variable index and initialize it with value of the index of englishWord in englishList
            index = englishList.index(englishWord.lower())
            # create a string variable translatedWord and initialize it with value of corresponding word in secondList
            translatedWord = secondList[index]
            # if there is the translation for the englishWord.lower()
            if translatedWord != "-" :
                # display a message to the user
                print(englishWord.lower(), "is translated to", translatedWord)
                # append the word and its translation to the fileAppend
                print(englishWord.lower() + " = " + secondList[index], file=fileAppend)
            # if there is no translation for the englishWord.lower(), display a message to the user
            else:
                print(englishWord.lower(), "did not have a translation.")
        # update the value of continueOrNot by asking user
        continueOrNot = input("Another word (y or n)? ").lower()
        # check if the user inputs a valid choice
        # if the user's input is invalid, ask again
        while continueOrNot != "n" and continueOrNot != "y":
            continueOrNot = input("Another word (y or n)? ").lower()
    # print out the ending message for the program
    print("\nTranslated words have been saved to " + resultsFile)
    # close the file
    fileAppend.close()

# function: main
# parameter: none
# return: none
# side effect: call the functions and finish the program
def main():
    # call function getLanguages to get the list of languages
    langList = getLanguages()
    # call function readFile to read the CSV file for the English words
    englishList = readFile(langList)
    # call function getSecondLanguage to get the second language
    langStr = getSecondLanguage(langList)
    # call function readFile to read the CSV file for that language
    secondList = readFile(langList, langStr)
    # ask the user to enter a name for the results file
    resultsFile = input("\nEnter a name for the results file (return key for " + langStr + ".txt): ")
    # use the second language with ".txt" as a default file name
    if resultsFile == "":
        resultsFile = langStr + ".txt"
    # call function createto write a message to the results file
    createResultsFile(langStr, resultsFile)
    # call function translateWords to allow user to enter word
    # translate those words and save to the text file
    translateWords(englishList, secondList, resultsFile)

# call function main
main()