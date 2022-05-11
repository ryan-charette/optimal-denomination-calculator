numberOfCoins = int(input("How many different values of coins should there be? "))
number = int("9" + "01" * numberOfCoins)
endpoint= int("902" + "00" * (numberOfCoins - 1))
numberList = []
coinsNeeded = 0
coinsLeft = 0 #used to store value for calculations
bestCoinsNeeded = 100000
bestNumberList = []

while number < endpoint:
    for n in range(numberOfCoins):
        numberList.append(int(str(number)[2 * n + 1] + str(number)[2 * n + 2]))
    for value in range(numberOfCoins):
        if numberList[value] == 0:
            numberList[value] = 1 #prevents divide by zero errors

    for x in range(1, 99):
        for num in range(numberOfCoins):
            if num == 0:
                coinsNeeded += (x // numberList[-1])
                coinsLeft = x - (x // numberList[-1]) * numberList[-1]
            else:
                coinsNeeded += (coinsLeft // numberList[-1 * (num + 1)]) #iterates through list in reverse
                coinsLeft = coinsLeft - (coinsLeft // numberList[-1 * (num + 1)]) * numberList[-1 * (num + 1)]
    if coinsNeeded < bestCoinsNeeded:
        bestCoinsNeeded = coinsNeeded
        bestNumberList = numberList
        print("Best coin values so far: " + str(bestNumberList) + " Average coins per transaction: " + str(bestCoinsNeeded / 99))
    coinsNeeded = 0
    numberList = []
    number += 1
print("COMPLETE")
