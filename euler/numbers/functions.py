import functools as ft
from fractions import gcd

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

def power_sum(n, exp, b = 10):
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
    #que diferencia hay entre esto y [[0] * (k + 1)] * (n + 1)?:
    m = [[0 for c in range (k + 1)]
        for r in range(n + 1)]

    #init:
    for i in range(n + 1):
        for j in range(k + 1):
            if i == j or j == 0:
                m[i][j] = 1

    #calculating:
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            m[i][j] = m[i - 1][j - 1] + m[i - 1][j]
    return m, m[n][k]

def sum_up_to(n):
    """
        Returns the sum of all numbers up to n.
    """
    return n * (n + 1) // 2
#print(sum_up_to(100))

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
#print(fib(20))

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

def lcm(a, b):
    """
        Returns the lcm of two numbers.
    """
    return a * b // gcd(a, b)

def order(a, n):
    """
        Retorna order(a, n), el menor entero k que cumple
        que a^k = 1 (mod n). Tiende a ser ineficiente a
        medida que los valores crecen, pero cumple con su
        objetivo si le das la oportunidad :)
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

def power_sum(n, exp, b = 10):
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
        n = n // b
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

def factorial_sum(n, factorial_list):
    """
        Given n = abcd...e returns sum{a!}, where the sum
        is taken over all of n's digits.
    """
    total = 0
    while n >= 10:
        d = n % 10
        total += factorial_list[d]
        n =  n // 10
    return total + factorial_list[n]