# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word = word.lower()
    word = sorted(word)
    anagram = anagram.lower()
    anagram = sorted(anagram)

    if anagram == word:
        return True
    else:
        return False


msg = "This program checks if the two words are ANAGRAM"
print(msg)
print("First Word>>> ")
firstWord = input()
print("Second Word>>> ")
secondWord = input()
print(find_anagram(firstWord, secondWord))
