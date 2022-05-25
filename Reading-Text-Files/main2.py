# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
from collections import Counter
import re

def read_file_content(filename):

    # Reading the text file
    with open(filename, "r") as f:

        return f.read()

def count_words():
    text = read_file_content("./story.txt")

    # [assignment] Add your code here
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)

    
    return Counter(text.split())

print(count_words())