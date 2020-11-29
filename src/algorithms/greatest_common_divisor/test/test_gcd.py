from algorithms.greatest_common_divisor.gcd import gcd


def test_gcd():
    assert gcd(206, 40) == 2
    assert gcd(1344, 217) == 7