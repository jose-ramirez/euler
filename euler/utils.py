import math
from fractions import gcd
from operator import itemgetter
from math import sin, cos, atan, sqrt
import functools as ft
import euler.numbers.functions as f

class Utils:
    def binom(self, n, k):
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

    def fib(self, m):
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
    #print(sieve(100))

    def is_palindrome(self, s):
        """
            Returns whether a word (assumed
            without whitespaces) is palindrome.
        """
        return s == s[::-1]
    #print(palindrome(str(998801)))

    def to_matrix(self, filename, separator = ' '):
        """
            Returns a matrix from the contents
            of a file (we're assuming it's
            possible anytime we call this function).
            TODO: this needs to be fixed to be able to read
            ALL the input files and returns a matrix with
            the data correctly.
        """
        f = open(filename, 'r')
        return [list(map(self.f1, row.strip('\n').split(separator)) )
            for row in f.readlines()]

    def show(self, matrix):
        """
            Prints a matrix to the screen.
        """
        for row in range(len(matrix)):
            print(matrix[row])

    def size(self, name, matrix):
        """
            Prints the matrix's dimensions, assuming all rows
            have the same length:
        """
        print('%s\'s size: (%d, %d)'
            %(name, len(matrix),len(matrix[0])))

    def to_number(self, filename):
        """
            Returns a number representation of the number
            in a file (it's assumed that it's decimal
            representation is >= 100 digits).
        """
        return int(open(filename, 'r').readline())

    def d(self, n):
        """
            Returns the number of divisors of n.
        """
        i = 1
        res = 0
        while i ** 2 <= n:
            if n % i == 0:
                res += 2
                if n // i == i:
                    res -= 1
            i += 1
        return res

    """
        ... Still don't know if this is useful.
    """
    def f1(self, char):
        if char == '-':
            return 0
        else:
            return int(char)


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
            It is assumed that data is an ordered list. returns the
            index of val in data if val if found, else returns -1.
        """

        #the indices we'll be using to narrow our search:
        a, b = 0, len(data) - 1

        #we need to have enough data to make the testing:
        while b - a + 1 > 0:
            
            #update m to calculate the right address:
            m = b - a + 1

            #our suspect might be here in this position:
            pos = a + (m // 2)

            #found it! return the original index:
            if data[pos] == val:
                return pos

            #might be on the left side of the array:
            elif data[pos] > val:
                b = pos - 1

            #might be on the right side:
            else:
                a = pos + 1

        #here we also found nothing, since we ended up with a
        #pair of indices that can't be interpreted as the
        #extremes of an array:
        return -1

    def parts(self, n):
        """
            Partition function, according to a recurrence due
            to Euler. Returns a list with all values of
            parts(k) for k up to n.
        """
        #initial values for parts(n):
        l = [1, 1, 2]
        i = 3
        for i in range(3, n + 1):
            #initial values for the indices:
            k, k_ = 1, -1
            total = 0
            ind = 0
            a, a_, p_ = i - f.p(k), i - f.p(k_), (-1) ** ind
            indices_valid = a >= 0 or a_ >= 0
            #calculate next value for partition function:
            while indices_valid:
                total += p_ * (l[a] * (a >= 0) + l[a_] * (a_ >= 0))
                #update indices:
                k, k_, ind = k + 1, k_ - 1, ind + 1
                a, a_, p_ = i - f.p(k), i - f.p(k_), (-1) ** ind
                indices_valid = a >= 0 or a_ >= 0
            #add value to list:
            l.append(total)
        return l

    def pi(self, n, prime_list):
        """
            Prime counting function. It depends on already having a
            precomputed list of primes.
        """
        return bisect(prime_list, n) + 1

    def semiprimes(self, n):
        """
            Counts all the semiprimes below n. Slows down as n
            becomes larger. Haven't proved whether the output
            is correct all the time or not:
        """
        p_l = self.sieve(n)
        total = 0
        for p in p_l:
            if p < int(sqrt(n)) + 1:
                total += self.pi(int(n / p), p_l) - \
                    self.pi(p, p_l) + 1
            else:
                break
        print(total)

    #semiprimes(500000)

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

    def mul(self, mat, vec):
        """
            Matrix and vector product.
        """
        res = []
        rows = len(mat)
        cols = len(mat[0])
        for i in range(rows):
            r = mat[i]
            res.append(sum([r[k] * vec[k] for k in range(cols)]))
        return res

    def add(self, v1, v2):
        """
            Vector sum.
        """
        return [v1[k] + v2[k] for k in range(len(v1))]

    def sub(self, v1, v2):
        """
            Vector difference.
        """
        return [v1[k] - v2[k] for k in range(len(v1))]

    def subm(self, m1, m2):
        """
            Matrix deifference.
        """
        m = []
        rows = len(m1)
        for i in range(rows):
            m.append(self.sub(m1[i], m2[i]))
        return m

    def solve_quadratic(self, a, b, c):
        """
            Solve the quadratic equation ax^2 + bx + c = 0.
        """
        d = sqrt((b ** 2) - (4 * a * c))
        return (-b - d) / (2 * a), (-b + d) / (2 * a)

### Some testing for the geometry functions:
#multiply matrix and vector; result should equal [-1, 1]:
#print mul([[0 , -1], [1, 0]], [1, 1])
#
#subtract 2 matrices; should return [[0, 0], [0, 0]]:
#print subm([[1, 0], [0, 1]], [[1, 0], [0, 1]])
