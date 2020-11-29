from algorithms.least_common_multiple.lcm import lcm


def test_lcm():
    assert lcm(6, 8) == 24
    assert lcm(28851538, 1183019) == 1933053046
    assert lcm(18, 35) == 630
    assert lcm(226553150, 1023473145) == 46374212988031350 