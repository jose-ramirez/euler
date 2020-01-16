from euler.utils import Utils

def test_to_matrix():
    u = Utils()
    u.to_matrix('./test_matrix.in')

def test_to_matrix_2():
    u = Utils()
    u.to_matrix('./test_matrix_2.in', separator=',')

def test_log_factorial():
    u = Utils()
    actual = u.log_factorial(5)
    assert(actual > 0)

def test_log_nPr():
    u = Utils()
    actual = u.log_nPr(5, 4)
    assert(actual > 0)

def test_is_prime():
    u = Utils()
    actual_prime = u.is_prime(31)
    assert(actual_prime == True)

def test_sieve():
    u = Utils()
    primes = u.sieve(50)
    assert(primes == [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])

def test_sieve_set():
    u = Utils()
    primes = u.sieve_set(50)
    assert(primes == set([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]))

def test_is_prime_corner_cases():
    u = Utils()
    actual_prime = u.is_prime(2)
    assert(actual_prime == True)

    actual_prime = u.is_prime(3)
    assert(actual_prime == True)

    actual_prime = u.is_prime(4)
    assert(actual_prime == False)

    actual_prime = u.is_prime(5)
    assert(actual_prime == True)

def test_is_composite():
    u = Utils()
    actual_prime = u.is_prime(2200)
    assert(actual_prime == False)