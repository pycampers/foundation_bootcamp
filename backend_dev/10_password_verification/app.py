from flask import Flask, render_template, request, redirect, url_for
import hashlib
from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()

app = Flask(__name__)


def make_md5_hash(user_entered_password):
    result = hashlib.md5(user_entered_password.encode()) 
    password_hash = result.hexdigest()
    return password_hash


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sign_up')
def sign_up():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    password = request.form.get('password')
    search_result = db.search(User.username == username)
    if len(search_result) != 0:
        return 'username already exists.'
    else:   
        password_hash = make_md5_hash(password)

        user_pass_dict = {'username':username, 'password':password_hash}
        db.insert(user_pass_dict)
        return redirect(url_for('login'))


@app.route('/check_login', methods=['POST'])
def check_login():
    username = request.form.get('username')
    password = request.form.get('password')
    search_result = db.search(User.username == username)
    if len(search_result) == 0:
        return 'incorrect username.'

    else:
        correct_password_hash = search_result[0]['password']
        user_entered_password_hash = make_md5_hash(password)

        if user_entered_password_hash == correct_password_hash:
            return f'Welcome {username}, you are logged in.'
        else:
            return 'Wrong password.'

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'GET':
        return render_template('change_password.html')
    else:
        username = request.form.get('username')
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')

        search_result = db.search(User.username == username)
        if len(search_result) == 0:
            return 'incorrect username.'
        else:
            old_password_hash = make_md5_hash(old_password)
            correct_password_hash = search_result[0]['password']
            if old_password_hash == correct_password_hash:
 
                result = db.update({
                    'password': make_md5_hash(new_password)}, 
                    User.username == username
                    )
                print(result)
                return 'Password Changed.'
            else:
                return 'wrong password.'
        

if __name__ == '__main__':
    app.run(debug=True)