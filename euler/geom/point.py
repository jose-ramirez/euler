from math import sin, cos, pi, fabs

class Point:
    def __init__(self, coordinates):
        """
            For now, we'll assume 2d points:
        """
        self.x = coordinates[0]
        self.y = coordinates[1]

    def __repr__(self):
        return f'({self.x:.2f}, {self.y:.2f})'

    def close_enough(self, p0, tol=1e-5):
        x, y = self.x, self.y
        x1, y1 = p0.x, p0.y
        return fabs(x - x1) < tol and fabs(y - y1) < tol

    def rotate(self, center, theta=pi/2):
        """
            Rotates this point with respect tho the given center,
            theta radians.
        """
        dx, dy = self.x - center.x, self.y - center.y
        new_x = cos(theta) * dx - sin(theta) * dy
        new_y = cos(theta) * dy + sin(theta) * dx
        return Point([new_x + center.x, new_y + center.y])