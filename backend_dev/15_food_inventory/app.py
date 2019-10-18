from flask import Flask, request, jsonify, render_template, url_for, redirect
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy


"""
TODO

1. Accept capital city names
2. Food type to drop down
3. Make a home page with links to donate and find food page
"""

file_name = 'FoodDonation.db'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{file_name}"
db = SQLAlchemy(app)

class FoodDonation(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String)
   age = db.Column(db.Integer) 
   expiry = db.Column(db.Integer)
   food_type = db.Column(db.String)
   city = db.Column(db.String)
   phone_no = db.Column(db.String)
   quantity = db.Column(db.Integer) 

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/food_donation', methods=['GET', 'POST'])
def food_donation():
    if request.method == 'GET':
        return render_template('donate.html')
    else:
        data_fields = ['name',
                        'age',
                        'expiry',
                        'food_type',
                        'city',
                        'phone_no',
                        'quantity']
        data_dict = {}
        for field in data_fields:
            data_dict[field] = request.form.get(field)
        food_donation = FoodDonation(**data_dict)
        db.session.add(food_donation)
        db.session.commit()

        return redirect(url_for('food_donation'))

@app.route('/food_receive', methods=['GET','POST'])
def food_receive():
    if request.method == 'GET':
        return render_template('find_food.html')
    else:
        food_type = request.form.get('food_type')
        city = request.form.get('city')
        result = FoodDonation.query. \
            filter_by(food_type=food_type). \
            filter_by(city=city). \
                all()
                
        print(result)
        return render_template('results.html', food_donations=result)

@app.route('/delete_food')
def delete_food():
    food_donation_id = request.args.get('id')
    result = FoodDonation.query.get(food_donation_id)
    print(result)
    db.session.delete(result)
    db.session.commit()
    return redirect(url_for('food_receive'))



if __name__ == '__main__':
    app.run(debug=True)