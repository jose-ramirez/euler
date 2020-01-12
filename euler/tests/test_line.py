from euler.geom.point import Point
from euler.geom.line import Line
import math

origin = Point([0.0, 0.0])
c = 1 / math.sqrt(2)

def close_enough(a, b, tol = 1e-5):
    return math.fabs(a - b) < tol

def test_intersect_lines():
    l1 = Line(1.0, 0)
    l2 = Line(-1.0, 0)
    p = l1.intersect(l2)
    x, y = p.x, p.y
    assert close_enough(0, x)
    assert close_enough(0, y)

def test_intersect_lines_2():
    l1 = Line(1.0, 0)
    l2 = Line(-1.0, 1)
    p = l1.intersect(l2)
    x, y = p.x, p.y
    assert close_enough(0.5, x)
    assert close_enough(0.5, y)

def test_rotate_line():
    l1 = Line(1.0, 0)
    l2 = l1.rotate(origin, math.pi / 2)
    m, b = l2.m, l2.b
    assert close_enough(-1.0, m)
    assert close_enough(0, b)

def test_rotate_line():
    l1 = Line(1.0, 0)
    l2 = l1.rotate(Point([0.5, 0.5]), math.pi / 2)
    m, b = l2.m, l2.b
    assert close_enough(-1.0, m)
    assert close_enough(1.0, b)

def test_rotate_line_2():
    l1 = Line(-1.0, 1.0)
    l2 = l1.rotate(Point([0.5, 0.5]), math.pi / 2)
    m, b = l2.m, l2.b
    assert close_enough(1.0, m)
    assert close_enough(0, b)

def test_perpendicular():
    l1 = Line(1.0, 0)
    l2 = l1.perpendicular(Point([0.5, 0.5]))
    m, b = l2.m, l2.b
    assert close_enough(-1.0, m)
    assert close_enough(1.0, b)

def test_angle_lines():
    a = 1 / math.sqrt(3)
    b = 1 / a
    l1 = Line(a, 0)
    l2 = Line(b, 0)
    angle = l2.angle(l1)
    assert close_enough(angle, -math.pi / 6)

def test_angle_lines_2():
    a = 1 / math.sqrt(3)
    b = 1 / a
    l1 = Line(b, 0)
    l2 = Line(a, 0)
    angle = l2.angle(l1)
    assert close_enough(angle, math.pi / 6)

def test_reflect_line():
    a = 1 / math.sqrt(3)
    l1 = Line(a, 0)
    axis = Line(1.0, 0)
    l2 = l1.reflect(axis)
    assert close_enough(1 / a, l2.m)
    assert close_enough(0, l2.b)

def test_reflect_line_2():
    a = math.sqrt(3)
    l1 = Line(a, 0)
    axis = Line(1.0, 0)
    l2 = l1.reflect(axis)
    assert close_enough(1 / a, l2.m)
    assert close_enough(0, l2.b)