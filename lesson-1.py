# HOMEWORK - Create python script

from random import randint

# create list of 100 random numbers from 0 to 1000
numListRand = []
for i in range(100):
    num = randint(0, 1000)
    numListRand.append(num)

# sort list from min to max (without using sort())
numList = []
numListRandTemp = numListRand.copy()

for i in range(len(numListRandTemp)):
    minNum = min(numListRandTemp)
    numList.append(minNum)
    numListRandTemp.remove(minNum)

# 3) calculate average for even and odd numbers
# TODO
# 4) print both average result in console
# TODO

