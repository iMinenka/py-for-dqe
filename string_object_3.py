some_text_1 = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces."""

import re


def normalize_text(text):
    # Split text by tab and capitalize after tab
    text_capitalized_after_tab = [i.capitalize() for i in text.lower().split("\t")]
    # Capitalise sentence starting after dot
    text_capitalized_after_dot = "\t".join(text_capitalized_after_tab).split(".")  # join textByTab and split it by dot
    text_capitalized = list()
    for sentence in text_capitalized_after_dot:  # every sentence in text
        for word in sentence:  # every symbol in sentence
            if word[0].isalpha():  # symbol is letter
                capitalized_sentence = sentence.replace(word, word.upper(), 1)  # replace first letter by Capital letter
                text_capitalized.append(capitalized_sentence)  # insert sentence with Uppercase letter
                break
            else:
                text_capitalized.append(sentence)
                break
    text_normalized = ".".join(text_capitalized) # + '.'
    return text_normalized


def replace_iz_by_is(text):
    # Replace iz by is in text
    text_with_replacement = text.replace(" iz ", " is ")
    # print(text_with_replacement)
    return text_with_replacement


def create_extra_sentence(text):
    # create a sentence from last words
    extra_sentence_to_add = list()  # empty list for sentence from last words
    for sentence in text.split("."):  # from every sentence of the text
        if sentence:
            last_word = sentence.split()[-1]
            extra_sentence_to_add.append(last_word)
    extra_sentence_normalized = " ".join(extra_sentence_to_add).capitalize()
    return extra_sentence_normalized


def add_extra_sentence(sentence, text):
    # Add extra sentence to the paragraph
    text_list = text.split('.')
    text_list.insert(3, " " + sentence)
    text_with_sentence = ".".join(text_list)
    return text_with_sentence


def count_whitespaces(text):
    # Count of whitespaces in text
    spaces_count = len(re.findall(r"\s", text))
    return spaces_count


if __name__ == '__main__':
    some_text = "asd asd"
    normalized_text = normalize_text(some_text)
    extra_sentence = create_extra_sentence(normalized_text)
    text_with_extra_sentence = add_extra_sentence(extra_sentence, normalized_text)
    iz_corrected_text = replace_iz_by_is(text_with_extra_sentence)
    print(iz_corrected_text)
    print("I got", count_whitespaces(normalized_text))
