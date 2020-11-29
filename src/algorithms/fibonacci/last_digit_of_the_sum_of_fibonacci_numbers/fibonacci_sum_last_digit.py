# Uses python3
import sys

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


def fibonacci_sum(n):
    """
    return last digit of a sum of the first n Fibonacci numbers
    """
    last_digit_of_the_nth_plus_2 = get_fibonacci_huge(n + 2, 10)
    if last_digit_of_the_nth_plus_2 == 0:
        return 9
    else:
        return last_digit_of_the_nth_plus_2 - 1

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
