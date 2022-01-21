# HOMEWORK - Create python script

from random import randint

# 1) create list of 100 random numbers from 0 to 1000

numListRand = []
for i in range(100):
    num = randint(0, 1000)
    numListRand.append(num)

# 2) sort list from min to max (without using sort())

numList = []
numListRandTemp = numListRand.copy()

# loop to find min number in numListRand, remove it and add to list numList
for i in range(len(numListRandTemp)):
    minNum = min(numListRandTemp)
    numList.append(minNum)
    numListRandTemp.remove(minNum)

# 3) calculate average for even and odd numbers

# Solution 1

# calculate sum and count of odd and even numbers
evenSum = 0
evenCount = 0
oddSum = 0
oddCount = 0

for i in numList:
    if i % 2 == 0:          # number is even
        evenSum += i
        evenCount += 1
    else:                   # number is odd
        oddSum += i
        oddCount += 1

# calculate average for odd and even lists
avgEven = evenSum / evenCount
avgOdd = oddSum / oddCount

# Solution 2

# create two lists with odd and even numbers with comprehension
evenList = [i for i in numList if i % 2 == 0]
oddList = [i for i in numList if i % 2 != 0]

# calculate average for odd and even lists
avgEvenList = sum(evenList) / len(evenList)
avgOddList = sum(oddList) / len(oddList)

# 4) print both average result in console
print("Solution 1:\n", "Avg even:", avgEven, "Avg odd:", avgOdd)
# or with format
print('Solution 2:\n Avg even: {} Avg odd: {}'.format(avgEvenList, avgOddList))
