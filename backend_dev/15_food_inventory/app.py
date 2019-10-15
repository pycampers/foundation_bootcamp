from flask import Flask, request, jsonify
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy


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

@app.route('/food_donation', methods=['POST'])
def food_donation():
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

    return jsonify(data_dict)

@app.route('/food_receive', methods=['POST'])
def food_receive():
    food_type = request.form.get('food_type')
    city = request.form.get('city')
    result = FoodDonation.query. \
        filter_by(food_type=food_type). \
        filter_by(city=city). \
            all()
            
    print(result)
    return f'{city} {food_type}'


if __name__ == '__main__':
    app.run(debug=True)