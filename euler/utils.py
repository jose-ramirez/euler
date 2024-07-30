import math
from math import gcd
from operator import itemgetter
from math import sin, cos, atan, sqrt, log
import functools as ft
import euler.numbers.functions as f

class Utils:
    def sieve(self, n=100):
        """
            Returns all primes less than n (if possible
            in a reasonable amount of time).
            Taken from
            http://code.activestate.com/recipes/577228-sieve-of-eratosthenes-python/
        """
        sqrtn = int(n**0.5)
        sieve = [True] * (n+1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, sqrtn+1):
            if sieve[i]:
                m = n//i - i
                sieve[i*i:n+1:i] = [False] * (m+1)
        sieve = [i for i in range(n+1) if sieve[i]]
        return sieve

    def sieve_set(self, n=100):
        """
            Returns all primes less than n (if possible
            in a reasonable amount of time).
            Taken from
            http://code.activestate.com/recipes/577228-sieve-of-eratosthenes-python/
        """
        sqrtn = int(n**0.5)
        sieve = [True] * (n+1)
        sieve[0] = False
        sieve[1] = False
        for i in range(2, sqrtn+1):
            if sieve[i]:
                m = n//i - i
                sieve[i*i:n+1:i] = [False] * (m+1)
        sieve = {i for i in range(n+1) if sieve[i]}
        return sieve

    def is_palindrome(self, s):
        """
            Returns whether a string (assumed without whitespaces) is palindrome.
        """
        return s == s[::-1]

    def to_matrix(self, filename, separator=' ', null_value = '-'):
        """
            Returns a matrix from the contents of a file (we're assuming it's
            possible anytime we call this function).
        """
        def try_get_value(c):
            return 0 if c == null_value else int(c)

        with open(filename, 'r') as f:
            return [[try_get_value(c) for c in row.strip('\n').split(separator)]
                for row in f.readlines()]

    def show(self, matrix):
        """
            Prints a matrix to the screen.
        """
        for row in range(len(matrix)):
            print(matrix[row])

    def to_number(self, filename):
        """
            Returns a number representation of the number in a file (it's
            assumed that it's decimal representation is >= 100 digits).
        """
        return int(open(filename, 'r').readline())

    def log_factorial(self, n):
        """
            Returns ln(n!).
        """
        return sum([log(i) for i in range(1, n + 1)])

    def log_nPr(self, n, r):
        """
            Returns ln(n! / (n - r)!).
        """
        return sum([log(i) for i in range(n - r + 1, n + 1)])

    def exp_mod(self, x, y, n):
        """
            Returns the value of x ** y (mod n), when x ** y
            is a really huge number, like 10 ** (10 ** 9).
        """
        if y == 0:
            return 1
        z = self.exp_mod(x, y // 2, n)
        if y % 2 == 0:
            return (z ** 2) % n
        else:
            return (x * (z ** 2)) % n

    def chop(self, val, data):
        """
            Self made iterative binary search :)

            It is assumed that data is an ordered list. Returns the index of
            val in data if val if found, else returns -1.
        """

        # the indices we'll be using to narrow our search:
        a, b = 0, len(data) - 1

        # we need to have enough data to make the testing:
        while b - a + 1 > 0:

            # update m to calculate the right address:
            m = b - a + 1

            # our suspect might be here in this position:
            pos = a + (m // 2)

            # found it! return the original index:
            if data[pos] == val:
                return pos

            # might be on the left side of the array:
            elif data[pos] > val:
                b = pos - 1

            # might be on the right side:
            else:
                a = pos + 1

        # here we also found nothing, since we ended up with a
        # pair of indices that can't be interpreted as the
        # extremes of an array:
        return -1

    def parts(self, n):
        """
            Partition function, according to a recurrence due to Euler.

            Returns a list with all values of parts(k) for k up to n.
        """
        # initial values for parts(n):
        l = [1, 1, 2]
        i = 3
        for i in range(3, n + 1):
            # initial values for the indices:
            k, k_ = 1, -1
            total = 0
            ind = 0
            a, a_, p_ = i - f.p(k), i - f.p(k_), (-1) ** ind
            indices_valid = a >= 0 or a_ >= 0
            # calculate next value for partition function:
            while indices_valid:
                total += p_ * (l[a] * (a >= 0) + l[a_] * (a_ >= 0))
                # update indices:
                k, k_, ind = k + 1, k_ - 1, ind + 1
                a, a_, p_ = i - f.p(k), i - f.p(k_), (-1) ** ind
                indices_valid = a >= 0 or a_ >= 0
            # add value to list:
            l.append(total)
        return l

    def is_prime(self, n):
        """
            Returns true iff n is prime. A rather inefficient implementation.
        """
        return all([n % i != 0 for i in range(2, int(sqrt(n) + 1))])

    def divisors_dict(self, m, primes):
        """
            Dictionary with prime factors of m and its exponents:
        """
        vals = {}
        for p in primes:
            if m == 1:
                return vals
            if m % p != 0:
                continue
            else:
                m = m / p
                total = 1
                while m % p == 0:
                    total += 1
                    m = m / p
                vals.update({str(p): total})
        return vals
