import math
from point2d import Point2D


class Planet:

    def __init__(self, angular_vel, time, distance):
        self.angular_vel = angular_vel
        self.time = time
        self.distance = distance
        self.theta = angular_vel * time
        self.position = Point2D(self.calculate_pos_x(), self.calculate_pos_y())
        self.x_pos = self.calculate_pos_x()
        self.y_pos = self.calculate_pos_y()

    def calculate_pos_x(self):
        grad2rad = math.radians(self.theta)
        return self.distance * math.cos(grad2rad)

    def calculate_pos_y(self):
        grad2rad = math.radians(self.theta)
        return self.distance * math.sin(grad2rad)