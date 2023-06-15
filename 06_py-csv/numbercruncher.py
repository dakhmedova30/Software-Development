'''
The Gooblers: Kevin Liu, Russell Goychayev, Diana Akhmedova
SoftDev
K06 -- StI/O: Divine your Destiny!
2022-10-01
time spent: 1.0 hour

QCC:
    -   Is there a more efficent way of testing the random devo and if the algo works?
    -   Is there another way to create a weighted random selector?

DISCO:
    -   One way of truncating a float requires you to turn it to a string first and then substringing it
    -   dict.pop() removes the last element
    -   dict.pop(index) removes the element of that index
    -   str.rsplit(delimiter, maximum) goes backwards and split the string on the delimiter maximum times

OPS SUMMARY:
    1.  Read the occupations.csv file and store it as a string
    2.  Split the string with the delimiter '\n'
    3.  Remove the insignifcant elements of the list
    4.  Initialize three dictionaries, one for storing the values and two for testing
    5.  For the rest of the elements in the list, reverse split them once with the delimiter ','
    6.  Using the list we got from rsplit, initialize all dictionaries with the key of list[0](occupations)
    7.  Store list[1] (percentage) as the value of one of the dictionaries (dict1)
    8.  Initalize the other two dictionaries with one(dict2) with the value of [percentage, 0] and the other(total): 0
    9:  Take the percentage of dict1 and multiplying it by 10, then store the key percentage*10 times in a list
    10. Using random.choice, pick a element from the list at random

    TESTING ALGO:
    1. Run for random.choice 1000 times, for each time a key appears, increment dict2[key][1] by 1
    2. Then take the percent error of the number of times a key appears compare to its percentage
    3. Store that percent in total
    4. Reset dict2 and perform steps 1-3 for a total of 1000 times
    5. For every element in total, divide it by 1000
    The values in total should be the total percent error of each key(the closer it is to 0, the more accurate)
'''

import random

a = open("occupations.csv")
b = a.read()

dict = {}
dict2 = {}
total = {}
txt = b.split("\n")
txt.pop() # remove last element: " "
txt.pop() # remove last element: "'Total': '99.8'"
txt.pop(0) # remove first element: "'Job Class': 'Percentage'"

for x in txt:
    list = x.rsplit(",", 1)
    dict[list[0]]= float(list[1])
    a = int(float(list[1]) * 10)
    # print(a)
    dict2[list[0]] = [a, 0]
    total[list[0]] = 0
list = []
for x in dict:
    for y in range(0, int(dict[x]*10)):
        list.append(x)

random_occupation = random.choice(list)
random_percentage = dict[random_occupation]
print("RANDOM OCCUPATION: " + random_occupation + "\nPERCENTAGE OF US WORKFORCE: " + str(random_percentage))

# testing if our random actual works with weighted
for y in range(0, 1000):
    for x in range(0, 1000):
        key = random.choice(list)
        dict2[key][1] = dict2[key][1] + 1
    for x in dict2:
        total[x] += ((float(dict2[x][0]) - float(dict2[x][1]))/float(dict2[x][0])) * 100
        dict2[x][1] = 0
    # print(dict2)

for z in total:
    total[z] = (str(abs(total[z]/1000)))[:4]
print("\nPERCENT ERROR: ")
print(total)

'''
to test the weighted averages

dict2 same key as dict
[key] = 0
1000 times
[key] = value + 1
'''
