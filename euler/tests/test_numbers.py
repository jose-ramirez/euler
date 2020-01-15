from euler.numbers import functions as f

def test_sum_up_to_100_works():
    actual = f.sum_up_to(100)
    assert(actual == 5050)

def test_fib():
    actual = f.fib(20)
    assert(actual == [0, 1, 1, 2, 3, 5, 8, 13])

def test_Dn_composite_number():
    assert(f.D(4) == [1, 2, 4])
    assert(f.D(30) == [1, 2, 3, 5, 6, 10, 15, 30])

def test_Dn_prime_number():
    assert(f.D(7) == [1, 7])
    assert(f.D(31) == [1, 31])

def test_phi():
    assert(f.phi(10) == [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4])