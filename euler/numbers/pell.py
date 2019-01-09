from math import sqrt
import sys

def PQa(P0, Q0, D):
    A = [0, 1]
    B = [1, 0]
    G = [-P0, Q0]
    P, Q = [P0], [Q0]
    a0 = int((P0 + sqrt(D)) / Q0)

    a = [a0]
    A.append((a[-1] * A[-1]) + A[-2])
    B.append((a[-1] * B[-1]) + B[-2])
    G.append((a[-1] * G[-1]) + G[-2])
    P.append((Q[-1] * a[-1]) - P[-1])
    Q.append((D - (P[-1] * P[-1])) // Q[-1])

    while 2 * a0 not in a:
        a, A, B, G, P, Q = step(a, A, B, G, P, Q, D)

    l = len(a[1:])

    if l % 2 == 1:
        for i in range(l):
            a, A, B, G, P, Q = step(a, A, B, G, P, Q, D)

    return a, B[2:], G[2:]

def step(a, A, B, G, P, Q, D):
    a.append(int((P[-1] + sqrt(D)) / Q[-1]))
    A.append((a[-1] * A[-1]) + A[-2])
    B.append((a[-1] * B[-1]) + B[-2])
    G.append((a[-1] * G[-1]) + G[-2])
    P.append((Q[-1] * a[-1]) - P[-1])
    Q.append((D - (P[-1] * P[-1])) // Q[-1])
    return a, A, B, G, P, Q

def min_sol(D):
    if is_square(D):
        return -1, -1

    a, B, G = PQa(0, 1, D)

    l = len(a[1:])

    if l % 2 == 1:
        return G[2 * l - 1], B[2 * l - 1]
    else:
        return G[l - 1], B[l - 1]

def verify_pell(a, b, D):
    return a * a - (D * b * b)

def is_square(n):
    return int(sqrt(n)) ** 2 == n