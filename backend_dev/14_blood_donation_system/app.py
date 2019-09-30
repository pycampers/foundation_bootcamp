from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB, Query


db = TinyDB('db.json')
Donor = Query()
app = Flask(__name__)

@app.route('/donor')
def donor_form():
    return render_template('donor_form.html')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register_donor', methods=['POST'])
def register_donor():
    donor_info = {}
    donor_info['name'] = request.form.get('name').lower()
    donor_info['age'] = request.form.get('age').lower()
    donor_info['blood_group'] = request.form.get('blood_group').lower()
    donor_info['city'] = request.form.get('city').lower()
    donor_info['phone_no'] = request.form.get('phone_no')

    search_result = db.search(Donor.phone_no == donor_info['phone_no'])
    if len(search_result) != 0:
        return "Donor already Exists." 
    else:
        db.insert(donor_info)
        return redirect(url_for('home'))


@app.route('/receiver', methods=['POST', 'GET'])
def receiver():
    if request.method == 'GET':
        return render_template('receiver_form.html')
    else:
        blood_group = request.form.get('blood_group').lower()
        city = request.form.get('city').lower()
        result = db.search((Donor.blood_group == blood_group) & (Donor.city == city))
        return render_template('show_result.html', donor_list=result)

if __name__ == '__main__':
    app.run(debug=True)