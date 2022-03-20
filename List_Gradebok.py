#list manipulation and 2D list

last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
print(last_semester_gradebook )
#Result: [['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65]]
print()

#Single dimensional List(Strings)
subjects = ["physics", "calculus", "poetry", "history"]
print(subjects)
#Result: ['physics', 'calculus', 'poetry', 'history']
print()

#Single dimensional List(Integers)
grades = [98, 97, 85, 88]
print(grades)
#Result: [98, 97, 85, 88]
print()

#2D list with two data types
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
#Result: [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
print()

#Adding to a 2D list
gradebook.append(["computer science", 100])
print(gradebook)
#Result: [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['computer science', 100]]
print()

gradebook.append(["visual arts", 93])
print(gradebook)
#Result: [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['computer science', 100], ['visual arts', 93]]
print()

#Updating a 2D list
gradebook[-1][-1] = 98
print(gradebook)
#Result: [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88], ['computer science', 100], ['visual arts', 98]]
print()

#Deleting from a sublist in 2D list
gradebook[2].remove(85)
print(gradebook)
#Result: [['physics', 98], ['calculus', 97], ['poetry'], ['history', 88], ['computer science', 100], ['visual arts', 98]]
print()

#Adding to a sublist
gradebook[2].append("Pass")
print(gradebook)
#Result: [['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['computer science', 100], ['visual arts', 98]]
print()

#Combining List
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
#Result: [['politics', 80], ['latin', 96], ['dance', 97], ['architecture', 65], ['physics', 98], ['calculus', 97], ['poetry', 'Pass'], ['history', 88], ['computer science', 100], ['visual arts', 98]]
