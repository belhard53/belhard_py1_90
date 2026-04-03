import pytest
from func_for_test import sum_of_numbers




@pytest.mark.parametrize(
    'n, expected', (
        (123, 6),
        (12, 3),
        (111, 3),
        (0, 0),
    )
)
def test_sum_of_number(n, expected):
    assert sum_of_numbers(n) == expected
    
# запускать так
# pytest lesson16\example\testing\test_sum_num.py
# pytest lesson16\example\testing - все тесты