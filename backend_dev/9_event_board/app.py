from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query
import json

db = TinyDB('db.json')
Event = Query()
app = Flask(__name__)

@app.route('/add_event', methods=['POST', 'GET'])
def hello_name():
    if request.method == 'GET':
        return render_template('add_event.html')
    else:
        event_data = ['name',
                    'area',
                    'start_time',
                    'end_time',
                    'organizer',
                    'attendents']
        event_details = {}
    
        for data_point in event_data:
            event_details[data_point] = request.form.get(data_point)
        db.insert(event_details)
        return redirect(url_for('home'))

@app.route('/')
def home():
    all_events = db.all()
    return render_template('events.html', all_events=all_events)


@app.route('/remove_event', methods=['POST'])
def remove_event():
    event_name = request.form.get('event_name')
    result = db.remove(Event.name == event_name)
    print(result)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug = True)