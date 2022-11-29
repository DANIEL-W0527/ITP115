# Jinghao (Daniel) Wang, jinghao@usc.edu
# ITP 115, Spring 2020
# Assignment 2
# Description:
# This program creates a harry potter vending machine.
# It determines change and gives a discount.

# initialize variable
butterbeerPrice = 58
quillPrice = 10
prophetPrice = 7
bookPrice = 400
creaturePrice = 900
itemPrice = 0
itemName = ""
discount = 0
galleonToKnut = 493
sickleToKnut = 29
numGalleonsPaid = 0
numSicklesPaid = 0
numKnutsPaid = 0
totalPaid = 0
totalChange = 0
changeInGalleon = 0
changeInSickles = 0
changeInKnuts = 0


# ask for the item selection from customer
print("Please select an item from the vending machine:")
print("      a) Butterbeer: 58 knuts")
print("      b) Quill: 10 knuts")
print("      c) The Daily Prophet: 7 knuts")
print("      d) Book of Spells: 400 knuts")
print("      e) Magical Creature: 900 knuts")
selection = input("> ")
if selection.lower() == "a":
    itemPrice = butterbeerPrice
    itemName = "Butterbeer"
elif selection.lower() == "b":
    itemPrice = quillPrice
    itemName = "Quill"
elif selection.lower() == "c":
    itemPrice = prophetPrice
    itemName = "The Daily Prophet"
elif selection.lower() == "d":
    itemPrice = bookPrice
    itemName = "Book of Spells"
elif selection.lower() == "e":
    itemPrice = creaturePrice
    itemName = "Magical Creature"
else:
    print("You have entered an invalid option.", end=" ")
    print("You will be given a Butterbeer for 58 knuts.")
    itemPrice = butterbeerPrice
    itemName = "Butterbeer"

# ask if user would like to share on Instagram
# customers will get 5 knuts discount if they will share on Instagram
shareOnIns = input("Will you share this on Instagram? (y/n): ")
if shareOnIns.lower() == "y":
    discount = 5
    print("Thanks! You get 5 knuts off your purchase")
elif shareOnIns.lower() != "n":
    print("You have entered an invalid option. No coupon will be used")

# the space between two parts
print()

# ask how much customers paid in galleons, sickles and knuts
print("Please tell me how much you paid in each coins.")
numGalleonsPaid = input("How many galleons you paid: ")
numSicklesPaid = input("How many sickles you paid: ")
numKnutsPaid = input("How many knuts you paid: ")

# calculate how much customers paid in knuts
totalPaid = int(numGalleonsPaid) * galleonToKnut
totalPaid = totalPaid + int(numSicklesPaid) * sickleToKnut
totalPaid = totalPaid + int(numKnutsPaid)
totalChange = totalPaid - (itemPrice - discount)

# calculate how much is the change in knuts
if totalChange // galleonToKnut != 0:
    changeInGalleon = totalChange // galleonToKnut
    changeInKnuts = totalChange % galleonToKnut
else:
    changeInKnuts = totalChange
if changeInKnuts // sickleToKnut != 0:
    changeInSickles = changeInKnuts // sickleToKnut
    changeInKnuts = changeInKnuts % sickleToKnut

# the space between the user input and the rest
print()

# inform customers their choice and how much they paid
print("You bought a " + itemName + " for " + str(itemPrice) + " knuts ", end="")
print("(with coupon of " + str(discount), "knuts) and paid with ", end="")
print(numGalleonsPaid, "galleons", end=", ")
print(numSicklesPaid, "sickles and", numKnutsPaid, "knuts.")

# inform customers how much is their change in knuts and sickles
print("Here is your change (" + str(totalChange) + " knuts):")
print("Galleons:", changeInGalleon)
print("Sickles:", changeInSickles)
print("Knuts:", changeInKnuts)


