from euler.geom.point import Point
from euler.geom.ellipse import Ellipse
from euler.geom.line import Line
import math

p = Point([0.0, 5.0])
e = Ellipse(2.0, 5.0)
l1 = Line(0.0, 0.0)
l2 = Line(0.0, 7.0)

def test_ellipse_has_point():
    assert e.has_point(p) == True

def test_ellipse_intersect():
    assert(len(e.intersect(l1)) == 2)
    assert(len(e.intersect(l2)) == 0)