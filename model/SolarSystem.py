from model.Planet import Planet


class SolarSystem:

    def __init__(self, time):
        self.ferengi = Planet(-1, time, 500)
        self.vulcano = Planet(5, time, 1000)
        self.betasoide = Planet(-3, time, 2000)
