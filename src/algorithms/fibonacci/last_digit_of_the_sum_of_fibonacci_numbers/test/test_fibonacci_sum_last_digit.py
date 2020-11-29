import pytest
from random import randrange
from algorithms.fibonacci.last_digit_of_the_sum_of_fibonacci_numbers.fibonacci_sum_last_digit import \
    fibonacci_sum, fibonacci_sum_naive

def test_fibonacci_sum_last_digit():
    assert fibonacci_sum(3) == 4
    assert fibonacci_sum(7) == 3
    assert fibonacci_sum(8) == 4
    assert fibonacci_sum(100) == 5
    assert fibonacci_sum(614162383528) == 9
