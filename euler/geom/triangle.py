from euler.geom.geom_helpers import same_side

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def contains(self, p):
        """
            The idea is to return True if the point p is inside this triangle.
        """
        a, b, c = self.a, self.b, self.c
        return same_side(p, a, b, c) and \
            same_side(p, b, a, c) and \
            same_side(p, c, a, b)