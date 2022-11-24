"""
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

# list of alphabet letters for keys
ABC = list(string.ascii_lowercase)
# random size of one dict (limited by alphabet length, duplicates excluded
dictSize = randint(1, len(ABC) - 1)
# empty list for lists of tuples (key, value)
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

dicts = [dict(i) for i in dictsRaw]  # transform List of lists with Tuples into List of dicts

# print dictionaries
print("List of {} dictionaries of size {}:".format(len(dicts), dictSize), dicts, sep="\n")
for i in dicts:
    print("Dictionary_{}:".format(dicts.index(i) + 1), dict(sorted(i.items())))

# 2) get previously generated list of dicts and create one common dict:

commonDict = dict()  # create empty common dict

for dic in dicts:  # for every dict in list of dicts
    dicIndex = dicts.index(dic) + 1  # number of current dictionary
    for k, v in dic.items():  # for key:value pair in a current dict
        existKey = [i for i in commonDict.keys() if i.startswith(k)]  # all keys starting with key
        if existKey and k in existKey:  # if commonDict not empty and has same letter key
            if commonDict[k] >= v:  # if value of existing key less than current key value
                commonDict.update({k + "_" + str((dicts.index([dic for dic in dicts if k in dic.keys()][0])) + 1): commonDict[k]})  # add new key:value common dict, key with prefix
                commonDict.pop(k)  # remove existing key:value
            else: # commonDict[k] < v:  # if value of existing key less than current key value
                commonDict.update({k + "_" + str(dicIndex): v})  # add new key:value common dict, key with prefix
                commonDict.pop(k)  # remove existing key:value
        elif existKey and k in existKey[0]:  # if commonDict not empty and has same letter key
            if commonDict[existKey[0]] < v:  # if value of existing key less than current key value
                commonDict.pop(existKey[0])  # remove existing key:value
                commonDict.update({k + "_" + str(dicIndex): v})  # add new key:value common dict, key with prefix
        else:  # if key does not exist in common dict
            commonDict[k] = v  # add new key:value
dictionary = dict(sorted(commonDict.items()))  # sort common dictionary

print("Common dictionary:", dictionary, sep="\n")

