import Lab2

def test_find_min_max():
    assert(Lab2.calc_min_max_temperature(5, 10, 15))

def test_calc_average():
    assert(Lab2.calc_average_temperature(5, 10, 15))

def test_calc_median_temperature():
    assert(Lab2.calc_median_temperature(5, 10, 15))