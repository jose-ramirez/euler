from euler.geom.triangle import Triangle
from euler.geom.point import Point

def test_triangle_contains_point():
    a = Point([-340, 495])
    b = Point([-153, -910])
    c = Point([835, -947])
    p = Point([0, 0])
    t = Triangle(a, b, c)
    assert t.contains(p) == True

def test_triangle_not_contains_point():
    a = Point([-175, 41])
    b = Point([-421, -714])
    c = Point([574, -645])
    p = Point([0, 0])
    t = Triangle(a, b, c)
    assert t.contains(p) == False