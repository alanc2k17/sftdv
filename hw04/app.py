#default flask app for funzies
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def display_login():
    print '\n\n\n'
    print '=== DIAGNOSTICS === this Flask object'
    print app
    print '=== DIAGNOSTICS === request object'
    print request
    print '=== DIAGNOSTICS === request.headers'
    print request.headers
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def display_auth():
    #====== DIAGNOSTIC PRINT STATEMENTS ======
    print '\n\n\n'
    print '=== DIAGNOSTICS === request object'
    print request
    #print '=== DIAGNOSTICS === request.args'
    #print request.args
    #print '=== DIAGNOSTICS === request.args[username]'
    #print request.args['username']
    print '=== DIAGNOSTICS === request.form'
    print request.form
    print '=== DIAGNOSTICS === request.form[username]'
    print request.form['username']
    print '=== DIAGNOSTICS === request.headers'
    print request.headers
    #====== DIAGNOSTIC PRINT STATEMENTS ======
    user = 'spngbeb'
    password = 'sqrpnts'

    #check for correct user/pass
    if request.form['username'] == user and request.form['password'] == password:
        return render_template('landing.html', result='hello friend')
    else:
        return render_template('landing.html', result='nice try friend')

if __name__ == '__main__':
    app.debug = True
    app.run()
