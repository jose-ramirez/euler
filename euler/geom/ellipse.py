from euler.geom.point import Point
from euler.geom.line import Line
import math

class Ellipse:
    def __init__(self, a, b):
        """
            The equation for the ellipse we'll
            be using is (x/a)^2 + (y/b)^2 = 1.
        """
        self.a = a
        self.b = b

    def intersect(self, line):
        """
            Should return the points of intersection
            of the line and this ellipse, if any,
            or an empty list if none is found.
        """
        m, c = line.m, line.b
        a, b = self.a, self.b
        den = (a * m) ** 2 + b ** 2
        d = a * b * math.sqrt(den - c ** 2)
        x1 = (-a ** 2 * m * c + d) / den
        x2 = (-a ** 2 * m * c - d) / den
        points = [Point([x1, m * x1 + c]), Point([x2, m * x2 + c])]
        return filter(lambda p: self.has_point, points)

    def has_point(self, point):
        """
            Is the given point on the ellipse?
        """
        x, y = point.x, point.y
        a, b = self.a, self.b
        f = (x / a) ** 2 + (y / b) ** 2
        return math.fabs(1.0 - f) < 1e-5

    def tangent(self, point):
        """
            Returns the tangent line to this ellipse
            at the given point. For now, I'll assume
            the point always lies on the ellipse, so it
            should always return an actual tangent line.
        """
        x, y = point.x, point.y
        a, b = self.a, self.b
        m = (- (b / a) ** 2) * (x / y)
        return Line(m, y - m * x)