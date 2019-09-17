from flask import Flask, request
import json
import weather_info

app = Flask(__name__)

@app.route('/')
def get_weather_data():
    city = request.args.get("city")
    if city == None:
        response = "Please enter a city in the url."
        return response
    else:
        weather_data = weather_info.main(city)
        weather_data_json = json.dumps(weather_data)
        return weather_data_json

if __name__ == "__main__":
    app.run(debug=True)