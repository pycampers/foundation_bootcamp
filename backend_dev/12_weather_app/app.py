from flask import Flask, jsonify, render_template, request
from weather_data import get_city_weather
app = Flask(__name__)

weather_states = {'Snow':'fas fa-snowflake',
                  'Sleet': 'fas fa-stroopwafel',
                  'Hail': 'fas fa-snowflake',
                  'Thunderstorm': 'fas fa-bolt',
                  'Heavy Rain': 'fas fa-cloud-showers-heavy',
                  'Light Rain': 'fas fa-cloud-rain',
                  'Showers': 'fas fa-shower',
                  'Heavy Cloud': 'fas fa-cloud',
                  'Light Cloud': 'fas fa-cloud-sun',
                  'Clear': 'fas fa-sun'
                  }


@app.route('/')
def hello_world():
    # weather_data = get_city_weather('bangalore')

    return render_template('home.html')


@app.route('/show_weather', methods=['POST'])
def show_weather():
    city_name = request.form.get('city_name')
    weather_data = get_city_weather(city_name)
    return render_template('weather.html', weather_data=weather_data, weather_states=weather_states)


if __name__ == '__main__':
    app.run(debug=True)