from flask import Flask
import json
from dict_to_html_table import make_html_table_from_dict

app = Flask(__name__)

name = "Hasan"
hometown = "Kota"
current_city = "Bangalore"
job = "Educator"

site_info = {'counter':0}

@app.route('/hello')
def hello_world():
    return 'just to test again'

@app.route('/about')
def about():
    '''Returns my bio in text format.'''
    my_bio = f'''
    Hello, Myself {name}. 
    I am from {hometown} and currently living in {current_city}.
    Working as an {job}.
    '''
    return my_bio

@app.route('/about/json')
def about_json():
    '''Returns my bio as a dict in json format.'''
    my_bio = {"name": name,
              "hometown": hometown,
              "current_city": current_city,
              "job": job}

    json_my_bio = json.dumps(my_bio)

    return json_my_bio

@app.route('/about/html')
def about_html():
    my_bio_html = f'''
    <html>
        <body>
            <h1>Hello, Myself {name}.</h1> </br>
            <p>I am from {hometown} and currently living in {current_city} </p>
            <p>Working as an {job}</p>
        </body>
    </html>
    '''

    return my_bio_html

@app.route('/dir_table')
def show_table():
    base_html = """
    <!DOCTYPE html>
        <html>
        <head>
        <style>
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        th, td {
        padding: 5px;
        text-align: left;    
        }
        </style>
        </head>
        <body>

        <h2>Cell that spans two columns</h2>
        <p>To make a cell span more than one column, use the colspan attribute.</p>

        <table style='width:100%'>
    """

    footer = """
            </table>

        </body>
        </html>
    """
    data_dict = [{"Name": "Hasan", "Telephone": "12345678"},
                {"Name": "Lorenzo", "Telephone": "98765432"}]

    html_table = make_html_table_from_dict(data_dict)
    print(html_table)
    final_html_page = base_html + html_table + footer

    return final_html_page
    



@app.route('/count_visits')
def count_visits():
    site_info['counter'] += 1
    message = f"This page have been visited {site_info['counter']} times."
    return message


# if you import this file from any other file, the code after the if condition
# will not run
if __name__ == "__main__":
    app.run(debug=True)