example = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces."""


def to_lower(text):
    return text.lower()


lwr = to_lower(example)


def tab_dot_capitalizer(text):
    tabs = text.split("\t")
    capitalized = list()
    for tab in tabs:
        # tabs.insert(tabs.index(tab), ". ".join([s.capitalize() for s in tab.split(". ")]))
        # tabs.pop(tabs.index(tab))
        capitalized.append(". ".join([s.capitalize() for s in tab.split(". ")]))
    return "\t".join(capitalized)


capitals = tab_dot_capitalizer(lwr)


def extra_sentence(text):
    extra = []
    for p in text.split("\t")[1:]:
        extra.append(p.split()[-1].rstrip("."))
    return " ".join(extra)


newSentence = extra_sentence(capitals)


def add_extra_sentence(text, extra, position=2):
    sentences = text.split(".")
    sentences[position] = sentences[position] + ". " + extra
    # text.insert(position, sentence)
    return ".".join(sentences)


textWithExtra = add_extra_sentence(capitals, newSentence)


def iz_replacer(text):
    return text.replace(" iz ", " is ")


replacedIz = iz_replacer(textWithExtra)
print(replacedIz)


def whitespace_counter(text):
    import re
    return len(re.findall(r"\s", text))


print("I got", whitespace_counter(textWithExtra))
