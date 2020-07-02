from model.SolarSystem import SolarSystem
from math import sin
from math import radians


def compare_angles(theta1, theta2):
    return sin(theta1) == sin(theta2) or sin(theta1) + sin(theta2) == 0


class Weather:

    def __init__(self, solarsystem: SolarSystem):
        self.solarSystem = solarsystem

    def calculate_drought(self):
        angle_ferengi = radians(self.solarSystem.ferengi.theta)
        angle_vulcano = radians(self.solarSystem.vulcano.theta)
        angle_betasoide = radians(self.solarSystem.betasoide.theta)
        return compare_angles(angle_ferengi, angle_vulcano) and compare_angles(angle_vulcano, angle_betasoide)
