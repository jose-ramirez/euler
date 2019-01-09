from euler.algebra.vector import Vector

def same_side(p1, p2, a, b):
    """
        Returns True if points p1, p2 are on the same side of
        the line joining a and b.
        Taken from the following page:
        http://www.blackpawn.com/texts/pointinpoly/
    """
    l = Vector.from_points(b, a)
    lp1 = Vector.from_points(p1, a)
    lp2 = Vector.from_points(p2, a)

    cp1 = l.cross_2d(lp1)
    cp2 = l.cross_2d(lp2)
    return cp1.dot(cp2) >= 0