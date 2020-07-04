from model.data.SolarSystem import SolarSystem
from model.repo.WeatherRepo import WeatherRepo


class RunApp:

    def __init__(self):
        self.solar_system = SolarSystem()
        self.weather_repo = WeatherRepo(self.solar_system)
        self.weather_repo.initialize_info()

    def get_weather_by_day(self, day):
        return self.weather_repo.search_by_day(day)

    def get_weather_all(self):
        return self.weather_repo.calculate_weather()


def main():
    run_app = RunApp()
    print(run_app.get_weather_by_day(270))
    print(run_app.get_weather_all())


if __name__ == '__main__':
    main()
