text = """homEwork:
	tHis iz your homeWork, copy these Text to variable. 

	You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

	it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE. 

	last iz TO calculate nuMber OF Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces."""

# Split text by tab and Capitalize after tab
textByTab = [i.capitalize() for i in text.lower().split("\t")]
#print("textByTab is", textByTab)

# Capitalise sentence starting after dot
textByDot = "\t".join(textByTab).split(".")  # join textByTab and split it by dot

for i in textByDot:     # every sentence in text
    for e in i:     #  every symbol in sentence
        if e[0].isalpha():      # symbol is letter
            cpt = i.replace(e, e.upper(), 1)        # replace first letter by Capital letter
            textByDot.insert(textByDot.index(i), cpt)       # insert sentence with Uppercase letter
            textByDot.pop(textByDot.index(i))       # remove sentence with Lowercase letter
            break
print("textByDot with capitalise", textByDot)

# create a sentence from last words
extraSent = ['']  # empty list for sentence from last words
for s in range(1, len(textByTab)):  # from every paragraph
    extraSent.append(textByTab[s].split()[-1].rstrip("."))  # take last word and add to extra sentence
# print("Extra sentence is:", extraSent)

# Add extra sentence to the paragraph
textByDot[3] = " ".join(extraSent) + textByDot[3]  # insert extra sentence into list textByDot
#print("textByDotWithExtra", textByDot)

textWithExtra = ".".join(textByDot)  # join text with extra sentence
# print("ExtraSent added\n", textWithExtra)

# Replace iz by is in text
textResultWithIs = textWithExtra.replace(" iz ", " is ")
print(textResultWithIs)

# Count of whitespaces in text
print("I got", sum((textResultWithIs.count(" "), textResultWithIs.count("\n"),
                    textResultWithIs.count("\t"))))
