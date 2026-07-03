import pytest
from code_optimizer import calculate_total_with_tax

def test_calculate_total_with_standard_tax():
    assert calculate_total_with_tax([10, 20, 30]) == 69.0

def test_calculate_total_empty_list():
    assert calculate_total_with_tax([]) == 0.0

def test_calculate_total_negative_value_raises_error():
    with pytest.raises(ValueError):
        calculate_total_with_tax([10, -20, 30])
