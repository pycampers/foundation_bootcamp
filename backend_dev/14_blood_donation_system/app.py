from flask import Flask, render_template, request, redirect, url_for
# from tinydb import TinyDB, Query
from datetime import datetime
from dateutil import parser
import models
from database_manager import Manager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker



dbname = 'blood_bank.db'
engine = create_engine('sqlite:///' + dbname)

database_connection = engine.connect()
        
Session = sessionmaker(bind=engine)
session = Session()
# version - 0.3

# TODO 
# - Disable donate button according the threshold
# - Improve the UI
# - Add the capitalize function to name


latest_donations = {}

# db = TinyDB('db.json')
# Donor = Query()
app = Flask(__name__)

@app.route('/donor')
def donor_form():
    return render_template('donor_form.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register_donor', methods=['POST'])
def register_donor():
    db_manager = Manager('blood_bank.db')
    donor_info = {}
    donor_info['name'] = request.form.get('name').lower()
    donor_info['age'] = request.form.get('age').lower()
    donor_info['blood_group'] = request.form.get('blood_group').lower()
    donor_info['city'] = request.form.get('city').lower()
    donor_info['phone_no'] = request.form.get('phone_no')

    for value in donor_info.values():
        print(value)
        if value == "":
            return "Please enter all the details."

    result = db_manager.read_from_database_filter(
                        models.Donors.c.phone_no == donor_info['phone_no'], 
                        models.Donors
                        )

    if result != None:
        return "Donor already Exists."
    else:
        db_manager.save_to_database(donor_info, models.Donors)
    return redirect(url_for('home'))


@app.route('/receiver', methods=['POST', 'GET'])
def receiver():
    db_manager = Manager('blood_bank.db')

    if request.method == 'GET':
        return render_template('receiver_form.html')
    else:
        blood_group = request.form.get('blood_group').lower()
        city = request.form.get('city').lower()
        # result = db.search((Donor.blood_group == blood_group) & (Donor.city == city))
        result = db_manager.read_from_database_two_filter(
            models.Donors.c.city == city,
            models.Donors.c.blood_group == blood_group,
            models.Donors
            )
        return render_template('show_result.html', donor_list=result)

@app.route('/all_donors')
def show_all_donors():
    db_manager = Manager('blood_bank.db')
    donor_list = db_manager.read_all_data_from_database(models.Donors)
    return render_template('donor_list.html', donor_list=donor_list)

@app.route('/record_time')
def record_time():
    # db_manager = Manager('blood_bank.db')
    current_time = datetime.now().strftime('%c')

    donor_number = request.args.get('phone_no')
    donor = session.query(models.Donors).filter(models.Donors.phone_no == donor_number).\
        update({models.Donors.latest_donation: current_time}, synchronize_session=False)
    print(donor)
    donor.latest_donation = current_time
    # result = db_manager.session.query(models.Donors).get(1)
    # result = db_manager.read_from_database_filter(
    #                 models.Donors.c.phone_no == donor_number, 
    #                 models.Donors
    #                 )
    # result.latest_donation = current_time
    # db_manager.session.commit()
    # last_donation_time_str = latest_donations.get(donor_number)
    # if last_donation_time_str:
    #     last_donation_time = parser.parse(last_donation_time_str)
    #     print('Donation time diff:', datetime.now() - last_donation_time)
    # print(donor_number, current_time)
    # latest_donations[donor_number] = current_time
    # donor_details = db.search(Donor.phone_no == donor_number)[0]
    # print(donor_details)
    # donation_count = donor_details.get('count')

    # if donation_count == None:
    #     db.update({'count': 1}, Donor.phone_no == donor_number)
    # else:
    #     db.update({'count': donation_count+1}, Donor.phone_no == donor_number)

    return redirect(url_for('show_all_donors'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')