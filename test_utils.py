from euler.utils import Utils as u


def test_log_factorial():
    actual = u.log_factorial(5)
    assert(actual > 0)


def test_log_nPr():
    actual = u.log_nPr(5, 4)
    assert(actual > 0)
