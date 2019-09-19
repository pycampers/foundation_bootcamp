from flask import Flask, request
from loguru import logger
import json

app = Flask(__name__)

phone_directory = []

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == "POST":
        name = request.form.get('name')
        phone_no = request.form.get('phone_no')

        if name == None or phone_no == None:
            return "Please add a name and phone no"
        # print(name, phone_no)
        logger.debug(f'name is {name}')
        logger.debug(f'phone no is {phone_no}')
        phone_entry = {'name': name, 'phone_no':phone_no}
        if phone_entry in phone_directory:
            return "We already have this number"
        else:
            phone_directory.append(phone_entry)
            logger.debug(phone_directory)

            return f"{name}'s' number have been added"

    else:
        phone_directory_json = json.dumps(phone_directory)
        return phone_directory_json

if __name__ == "__main__":
    app.run(debug=True)
