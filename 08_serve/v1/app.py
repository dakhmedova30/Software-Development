'''
ADJ In The House! :: Joseph Wu, Anna Fang, Diana Akhmedova
SoftDev
K08 -- Putting it Together
2022-10-07
time spent: 0.5 hours
'''

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    return "No hablo queso!"

app.run()

# This will display "No hablo queso" on the web page,
# but will not print "__main__" in the terminal.