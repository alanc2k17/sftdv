#Alan Chen
#SoftDev1 pd8
#HW03 -- ...and Now Enjoy Its Contents
#2016-09-24

import random
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
    parse('occupations.csv', 'r')
    return render_template("basic.html", temp="Occupations!",
                           heading="Occupations!", inputdata=dictionary,
                           chosen=random_occupation(dictionary))

#===============================================================
# parse(filename, mode)
# takes filename.csv and converts data into dictionary
def parse(filename, mode):
    #format data for processing
    f = open(filename, mode) #create new file object
    contents = f.read().split("\n") #parse plaintext by \n
    print contents
    for pair in contents: #parse contents into dictionary
        print pair
        if pair != "": #account for empty strings
            if pair[0] == '"': #if pair contains quotes
                dictionary[pair.split('"')[1]] = float(pair.split('"')[2].split(',')[1])
            else:
                if isNumber(pair.split(',')[1]):
                    dictionary[pair.split(',')[0]] = float(pair.split(',')[1])
                '''else: DON'T INCLUDE "JOB CLASS, PERCENTAGE" PAIR BECUZ
                         IT JUST BREAKS THINGS >:(
                    dictionary[pair.split(',')[0]] = pair.split(',')[1]'''
    print dictionary

def random_occupation(data):
    tot = 0
    rand = random.random() * 99.8 #pick random number btwn 0 and 99.8
 
    for key in dictionary: #iterate through occupations
        tot += dictionary[key] #add percentage to tot
        if tot >= rand: #return key if tot >= rand
            return key
        
    
# isNumber(n)
# checks if string n can be converted into a float
def isNumber(n):
    try:
        float(n)
        return True #returns true if string can be a float
    except ValueError:
        return False #false otherwise
    
if __name__ == "__main__":
    app.debug = True #
    app.run()
