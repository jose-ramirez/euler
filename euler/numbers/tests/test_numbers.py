from euler.numbers import functions as f


def test_sum_up_to_100_works():
    actual = f.sum_up_to(100)
    assert(actual == 5050)


def test_fib():
    actual = f.fib(20)
    assert(actual == [0, 1, 1, 2, 3, 5, 8, 13])
