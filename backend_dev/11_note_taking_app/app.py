from flask import Flask, render_template, request, redirect, url_for, jsonify
from tinydb import TinyDB, Query
from loguru import logger

db = TinyDB('db.json')
Note = Query()

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        all_notes = db.all()
        print(all_notes)
        return render_template('home.html', all_notes=all_notes)
    else:
        note_dict = {}
        note_dict['title'] = request.form.get('title')
        note_dict['note'] = request.form.get('note')
        logger.debug(f'note_dict {note_dict}')

        db.insert(note_dict)
        return redirect(url_for('home'))

@app.route('/delete_note')
def delete_note():
    note_no = request.args.get('note_no')
    if note_no == None:
        return "no note no"
    else:
        note_no = int(note_no)
    all_notes = db.all()
    note_to_delete = all_notes[note_no - 1]
    result = db.remove(Note.title == note_to_delete['title'] and Note.note == note_to_delete['note'])
    return redirect(url_for('home'))

@app.route('/edit_note', methods=['GET', 'POST'])
def edit_note():
    if request.method == 'GET':
        note_no = request.args.get('note_no')
        if note_no == None:
            return "no note no"
        else:
            note_no = int(note_no)
        all_notes = db.all()
        note_to_edit = all_notes[note_no - 1]
        return render_template('edit_note.html',
                                note_to_edit=note_to_edit,
                                note_no=note_no)
    else:
        note_no = int(request.args.get('note_no'))
        note_title = request.form.get('title')
        note_text = request.form.get('note')
        all_notes = db.all()
        note_to_edit = all_notes[note_no - 1]
        updated_note = {'title': note_title, 'note':note_text}
        result = db.update(updated_note, Note.title == note_to_edit['title'] and Note.note == note_to_edit['note'])
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
