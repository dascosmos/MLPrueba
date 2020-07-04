from model.data.SolarSystem import SolarSystem
from math import sin
from math import radians
from math import sqrt
from point2d import Point2D
from numpy import dot
from numpy import array
from enum import Enum


def compare_angles(theta1, theta2):
    return sin(theta1) == sin(theta2) or sin(theta1) + sin(theta2) == 0


def barycentric_point(a, b, c):

    v0 = array(c) - array(a)
    v1 = array(b) - array(a)
    v2 = array(Point2D(0, 0).cartesian()) - array(a)

    dot00 = dot(v0, v0)
    dot01 = dot(v0, v1)
    dot02 = dot(v0, v2)
    dot11 = dot(v1, v1)
    dot12 = dot(v1, v2)
    inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)

    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    return (u >= 0) and (v >= 0) and (u + v < 1)


def perimeter(p1, p2, p3):
    d1 = sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    d2 = sqrt((p3.x - p2.x)**2 + (p3.y - p2.y)**2)
    d3 = sqrt((p1.x - p3.x) ** 2 + (p1.y - p3.y) ** 2)

    return d1 +d2 + d3


class Drought:

    def __init__(self, solarsystem: SolarSystem):
        self.solarSystem = solarsystem

    def calculate_drought(self):
        angle_ferengi = radians(self.solarSystem.ferengi.theta)
        angle_vulcano = radians(self.solarSystem.vulcano.theta)
        angle_betasoide = radians(self.solarSystem.betasoide.theta)
        return compare_angles(angle_ferengi, angle_vulcano) and compare_angles(angle_vulcano, angle_betasoide)


class Rainy:

    def __init__(self, solarsystem: SolarSystem):
        self.solar_system = solarsystem

    def calculate_sun_inside_triangle(self):
        return barycentric_point(self.solar_system.ferengi.position.cartesian(),
                                 self.solar_system.vulcano.position.cartesian(),
                                 self.solar_system.betasoide.position.cartesian())

    def get_perimeter(self):
        return perimeter(self.solar_system.ferengi.position,
                         self.solar_system.vulcano.position,
                         self.solar_system.betasoide.position)


# TODO: calculate optimal conditions
class Optimal:
    pass


class WeatherTypes(Enum):
    DROUGHT = 1
    RAINY = 2
    MAX_RAINY = 3
    OPTIMAL = 4
    UNKNOWN = 5


class WeatherCalc:

    def __init__(self, solar_system: SolarSystem):
        self.drought = Drought(solar_system)
        self.rainy = Rainy(solar_system)

    def calculate_weather(self):

        if self.drought.calculate_drought():
            return WeatherTypes.DROUGHT, 0.0
        elif self.rainy.calculate_sun_inside_triangle():
            return WeatherTypes.RAINY, self.rainy.get_perimeter()
        else:
            return WeatherTypes.UNKNOWN, 0.0

