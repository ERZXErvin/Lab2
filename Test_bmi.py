import bmi2 as bmi


def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(1.8,77) == 0)


def test_bmi_over_weight():
    assert(bmi.calculate_bmi(1.8,100) == 1)


def test_bmi_under_weight():
    assert(bmi.calculate_bmi(1.8,5) == -1)