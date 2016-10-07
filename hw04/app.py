#default flask app for funzies
from flask import Flask, render_template, request, redirect, url_for
import utils.manage, hashlib

app = Flask(__name__)

@app.route('/')
def display_login():
    #====== DIAGNOSTIC PRINT STATEMENTS ======
    print '\n\n\n'
    print '=== DIAGNOSTICS === this Flask object'
    print app
    print '=== DIAGNOSTICS === request object'
    print request
    print '=== DIAGNOSTICS === request.headers'
    print request.headers
    #====== DIAGNOSTIC PRINT STATEMENTS ======

    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def display_auth():
    #====== DIAGNOSTIC PRINT STATEMENTS ======
    print '\n\n\n'
    print '=== DIAGNOSTICS === request object'
    print request
    print '=== DIAGNOSTICS === request.form'
    print request.form
    print '=== DIAGNOSTICS === request.headers'
    print request.headers
    #====== DIAGNOSTIC PRINT STATEMENTS ======
    ish = hashlib.sha1()
    ish.update(request.form['password'])
    hashed_pass = ish.hexdigest()

    if request.form['sub1'] == 'Register':
        if request.form['username'] in utils.manage.get_users():
            return render_template('landing.html',
                                   result = 'this username is already registered!')
        else:
            utils.manage.add_user(request.form['username'],
                                  hashed_pass)
            return render_template('landing.html',
                                   result = 'you have successfully registered!')
    else:
        if request.form['username'] in utils.manage.get_users():
            if utils.manage.get_users()[request.form['username']] == hashed_pass:
                return render_template('landing.html',
                                       result = 'successfully logged in!')
            return render_template('landing.html',
                                   result = 'incorrect password!')
        return render_template('landing.html',
                               result = 'u broke it!!! >:(')
        
    return "welcome to /auth! either something went kaboom or ur a hacker! >:("

@app.route('/register', methods=['POST'])
def display_register():
    #====== DIAGNOSTIC PRINT STATEMENTS ======
   print '\n\n\n'
   print '=== DIAGNOSTICS === request object'
   print request
   print '=== DIAGNOSTICS === request.form'
   print request.form
   print '=== DIAGNOSTICS === request.headers'
   print request.headers
   #====== DIAGNOSTIC PRINT STATEMENTS ======
   return render_template('register.html')

@app.route('/home')
def display_home():
   #====== DIAGNOSTIC PRINT STATEMENTS ======
   print '\n\n\n'
   print '=== DIAGNOSTICS === request object'
   print request
   print '=== DIAGNOSTICS === request.form'
   print request.form
   print '=== DIAGNOSTICS === request.headers'
   print request.headers
   #====== DIAGNOSTIC PRINT STATEMENTS ======
   return "welcome home!"

def test():
    return utils.manage.get_users()

if __name__ == '__main__':
    app.debug = True
    app.run()
