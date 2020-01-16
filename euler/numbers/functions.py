import functools as ft
from fractions import gcd
from euler import utils


def p(n):
    """
        The nth pentagonal number.
    """
    return n * (3 * n - 1) // 2


def t(n):
    """
        The nth triangular number.
    """
    return n * (n + 1) // 2


def h(n):
    """
        The nth hexagonal number.
    """
    return n * (2 * n - 1)

def v(n, p):
    """
        Returns the max exponent of p in the prime factiorization of n!,
        by Legendre's formula (https://en.wikipedia.org/wiki/Legendre%27s_formula).
    """
    total = 0
    d = int(n / p)
    while d != 0:
        total += d
        d = int(d / p)
    return total

def power_sum(n, exp, b=10):
    """
        Returns the power sum of n, i.e., if n = abcd...
        in base b (here b defaults to 10), then
        power_sum(n, exp, b) returns sum{a^exp}, taking the
        sum over all of n's digits.
    """
    total = 0
    while n >= b:
        d = n % b
        total += d ** exp
        n /= b
    return total + n ** exp


def factorial(n):
    """
        The very well known factorial function. Given n,
        returns n! for n >= 0.
    """
    if n == 0:
        return 1
    else:
        return ft.reduce(lambda x, y: x * y, range(1, n + 1))


def binom(n, k):
    """
        Calculates the binomial coefficient nCk.
    """
    # what's the difference between this and [[0] * (k + 1)] * (n + 1)?:
    m = [[0 for c in range(k + 1)]
         for r in range(n + 1)]

    # init:
    for i in range(n + 1):
        for j in range(k + 1):
            if i == j or j == 0:
                m[i][j] = 1

    # calculating:
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            m[i][j] = m[i - 1][j - 1] + m[i - 1][j]
    return m, m[n][k]


def sum_up_to(n):
    """
        Returns the sum of all numbers up to n.
    """
    return n * (n + 1) // 2


def fib(m):
    """
        Returns a list with all fibonacci numbers up to m.
    """
    l = []
    l.append(0)
    l.append(1)
    f = 0
    while f < m:
        f = l[-1] + l[-2]
        if f < m:
            l.append(f)
    return l


def d(n):
    """
        Returns the number of divisors of n.
    """
    i = 1
    res = 0
    while i ** 2 <= n:
        if n % i == 0:
            res += 2
            if n / i == i:
                res -= 1
        i += 1
    return res

def D(n):
    """
        Returns a list with the divisors of n.
    """
    l = []
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            l.append(i)
            if n // i != i:
                l.append(n // i)
        i += 1
    l.sort()
    return l

def phi(n):
    """
        Returns a list of Euler's totient function evaluated for 0 <= i <= n.
    """
    u = utils.Utils()
    l = [0, 1]
    for i in range(2, n + 1):
        if u.is_prime(i):
            l.append(i - 1)
        else:
            i_proper_divisors = D(i)[:-1]
            prev_phis = [ l[m] for m in i_proper_divisors ]
            l.append(i - sum(prev_phis))
    return l

def phi_with_sieve(n, primes):
    """
        Returns a list of Euler's totient function evaluated for 0 <= i <= n.
    """
    l = [0, 1]
    for i in range(2, n + 1):
        if i in primes:
            l.append(i - 1)
        else:
            i_proper_divisors = D(i)[:-1]
            prev_phis = [ l[m] for m in i_proper_divisors ]
            l.append(i - sum(prev_phis))
    return l

def lcm(a, b):
    """
        Returns the lcm of two numbers.
    """
    return a * b // gcd(a, b)


def order(a, n):
    """
        Returns the least integer k such that a^k = 1 (mod n).It tends to be
        inefficient as the values increase, but does its job if you give it
        the chance :)
    """
    from fractions import gcd
    order = 0
    if(gcd(a, n) > 1):
        return order
    else:
        order = 1
        mod_exp = a
        while mod_exp != 1:
            order += 1
            mod_exp = (a * mod_exp) % n
    return order


def factorial_sum(n, factorial_list):
    """
        Given n = abcd...e returns sum{a!}, where the sum is taken over all of
        n's digits.
    """
    total = 0
    while n >= 10:
        d = n % 10
        total += factorial_list[d]
        n = n // 10
    return total + factorial_list[n]
