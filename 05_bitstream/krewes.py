"""
Russel Goychayev, Diana Akhmedova, Kevin Liu
SoftDev
K05 -- The More You Know About Your Data, the More Efficiently You Can Work With It
2022-09-28
time spent: 0.5 hours

DISCO:
 - We learned how to access and read text file using open() and read().
 - We learned how to splice a String by using split(String).

QCC:
 - What is the time complexity of split()?

OPS SUMMARY:
 1. Read the krewes.txt file.
 2. Create a list called student_arr and splice krewes.txt by "@@@", which equals to the student_arr.
 3. Create a dictionary called studentsDict.
 4. Iterate throught student_arr and splice each student by "$$$", setting the result to a temp list.
 5. Using the index of temp, assign each element in the dictionary with the key of the Devo name and the value of the period and the ducky.
 6. Using random.choice() on a list, formed by the list() funcion, we were able to choose a random key.
 7. Using the random key, we were able to return the data associated with the key and printed out the Devo, their period, and their ducky as a String.
"""

import random

txt = open("krewes.txt")
text = txt.read()
# print(text)

student_arr = text.split("@@@")
# print(student_arr)

studentsDict = {}

for student in student_arr:
    temp = student.split("$$$")
    studentsDict[temp[1]] = [temp[0], temp[2]]
# print(studentsDict)

def chooseDevoWithChoice():
    randomStudent = random.choice(list(studentsDict))
    result = "Random Devo: " + randomStudent
    data = studentsDict[randomStudent]
    return str(result) + "\nPeriod: " + str(data[0]) + "\nDucky: " + str(data[1])

print(chooseDevoWithChoice())
