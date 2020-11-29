from algorithms.fibonacci.fibonacci_number.fibonacci import calc_fib


def test_fibonacci():
    assert calc_fib(0) == 0
    assert calc_fib(1) == 1
    assert calc_fib(2) == 1
    assert calc_fib(3) == 2
    assert calc_fib(10) == 55
    assert calc_fib(20) == 6765
    assert calc_fib(50) == 12586269025
    assert calc_fib(100) == 354224848179261915075