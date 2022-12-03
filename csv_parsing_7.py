"""Calculate number of words and letters from previous Homeworks 5/6 output test file.
Create two csv:
1.word-count (all words are preprocessed in lowercase)
2.letter, cout_all, count_uppercase, percentage (add header, spacecharacters are not included)
CSVs should be recreated each time new record added.
"""
import csv
import re


def read_file():
    with open("feed.txt", "r") as file:
        content = file.read()
    return content


def extract_words(text):
    pattern = re.compile('[A-z]+')
    words = re.findall(pattern, text.lower())
    return words


def word_counter(list_of_words):
    word_count_list = list()
    for word in list_of_words:
        word_count = list_of_words.count(word)
        if word not in word_count_list:
            word_count_list.append(word)
            word_count_list.append(word_count)
    grouped_list = list(zip(word_count_list[0::2], word_count_list[1::2]))
    return grouped_list


def csv_writer_1(data):
    with open("csv_file_1.csv", "w") as feed_file:
        word_writer = csv.writer(feed_file, delimiter=',', quotechar='^', quoting=csv.QUOTE_ALL)
        for element in data:
            print(element)
            word_writer.writerow(element)



if __name__ == '__main__':
    file_content = read_file()
    print(file_content)
    print(extract_words(file_content))
    words = extract_words(file_content)
    print(words)
    count = word_counter(words)
    print(count)
    csv_writer_1(count)