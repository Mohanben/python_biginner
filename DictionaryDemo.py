# Dictionary for the Python#

phoneBook = {
    "Mohan": 323243434,
    "Ben": 4354354355,
    "Chandrasekar": 398987676
}

for name, number in phoneBook.items():
    print(name)
    print(number)

# Remove the Value from the index#

del phoneBook["Ben"]

print(phoneBook)


if "Chandrasekar" in phoneBook:
    print("Chandrasekar is in the list")
