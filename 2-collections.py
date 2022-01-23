""" Homework
1. create a list of random number of dicts (from 2 to 10)
- dict's random numbers of keys should be letter,
- dict's values should be a number (0-100),
-- example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
2. get previously generated list of dicts and create one common dict:
- if dicts have same key, we will take max value, and rename key with dict number with max value
- if key is only in one dict - take it as is,
- example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
"""
# 1) create a list of random number of dicts (from 2 to 10)

import string
from random import randint

# list of alphabet letters
ABC = list(string.ascii_lowercase)
# random size of one dict (limited by alphabet length, duplicates excluded
dictSize = randint(1, len(ABC) - 1)
# empty dictionary
dictsRaw = []

for i in range(randint(2, 10)):  # for every Dict (2 to 10)
    dictRaw = []  # List with tuples as pair (key, value)
    dictsRaw.append(dictRaw)  # add List to the List of Dicts
    abc = ABC.copy()  # to use ABC letters as keys
    # generate pair key-value
    for p in range(dictSize):
        n = randint(0, len(abc) - 1)  # random index of letter
        pair = (abc[n], randint(0, 100))  # generate pair key-value (random_letter, random_number_0-100)
        dictRaw.append(pair)  # add tuple to one Dict
        abc.pop(n)  # remove letter from abc to prevent duplicates

dicts = [dict(i) for i in dictsRaw]  # transform List of lists into List of dicts

print(dicts)

# 2) get previously generated list of dicts and create one common dict:

commonDict = dict()  # create empty common dict

for dic in dicts:  # for every dict in list of dicts
    for k, v in dic.items():  # for key:value pair in a single dict
        if k in commonDict:  # if key exists in a common dict
            if commonDict[k] < v:  # and key' values greater than in common dict
                commonDict.update({k: v})  # update common dict key with greater value
            else:
                continue
        else:  # if key does not exist in common dict
            commonDict[k] = v  # add new key:value

print(commonDict)
