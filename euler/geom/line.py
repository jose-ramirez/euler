from euler.geom.point import Point
import math

class Line:
    def __init__(self, m, b):
        """
            Our base eq. here will be y = mx + b.
        """
        self.m = m
        self.b = b

    def reflect(self, axis):
        """
            Returns the reflected line of this one
            with respect to the given axis.
        """
        p = self.intersect(axis)
        alpha = self.angle(axis)
        return axis.rotate(p, alpha)

    def perpendicular(self, point):
        """
            Returns the perpendicular to this line
            with respect to the given point.
        """
        m_p = -1.0 / self.m
        x, y = point.x, point.y
        return Line(m_p, y - m_p * x)

    def angle(self, other_line):
        """
            Returns the angle between this line
            and another one.
        """
        m2, m1 = self.m, other_line.m
        return math.atan2(m1 - m2, 1 + m1 * m2)

    def intersect(self, other_line):
        """
            Returns the intersection point of this
            line and the one passed as parameter,
            or None if the lines are 'parallel enough'.
        """
        m1, m2 = self.m, other_line.m
        b1, b2 = self.b, other_line.b
        if m1 == m2: # lines are parallel, or equal
            return None
        else:
            p_x = (b1 - b2) / (m2 - m1)
            p_y = (m2 * b1 - m1 * b2) / (m2 - m1)
            return Point([p_x, p_y])

    def rotate(self, p, theta):
        """
            Returns the result of rotating this line
            theta radians with respect to p.
        """
        m, b = self.m, self.b
        some_x1, some_x2 = 1.0, 2.0
        some_y1, some_y2 = m * some_x1 + b, m * some_x2 + b
        p1, p2 = Point([some_x1, some_y1]), Point([some_x2, some_y2])
        new_p1, new_p2 = p1.rotate(p, theta), p2.rotate(p, theta)
        x1, y1, x2, y2 = new_p1.x, new_p1.y, new_p2.x, new_p2.y
        new_m = (y2 - y1) / (x2 - x1)
        new_b = y1 - (new_m * x1)
        return Line(new_m, new_b)