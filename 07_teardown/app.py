'''
Scuba Doo Divers: David Chen, Diana Akhmedova, Sam Cowan
SoftDev
K07 -- Learnination Via Deconstruction
2022-10-03
time spent: 0.3 hours

DISCO:
- Using "print()" will display the information in the console.
- Using "return" will display the information on the localhost server.

QCC:
0. JavaScript.
1. "/" means the base path.
2. This will print to the console.
3. __main__
4. This will appear on a locally hosted server and will only appear if you are in the Flask session.
   If you click on the link in the console after "Running on __", but will say "Unable to connect" if you press CTRL+C in the console and exit the session.
5. JavaScript.

INVESTIGATIVE APPROACH:
- Our trio ran the code and clicked on the link in the console, which led to the localhost server.
- We discovered that if you type in CTRL+C or exit the session, we will be no longer connected to the server.
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?
