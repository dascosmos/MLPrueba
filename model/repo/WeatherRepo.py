from model.calculations.Weather import WeatherCalc
from model.data.SolarSystem import SolarSystem
from model.calculations.Weather import WeatherTypes
import operator


class WeatherRepo:

    def __init__(self, solar_system: SolarSystem):
        self.solar_system = solar_system
        self.cache = {0: WeatherTypes.DROUGHT.name}
        self.most_rainy_days = {}
        self.weather_calc = WeatherCalc(self.solar_system)

    def initialize_info(self):
        for x in range(1, 3650, 1):
            self.solar_system.calculate_pos_with_time(x)
            weather_type = self.weather_calc.calculate_weather()[0].name
            rainy_days = self.weather_calc.calculate_weather()[1]
            self.cache.update({x: weather_type})
            if rainy_days != 0.0:
                self.most_rainy_days.update({x: rainy_days})

    def search_by_day(self, day):
        return self.cache[day]

    def calculate_weather(self):
        filter_dict = dict(filter(lambda elem: elem[1] != WeatherTypes.UNKNOWN, self.cache.items()))
        cont_drought = 0
        cont_rainy = 0
        cont_rainy_periods = 0
        cont_most_rainy = 0

        for key in filter_dict.keys():
            if filter_dict[key] ==  WeatherTypes.DROUGHT.name:
                cont_drought += 1
            elif filter_dict[key] == WeatherTypes.RAINY.name:
                cont_rainy += 1

        rainy_values = {}
        day_most_rain = []
        keys = list(self.most_rainy_days.keys())
        for x, key in enumerate(keys):
            if x < len(keys)-1:
                if keys[x+1] == key + 1:
                    rainy_values.update({key: self.most_rainy_days[key]})
                else:
                    cont_rainy_periods += 1
                    day_most_rain.append(max(rainy_values.items(), key=operator.itemgetter(1))[0])
                    rainy_values.clear()

        return ("drought days: " + str(cont_drought) +
                " rainy days: " + str(cont_rainy) +
                " rainy perieods: " + str(cont_rainy_periods) + "\n" +
                " days with most rain: " + str(lambda x: x in day_most_rain) + "\n")
