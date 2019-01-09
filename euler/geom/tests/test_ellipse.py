from euler.geom.point import Point
from euler.geom.ellipse import Ellipse
import math

p = Point([0.0, 5.0])
e = Ellipse(2.0, 5.0)

def test_ellipse_has_point():
    assert e.has_point(p) == True