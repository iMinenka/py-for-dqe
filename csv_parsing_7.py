"""Calculate number of words and letters from previous Homeworks 5/6 output test file.
Create two csv:
1.word-count (all words are preprocessed in lowercase)
2.letter, cout_all, count_uppercase, percentage (add header, spacecharacters are not included)
CSVs should be recreated each time new record added.
"""
import csv
import re
from string import ascii_lowercase


def read_file():
    with open('feed.txt', 'r') as file:
        file_content = file.read()
    return file_content


def extract_words(text):
    pattern = re.compile('[A-z]+')
    words_only = re.findall(pattern, text)
    return words_only


def count_words(list_of_words):
    words_to_lower = [word.lower() for word in list_of_words]
    word_count_list = list()
    for word in words_to_lower:
        word_count = words_to_lower.count(word)
        if word not in word_count_list:
            word_count_list.append(word)
            word_count_list.append(word_count)
    grouped_list = list(zip(word_count_list[0::2], word_count_list[1::2]))
    return grouped_list


def count_letters(list_of_words):
    text = list(''.join(list_of_words))
    alphabet = ascii_lowercase
    letter_count_summary = list()
    for letter in alphabet:
        if letter in text or letter.upper() in text:
            letter_stats = dict()
            letter_stats['letter'] = letter
            letter_stats['count_all'] = text.count(letter.lower()) + text.count(letter.upper())
            letter_stats['count_uppercase'] = text.count(letter.upper())
            letter_stats['percentage'] = round(letter_stats['count_all'] / len(text) * 100, 2)
            letter_count_summary.append(letter_stats)
    return letter_count_summary


def write_words_count_to_csv(words):
    with open('csv_file_1.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter='-', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for word in words:
            writer.writerow(word)


def write_letters_count_to_csv(letters):
    with open('csv_file_2.csv', 'w') as csv_file:
        fieldnames = ['letter', 'count_all', 'count_uppercase', 'percentage']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for letter in letters:
            writer.writerow(letter)


def main():
    text_from_file = read_file()
    words_from_text = extract_words(text_from_file)
    words_count = count_words(words_from_text)
    letters_count = count_letters(words_from_text)
    write_words_count_to_csv(words_count)
    write_letters_count_to_csv(letters_count)


if __name__ == '__main__':
    main()
