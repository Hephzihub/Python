# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import re

def read_file_content(filename):

    # Reading the text file
    text_file = open(filename)
    # Reads the string
    text_data = text_file.read()
    #Coverts all uppercase to lowercase
    text_data = text_data.lower()

    # Remove punctuations using RegEX
    text_data = re.sub(r'[^\w\s]', '', text_data)
    
    # Returns the text without double spaces and new line
    return text_data.replace("  \n", " ")

def count_words():
    #The read_file_content() is invoked with a parameters and the returned value is saved
    text = read_file_content("./story.txt")

    #The string is coverted into a list
    text_list = text.split(" ")

    # A new list is created
    text_new_list = []
    
    #This control flow puts the strings in old list to new list with reoccurrence
    for i in text_list:

        #Checks if word already exist
        if i not in text_new_list:
            
            #adds word
            text_new_list.append(i)
    for i in range(0, len(text_new_list)):

        print("\"" + text_new_list[i] + "\"" + ':', text_list.count(text_new_list[i]))

    # return {"as": 10, "would": 20}

count_words()
