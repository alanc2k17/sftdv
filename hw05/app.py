#default flask app for funzies
from flask import Flask, render_template, request, redirect, url_for, session
import utils.manage, hashlib, os

app = Flask(__name__)
app.secret_key = os.urandom(32)

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
    hash_object0 = hashlib.sha1()
    hash_object0.update(request.form['password'])
    hashed_pass = hash_object0.hexdigest()

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
                session['usernname'] = request.form['username']
                return render_template('landing.html',
                                       result = 'successfully logged in!')
            return render_template('landing.html',
                                   result = 'incorrect password!')
        return render_template('landing.html',
                               result = 'this user is not registered!')
        
    return render_template('landing.html',
                           result = 'uh oh u broke my website! pls send help')

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
   return 'welcome home!'

@app.route('/logout')
def display_logout():
   #====== DIAGNOSTIC PRINT STATEMENTS ======
   print '\n\n\n'
   print '=== DIAGNOSTICS === request object'
   print request
   print '=== DIAGNOSTICS === request.form'
   print request.form
   print '=== DIAGNOSTICS === request.headers'
   print request.headers
   #====== DIAGNOSTIC PRINT STATEMENTS ======
   session.pop('user', None)
   return 'Logged out!'
def test():
    return utils.manage.get_users()

if __name__ == '__main__':
    app.debug = True
    app.run()
