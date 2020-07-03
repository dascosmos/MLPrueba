from model.SolarSystem import SolarSystem
from math import sin
from math import radians
from point2d import Point2D
from numpy import dot


def compare_angles(theta1, theta2):
    return sin(theta1) == sin(theta2) or sin(theta1) + sin(theta2) == 0


def barycentric_point(a, b, c):
    v0 = c - a
    v1 = b - a
    v2 = Point2D(0, 0).cartesian() - a

    dot00 = dot(v0, v0)
    dot01 = dot(v0, v1)
    dot02 = dot(v0, v2)
    dot11 = dot(v1, v1)
    dot12 = dot(v1, v2)
    inv_denom = 1 / (dot00 * dot11 - dot01 * dot01)

    u = (dot11 * dot02 - dot01 * dot12) * inv_denom
    v = (dot00 * dot12 - dot01 * dot02) * inv_denom

    return (u >= 0) and (v >= 0) and (u + v < 1)


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


# TODO: calculate optimal conditions
class Optimal:
    pass
