numberOfCoins = int(input("How many different values of coins should there be? "))
number = int("9" + "01" * numberOfCoins)
endpoint= int("902" + "00" * (numberOfCoins - 1))
numberList = []
coinsNeeded = 0
coinsLeft = 0 #used to store value for calculations
bestCoinsNeeded = 100000
bestNumberList = []

def calculator(maxRange, multiplesOf, insertBoolean):
    global number
    global numberList
    global coinsNeeded
    global bestCoinsNeeded
    global bestNumberList

    if numberOfCoins > 3:
        print("This process could take up to several minutes.")

    while number < endpoint:
        for n in range(numberOfCoins):
            numberList.append(int(str(number)[2 * n + 1] + str(number)[2 * n + 2]))
        for value in range(numberOfCoins):
            if numberList[value] == 0:
                numberList[value] = 1 #prevents divide by zero errors

        for x in range(1, maxRange):
            for num in range(numberOfCoins):
                if num == 0:
                    coinsNeeded += (x // numberList[-1])
                    coinsLeft = x - (x // numberList[-1]) * numberList[-1]
                else:
                    coinsNeeded += (coinsLeft // numberList[-1 * (num + 1)]) #iterates through list in reverse
                    coinsLeft = coinsLeft - (coinsLeft // numberList[-1 * (num + 1)]) * numberList[-1 * (num + 1)]
        if coinsNeeded < bestCoinsNeeded:
            bestCoinsNeeded = coinsNeeded
            for bestNum in range(numberOfCoins):
                numberList[bestNum] *= multiplesOf
                bestNumberList = numberList
            if insertBoolean == True:
                bestNumberList.insert(0, 1)
        coinsNeeded = 0
        numberList = []
        number += 1
    if insertBoolean == False:
        print("Best coin values: " + str(bestNumberList) + " Average coins per transaction: " + str(bestCoinsNeeded / maxRange))

def customInputCalculator(numberList):
    global coinsNeeded
    for x in range(1, 99):
        for num in range(numberOfCoins):
            if num == 0:
                coinsNeeded += (x // numberList[-1])
                coinsLeft = x - (x // numberList[-1]) * numberList[-1]
            else:
                coinsNeeded += (coinsLeft // numberList[-1 * (num + 1)]) #iterates through list in reverse
                coinsLeft = coinsLeft - (coinsLeft // numberList[-1 * (num + 1)]) * numberList[-1 * (num + 1)]
    print("Coin values: " + str(numberList) + " Average coins per transaction: " + str(coinsNeeded / 99))

def main():
    selection = input("""
Select one of the following options: 
[1] Allow any coin value
[2] Only allow multiples of 5
[3] Only allow 1 and multiples of 5
[4] Evaluate user-inputted values

""")

    print("Calculating...")

    if selection == "1":
        calculator(99, 1, False)

    if selection == "2":
        calculator(19, 5, False)

    if selection == "3":
        global numberOfCoins 
        numberOfCoins -= 1
        calculator(19, 5, True)
        numberOfCoins += 1
        customInputCalculator(bestNumberList)

    if selection == "4":
        numberListString = input("Enter coin values separated by commas: ")
        numberList = numberListString.split(",")
        for stringNum in range(numberOfCoins):
            numberList[stringNum] = int(numberList[stringNum])
        numberList.sort()
        customInputCalculator(numberList)

main()