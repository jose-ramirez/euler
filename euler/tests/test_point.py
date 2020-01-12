from euler.geom.point import Point
from euler.geom.line import Line
import math

origin = Point([0.0, 0.0])
c = 1 / math.sqrt(2)

def close_enough(a, b, tol = 1e-5):
    return math.fabs(a - b) < tol

def test_rotate_point_works():
    p = Point([1.0, 0])    
    p1 = p.rotate(origin, math.pi / 2)
    x, y = p1.x, p1.y
    assert close_enough(0, x)
    assert close_enough(1.0, y)

def test_rotate_point_works_2():
    p = Point([1.0, 0])
    p1 = p.rotate(origin, math.pi / 4)
    x, y = p1.x, p1.y    
    assert close_enough(c, x) 
    assert close_enough(c, y)

def test_rotate_point_works_3():
    p = Point([c, c])
    p1 = p.rotate(origin, math.pi / 2)
    x, y = p1.x, p1.y
    assert close_enough(-c, x)
    assert close_enough(c, y)

def test_rotate_point_works_4():
    p = Point([c, c])
    center = Point([1.0, 1.0])
    p1 = p.rotate(center, math.pi / 2)
    x, y = p1.x, p1.y
    assert close_enough(2 - c, x)
    assert close_enough(c, y)