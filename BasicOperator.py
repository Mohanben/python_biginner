"Basic Operator Demo"

number = 1 + 2 * 3 / 11.0;

print(number)

# Reminder operator#

remainder = 10 % 2

print(remainder)

# Multiplication with power relatoinship#

multiplicaiton = 11 ** 2

print(multiplicaiton)

# Concadination with String #

helloworld = "Hello," + " " + "World.";

print(helloworld)

# List can be join the additional Operator#

mFirstList = [1, 2, 3, 4, 5]
mSecondList = [10, 11, 22, 33]
mThirdList = ["Mohan", "Ben", "Chandrasekar"]

mMergeList = mFirstList + mSecondList + mThirdList;

for mName in mMergeList:
    if (mName == "Mohan"):
        print("Yes got it")
    else:
        print("Nope")
    # print(mName)

print(mMergeList)

if "Mohan" in mMergeList:
    print("true !! Its there")
