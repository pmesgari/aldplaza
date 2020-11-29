import pytest
from random import randrange
from algorithms.fibonacci.last_digit_of_the_partial_sum_of_fibonacci_numbers.fibonacci_partial_sum import \
    fibonacci_partial_sum, fibonacci_partial_sum_naive


def test_fibonacci_partial_sum():
    assert fibonacci_partial_sum(10, 10) == 5
    assert fibonacci_partial_sum(3, 7) == 1
    assert fibonacci_partial_sum(10, 200) == 2
    assert fibonacci_partial_sum(5, 8) == 7



@pytest.mark.stresstest
def test_stress_test():
    while True:
        m, n = sorted([randrange(0, 10) for x in range(0, 2)])
        result_fast = fibonacci_partial_sum(m, n)
        result_naive = fibonacci_partial_sum_naive(m, n)
        print(f"Running stress test with m={m} n={n}")
        assert result_fast ==  result_naive, f"Detected a wrong answer, \
            expected {result_naive} got {result_fast} \
            with input m={m} n={n}"