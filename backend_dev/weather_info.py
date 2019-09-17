import requests
import json


def get_woeid(city_name):
    id_query_url = f"https://www.metaweather.com/api/location/search/?query={city_name}"
    json_data = requests.get(id_query_url).content

    weather_data = json.loads(json_data)
    weather_id = weather_data[0]["woeid"]

    return weather_id


def get_weather_data(woeid, all=False):
    weather_data_url = f"https://www.metaweather.com/api/location/{woeid}/"
    json_data = requests.get(weather_data_url).content

    weather_data = json.loads(json_data)
    # https://codebeautify.org/jsonviewer
    # json viewer
    important_data = {}

    important_keys = ["weather_state_name",
        #   "id",

        #   "weather_state_abbr",
        #   "wind_direction_compass",
        #   "created",
        "applicable_date",
        "min_temp",
        "max_temp",
        "the_temp",
        "wind_speed",
        #   "wind_direction",
        #   "air_pressure",
        "humidity",
        #   "visibility",
        "predictability",
        ]

    single_day_data = weather_data["consolidated_weather"][0]

    if all == False:
        for single_key in important_keys:
            important_data[single_key] = single_day_data[single_key]

        return important_data
    else:
        return single_day_data


def main(city, all_data=False):
    woeid = get_woeid(city)
    weather_data = get_weather_data(woeid, all_data)
    return weather_data

if __name__ == "__main__":
    woeid = get_woeid("bangalore")
    weather_data = get_weather_data(woeid)
    print(weather_data)