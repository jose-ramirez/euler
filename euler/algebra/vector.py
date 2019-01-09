class Vector:
    def __init__(self, components):
        self.components = components

    @staticmethod
    def from_points(p1, p2):
        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y
        return Vector([y1 - y2, x1 - x2])

    def dot(self, b):
        x, y = self.components, b.components
        return sum([x[i] * y[i] for i in range(len(self.components))])

    def cross_2d(self, b):
        """
            Cross product for 2d vectors, seen as 3d vectors with
            z component equal to 0.
        """
        v1 = self.components
        v2 = b.components
        return Vector([0, 0, v1[0] * v2[1] - v1[1] * v2[0]])