from flask import Flask, request
import json
from tinydb import TinyDB, Query
import random

# https://tinydb.readthedocs.io/en/latest/getting-started.html#basic-usage

db = TinyDB('db.json')
app = Flask(__name__)

notes_list = []

@app.route('/')
def home():
    message = """
    <html>
        <body>
            <p> Go to <a href='/take_note'>/take_note</a></p>
            <p> Go to <a href='/show_notes'>/show_notes</a></p>
            <p> Go to <a href='/change_password'>/change_password</a></p>
        </body>
    </html>
    """
    return message

@app.route('/take_note')
def take_note():
    note_text = request.args.get("note_text")
    notes_list.append(note_text)
    db.insert({"id":random.randint(1,9999), "text":note_text})
    return "added your note"

@app.route('/show_notes')
def show_notes():
    notes_list = db.all()
    notes_json = json.dumps(notes_list)
    return notes_json


if __name__ == '__main__':
    app.run(debug=True)