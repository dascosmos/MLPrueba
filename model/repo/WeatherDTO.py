

class WeatherDTO:

    def __init__(self, drought_days, rainy_days, rainy_periods, optimal_periods, max_rainy_days):
        self.drought_days = drought_days
        self.rainy_days = rainy_days
        self.rainy_periods = rainy_periods
        self.optimal_periods = optimal_periods
        self.max_rainy_days = max_rainy_days
