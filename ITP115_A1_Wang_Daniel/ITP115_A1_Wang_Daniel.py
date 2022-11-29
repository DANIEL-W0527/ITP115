# Daniel Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 1
# Description:
# This Program creates a Mad Libs story.
# It asks for inputs from the users.
# It incorporates them into pre-written stories.

# get users' input
animals = input("Enter an animal that you like the most (plural): ")
verb = input("Enter a verb: ")
verbWithIng = input("Enter a verb ending in 'ing': ")
adj1 = input("Enter an positive adjective to describe a human: ")
adj2 = input("Enter a positive adjective to describe the mood: ")
num1 = int(input("Enter an integer greater than 10: "))
num2 = int(input("Enter a positive integer less than 5: "))
num3 = int(input("Enter a positive integer less than 10: "))
numWithDecimal = float(input("Enter a positive number with decimal: "))

# calculate number used in the story
product = num1 * num2
total = product - num3

# create the message to print out
msg1 = "You have always been dreaming about having " + "\"" + animals + "\""
msg1 += " as your pets because you are really " + "\"" + adj1 + "\"."
msg2 = "\"" + str(num2) + "\"" + " magical " + "\"" + animals + "\""
msg2 += " heard your wish and after " + "\"" + verbWithIng + "\""
msg2 += " for " + "\"" + str(numWithDecimal) + "\"" + " hours, they decide to give you a surprise."
msg3 = "Each of them bring " + "\"" + str(num1) + "\"" + " gifts for you, they wish you can enjoy these "
msg3 += "\"" + str(product) + "\"" + " gifts."
msg4 = "But one of them is really careless that lost " + "\"" + str(num3) + "\""
msg4 += " gifts so they only have " + "\"" + str(total) + "\"" + " gifts for you."
msg5 = "When you saw all those gifts, you are very " + "\"" + adj2 + "\""
msg5 += " that you want to " + "\"" + verb + "\"."

# Incorporate those words in the pre-written story and print out the message
print()
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
