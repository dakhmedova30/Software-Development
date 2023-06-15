# Diana Akhmedova
# SoftDev
# K20 -- A RESTful Journey Skyward
# 2022-11-22
# time spent: 0.5 hrs

# DISCO:
#  * readlines() returns a list that contains each line in the file as a separate list item.
#  * requests.get() allows you to make a request to a webpage; it sends a GET request to the url.
#  * json.loads() allows you to read a json file like a dictionary; parses a JSON string and converts it into a Python dictionary.

# QCC:
#  * Is there a way to read the fields of the JSON file?

# (Notes borrowed and added onto with permission from Jumping Seals (James Yu and Samantha Hua) due to absence.)


from flask import Flask, session, render_template, request, redirect
import requests
import json
app = Flask(__name__)


@app.route("/")
def get():
    with open('key_nasa.txt') as f:
        k = f.readlines() # nasa api key
    key = k[0] # changes the key from a list to a string
    data = requests.get(url=f"https://api.nasa.gov/planetary/apod?api_key={key}") # gets data from the website
    url = json.loads(data.text)["url"] # data.text turns data into a string, json.loads converts json string to dictionary
    explanation = json.loads(data.text)["explanation"] # explanation is the key in the json file
    return render_template("main.html", url=url, e=explanation)


if __name__ == "__main__":
    app.debug = True
    app.run()
