# ADJ In The House!
* Joseph Wu
* Anna Fang
* Diana Akhmedova

<br>

# DISCO:
- Everytime the user saves new changes, the debugger will activate and refresh the program.
- @app.route("/") routes the return of hello_world() onto a web page.
- "/" stands for the root of the directory.
- print() will print "\__main__" in the terminal.
- Return will display on the web page.
- run() runs the program.
- \n does not work in Flask, we have to use <\br> instead to create a new line.
- We have to have a main function, which is the first function underneath @app.route(), that will contain all other necessary funtions.
- The local variables cannot be underneath @app.route().

<br>

# QCC:
- What exactly is \__name__? What is \__main__?
- Why can we not have multiple functions returning at the same time?
- Why is Flask a combination of Python and HTML?

<br>

# OPS SUMMARY:

## RANDOM OCCUPATION GENERATOR:
1.  Read the occupations.csv file and store it as a string
2.  Split the string with the delimiter '\n'
3.  Remove the insignifcant elements of the list
4.  Initialize three dictionaries, one for storing the values and two for testing
5.  For the rest of the elements in the list, reverse split them once with the delimiter ','
6.  Using the list we got from rsplit, initialize all dictionaries with the key of list[0] (occupations)
7.  Store list[1] (percentage) as the value of one of the dictionaries (dict1)
8.  Initalize the other two dictionaries with one(dict2) with the value of [percentage, 0] and the other(total): 0
9.  Take the percentage of dict1 and multiplying it by 10, then store the key percentage*10 times in a list
10. Using random.choice, pick a element from the list at random

## RETURNING OUTPUT IN FLASK:
1.  We made sure to import random and Flask, as well as place the local variables above @app.route().
2.  Then we created a main function called output() that holds and returns our other functions with new lines as formatting. This includes:
3.  The roster() function that returns our TNPG and Roster.
4.  The random_occupation() funtion that includes our random occupation generator code and returns the random occupation + its percentage of the workforce.
5.  The list_occupations() funtion that returns a list of our occupation dictionary's keys.
6.  We made sure to include a debug that will refresh anytime we save changes on this file.