from model.data.Planet import Planet


class SolarSystem:

    def __init__(self):
        self.ferengi = Planet(-1, 500)
        self.vulcano = Planet(5, 1000)
        self.betasoide = Planet(-3, 2000)

    def calculate_pos_with_time(self, time):
        self.ferengi.calculate_with_time(time)
        self.vulcano.calculate_with_time(time)
        self.betasoide.calculate_with_time(time)