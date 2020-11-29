from algorithms.fibonacci.fibonacci_number_huge.fibonacci_huge import get_fibonacci_huge


def test_get_fibonacci_huge():
    assert get_fibonacci_huge(2015, 3) == 1
    assert get_fibonacci_huge(239, 1000) == 161
    assert get_fibonacci_huge(2816213588, 239) == 151