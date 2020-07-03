import math
from point2d import Point2D


def calculate_grad(ang_vel, time):
    theta = ang_vel * time
    if theta < 0:
        return 360 + (theta % 360)
    else:
        return theta % 360


def calculate_pos_x(theta, distance):
    grad2rad = math.radians(theta)
    return distance * math.cos(grad2rad)


def calculate_pos_y(theta, distance):
    grad2rad = math.radians(theta)
    return distance * math.sin(grad2rad)


class Planet:

    def __init__(self, angular_vel, distance):
        self.angular_vel = angular_vel
        self.distance = distance
        self.x_pos = distance
        self.y_pos = 0.0
        self.position = Point2D(self.x_pos, self.y_pos)
        self.theta = 0.0

    def calculate_with_time(self, time):
        self.theta = calculate_grad(self.angular_vel, time)
        self.x_pos = calculate_pos_x(self.theta, self.distance)
        self.y_pos = calculate_pos_y(self.theta, self.distance)
        return Point2D(self.x_pos, self.y_pos)

    def __str__(self):
        return '{self}'.format(self=self)
