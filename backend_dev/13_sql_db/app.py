from flask import Flask, render_template, request, url_for, redirect
from database_manager import Manager
import models

app = Flask(__name__)


@app.route('/')
def home():
    db_manager = Manager('user_details.db')
    result = db_manager.read_all_data_from_database(models.Students)
    return render_template('home.html', all_users=result )

@app.route('/add_student', methods=['POST'])
def add_student():
    db_manager = Manager('user_details.db')
    user_data = {}
    user_data['name'] = request.form.get('firstname')
    user_data['lastname'] = request.form.get('lastname')
    user_data['country'] = request.form.get('country')
    user_data['phone'] = request.form.get('phone_no')

    db_manager.save_to_database(user_data, models.Students)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)