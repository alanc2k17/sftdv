#Alan Chen
#SoftDev1 pd8
#HW03 -- ...and Now Enjoy Its Contents
#2016-09-24

import random, util.occu_picker
from flask import Flask, render_template

app = Flask(__name__)
dictionary = dict() #create an empty dictionary

@app.route("/")
def hello_world():
    return "buenos dias world"

@app.route("/my_first_template")
def test_template():
    return render_template("basic.html", temp="XP")

@app.route("/occupations")
def occupations_template():
    return render_template("basic.html", temp="Occupations!",
                           heading="Occupations!",
                           inputdata=util.occu_picker.parse('occupations.csv', 'r'),
                           chosen=util.occu_picker.random_occupation(dictionary))
    
if __name__ == "__main__":
    app.debug = True #
    app.run()
