import requests
import json

def get_city_weather(city_name):
    url_to_search_for_id = 'https://www.metaweather.com/api/location/search/?query={}'
    json_data = requests.get(url_to_search_for_id.format(city_name)).content
    weather_id_dict_data = json.loads(json_data)
    city_weather_id = weather_id_dict_data[0]['woeid']

    url_to_get_weather_data = 'https://www.metaweather.com/api/location/{}/'
    json_data = requests.get(url_to_get_weather_data.format(city_weather_id)).content
    weather_info_dict_data = json.loads(json_data)
    return weather_info_dict_data

if __name__ == '__main__':
    result = get_city_weather('bangalore')
    print(result)