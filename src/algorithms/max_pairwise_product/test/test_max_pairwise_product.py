import pytest
from random import randrange
from algorithms.max_pairwise_product.max_pairwise_product import max_pairwise_product, max_pairwise_product_naive


def test_max_pairwise_product():
    assert max_pairwise_product([]) == 0
    assert max_pairwise_product([1]) == 1
    assert max_pairwise_product([1, 2, 3]) == 6
    assert max_pairwise_product([10, 2, 3, 4, 5, 1, 12]) == 120
    assert max_pairwise_product([100000, 90000]) == 9000000000
    assert max_pairwise_product([62172, 70573, 58683, 66775, 23917, 1677, 57520, 25615, 22089]) == 4712512075
    print("done")


@pytest.mark.stresstest
def test_stress_test():
    while True:
        max_size = 10
        max_value = 100000
        a = [randrange(1, max_value) for i in range(0, max_size)]
        print(a)
        result_1 = max_pairwise_product(a)
        result_2 = max_pairwise_product_naive(a)
        assert result_1 == result_2, f"Detected a wrong answer, expected {result_2} got {result_1} with input {a}"


    