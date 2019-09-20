from flask import Flask, request
from flask import render_template
from tinydb import TinyDB, Query
import json


db = TinyDB('db.json')
User = Query()

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    user_data = db.search(User.name == name)[0]
    print(user_data)
    return render_template('home.html', user_data=user_data)

@app.route('/add_user')
def add_user():
    new_name = request.args.get('name')
    age = request.args.get('age')
    city = request.args.get('city')
    db.insert({'name':new_name, 'age':age, 'city':city})
    return 'Name have been updated.'

@app.route('/show_users')
def show_users():
    all_users = db.all()

    return render_template('user_details.html', all_users=all_users)

if __name__ == '__main__':
    app.run(debug = True)