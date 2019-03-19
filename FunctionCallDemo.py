#Function Call Demo#

def getValue():
    return 11

def generateCarSpeed(carSpeed, engineRPM):
    return carSpeed + engineRPM

def getStaionList(programName,progamId):
    print("Station List is Empty")

value = getValue()

print(value)

vehicleSpeed = generateCarSpeed(11,222)

print(vehicleSpeed)

getStaionList("","")