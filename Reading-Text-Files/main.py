# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
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

    text_list = text.split(" ")

    text_new_list = []

    for i in text_list:

        if i not in text_new_list:
            
            text_new_list.append(i)
    for i in range(0, len(text_new_list)):

        print("\"" + text_new_list[i] + "\"" + ':', text_list.count(text_new_list[i]))

    # return {"as": 10, "would": 20}

count_words()
