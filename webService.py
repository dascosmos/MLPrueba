import sys
import os
print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend([os.getcwd()])

import flask
from flask import request, jsonify
from model.data.SolarSystem import SolarSystem
from model.repo.WeatherRepo import WeatherRepo

app = flask.Flask(__name__)
app.config['DEBUG'] = True


def init_stellar_system():
    stellar_system = SolarSystem()
    weatherInfo = WeatherRepo(stellar_system)
    weatherInfo.initialize_info()
    return weatherInfo


def to_dict_all(weatherDTO):
    dictionary = {'Drought days': weatherDTO.drought_days,
                  'Rainy days': weatherDTO.rainy_days,
                  'Rainy periods': weatherDTO.rainy_periods,
                  'Optimal periods': weatherDTO.optimal_periods,
                  'Days with Max rain': weatherDTO.max_rainy_days
                  }

    return dictionary


def to_dict_by_day(result):
    dict = {}
    for key in result.keys():
        dict.update({"day": key, "weather": result[key]})

    return dict


weather_repo = init_stellar_system()


@app.route('/', methods=['GET'])
def home():
    return "<h1>Stellar system</h1><p>a software that predicts weather</p>"


@app.route('/forecast/weather', methods=['GET'])
def get_statistics():
    return jsonify(to_dict_all(weather_repo.calculate_weather()))


@app.route('/forecast/byDay', methods=['GET'])
def get_by_day():
    if 'day' in request.args:
        day = int(request.args['day'])
        if day < 0 or day > 3650:
            return "<h1>404</h1><p>The resource could not be found.</p>"
        else:
            return to_dict_by_day(weather_repo.search_by_day(day))
    else:
        return "Error: No id field provided. Please specify an id."


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()
