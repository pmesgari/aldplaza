# Uses python3
import sys
import time
import random

'''
Goal: calculate Fn mod m for very large n
    S1 find the pisano period pisano(m)
    S2 calculate r = n mod pisano(m)
    S3 calculate Fr mod m
'''


def pisano(m):
    previous = 0
    current = 1
    period = 1
    while True:
        previous, current = current, (previous + current) % m
        if (previous == 0 and current == 1):
            return period
        else:
            period = period + 1
    return period


def calc_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    result = []
    result.append(0)
    result.append(1)
    for i in range(2, n+1):
        result.append(result[i-1] + result[i-2])
    return result[n]


def get_fibonacci_huge(n, m):
    pisano_period = pisano(m)
    r = n % pisano_period
    return calc_fib(r) % m


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
