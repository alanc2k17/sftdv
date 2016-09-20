#Alan Chen
#SoftDev1 pd8
#HW02 -- Fill Your Flask
#2016-09-21
                                                           
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso"

@app.route("/memes")
def hello_memes():
    return '''<img src="http://memeshappen.com/media/created/IF-YOU-THINK-YOU39RE-ABLE-TO-STUDY-COMPUTER-SCIENCE-BECAUSE-YOU-SPEND-A-LOT-OF-TIME-ON-THE-COMPUTER-YOU39RE-GONNA-HAVE-A-BAD-TIME-meme-562.jpg" alt="if you think you're able to study computer science because you spend a lot of time on the computer, you're gonna have a bad time.">'''

@app.route("/funnest")
def hello_fun():
    return foo()


def foo():
    return "ya boi"

if __name__ == "__main__":
    app.run()

