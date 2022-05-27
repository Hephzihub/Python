# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from collections import Counter
from dataclasses import replace
import re

def read_file_content(filename):

    # Reading the text file
    text_file = open(filename)
    text_data = text_file.read()
    text_data = text_data.lower()

    # Remove punctuations using RegEX
    text_data = re.sub(r'[^\w\s]', '', text_data)

    return text_data.replace("  \n", " ")
    

def count_words():
    text = read_file_content("./story.txt")

    # [assignment] Add your code here
    text = text.split()
    # print(lin)

    di = dict()
    for w in text:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
    
    return di

print(count_words())
