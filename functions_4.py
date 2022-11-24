from random import randint, sample

# Homework 1 from Lesson 3

example = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces."""


# make all text lowercase
def to_lower(text):
    return text.lower()


lwr = to_lower(example)


# split by tab and capitalize
def tab_dot_capitalizer(text):
    tabs = text.split("\t")
    capitalized = list()
    for tab in tabs:
        # tabs.insert(tabs.index(tab), ". ".join([s.capitalize() for s in tab.split(". ")]))
        # tabs.pop(tabs.index(tab))
        capitalized.append(". ".join([s.capitalize() for s in tab.split(". ")]))
    return "\t".join(capitalized)


capitals = tab_dot_capitalizer(lwr)


# generate new sentence from last words
def extra_sentence(text):
    extra = []
    for p in text.split("\t")[1:]:
        extra.append(p.split()[-1].rstrip("."))
    return " ".join(extra)


newSentence = extra_sentence(capitals)


# add extra sentence to the text at specified position
def add_extra_sentence(text, extra, position=2):
    sentences = text.split(".")
    sentences[position] = sentences[position] + ". " + extra
    # text.insert(position, sentence)
    return ".".join(sentences)


textWithExtra = add_extra_sentence(capitals, newSentence)


# replace mistake "iz" by "is"
def iz_replacer(text):
    return text.replace(" iz ", " is ")


replacedIz = iz_replacer(textWithExtra)
print(replacedIz)


# count whitespaces in text
def whitespace_counter(text):
    import re
    return len(re.findall(r"\s", text))


print("I got", whitespace_counter(textWithExtra))

# Homework 2 from Lesson 2
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


# create a list of letters
def alphabet_letters():
    import string
    return list(string.ascii_lowercase)


abc = alphabet_letters()


# create a list of dictionaries
def dic_list_generator(list_size, dic_size):
    dics = []
    for i in range(list_size):
        keys = [k for k in sample(abc, dic_size)]  # random letters
        values = [v for v in sample(range(100), dic_size)]
        dic = dict(zip(keys, values))
        dics.append(dic)
    return dics


dictNumber = randint(2, 10)  # number of dics in list
dictSize = randint(1, len(abc) - 1)  # dic length
print(f"Number of dicts: {dictNumber}. Dict size: {dictSize}")

dictionaries = dic_list_generator(dictNumber, dictSize)
print(dictionaries)


# create a common dictionary from a list of dictionaries with highest value of key
def combine_dictionaries(diclist):
    commonDict = dict()  # create empty common dict
    for dic in diclist:  # for every dict in list of dicts
        dicIndex = diclist.index(dic) + 1  # number of current dictionary
        for k, v in dic.items():  # for key:value pair in a current dict
            existKey = [i for i in commonDict.keys() if i.startswith(k)]  # all keys starting with key
            if existKey and k in existKey:  # if commonDict not empty and has same letter key
                if commonDict[k] >= v:  # if value of existing key less than current key value
                    commonDict.update(
                        {k + "_" + str((diclist.index([dic for dic in diclist if k in dic.keys()][0])) + 1):
                             commonDict[k]})  # add new key:value common dict, key with prefix
                    commonDict.pop(k)  # remove existing key:value
                else:  # commonDict[k] < v:  # if value of existing key less than current key value
                    commonDict.update({k + "_" + str(dicIndex): v})  # add new key:value common dict, key with prefix
                    commonDict.pop(k)  # remove existing key:value
            elif existKey and k in existKey[0]:  # if commonDict not empty and has same letter key
                if commonDict[existKey[0]] < v:  # if value of existing key less than current key value
                    commonDict.pop(existKey[0])  # remove existing key:value
                    commonDict.update({k + "_" + str(dicIndex): v})  # add new key:value common dict, key with prefix
            else:  # if key does not exist in common dict
                commonDict[k] = v  # add new key:value
    return dict(sorted(commonDict.items()))  # sort common dictionary


commonDic = combine_dictionaries(dictionaries)
print(commonDic)
