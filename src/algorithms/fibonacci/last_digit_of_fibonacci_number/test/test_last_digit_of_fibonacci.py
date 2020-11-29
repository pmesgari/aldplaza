from algorithms.fibonacci.last_digit_of_fibonacci_number.fibonacci_last_digit import get_fibonacci_last_digit

def test_last_digit_of_fibonacci():
    assert get_fibonacci_last_digit(0) == 0
    assert get_fibonacci_last_digit(1) == 1
    assert get_fibonacci_last_digit(0) == 0
    assert get_fibonacci_last_digit(3) == 2
    assert get_fibonacci_last_digit(10) == 5
    assert get_fibonacci_last_digit(20) == 5
    assert get_fibonacci_last_digit(50) == 5
    assert get_fibonacci_last_digit(100) == 5
    assert get_fibonacci_last_digit(331) == 9
