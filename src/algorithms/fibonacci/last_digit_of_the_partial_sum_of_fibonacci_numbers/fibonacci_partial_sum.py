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
    """
    return Fn mod m
    """
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


def fibonacci_partial_sum(from_, to):
    """
    return the last digit of a partial sum of Fibonacci numbers
    """
    if from_ == to:
        return get_fibonacci_huge(to, 10)
    if from_ == 0:
        return fibonacci_sum(to)
    else:
        last_digit_sum_from_ = fibonacci_sum(from_ - 1)
        last_digit_sum_to = fibonacci_sum(to)
        if last_digit_sum_to < last_digit_sum_from_:
            return 10 + last_digit_sum_to - last_digit_sum_from_
        return last_digit_sum_to -  last_digit_sum_from_
    


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))