'''
ADJ In The House! :: Joseph Wu, Anna Fang, Diana Akhmedova
SoftDev
K08 -- Putting it Together
2022-10-07
time spent: 0.5 hours
'''

from flask import Flask
app = Flask(__name__) # create instance of class Flask

@app.route("/")       # assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   # where will this go?
                      # it will print in the terminal
    return "No hablo queso!"

app.run()

