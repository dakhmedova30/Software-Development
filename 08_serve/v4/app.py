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
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

# prints out the name, which is "__main__" and since it is not imported,
# the debugger is active and the program will run