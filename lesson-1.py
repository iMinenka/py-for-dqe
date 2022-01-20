# HOMEWORK - Create python script

from random import randint

# 1) create list of 100 random numbers from 0 to 1000
numListRand = []
for i in range(100):
    num = randint(0, 1000)
    numListRand.append(num)

# 2) sort list from min to max (without using sort())

# Option_1 with sort()
# numList.sort(reverse=True)

# Option_2 with sorted()
# numListRev = sorted(numList, reverse=True)

# Option 3 with index [::-1]
# numListRev = numList[::-1]

# 3) calculate average for even and odd numbers
# 4) print both average result in console

