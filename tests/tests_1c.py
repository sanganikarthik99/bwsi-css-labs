"""
tests_1c.py

unit tests for lab 1c, the maximum contiguous sum
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max_subarray_sum():
    assert max_subarray_sum([-1, -3, 4, 5, 6, 1, 2, 3]) == 21
    assert max_subarray_sum([-1, -2, -3, -4, -5, -6, -7, -8]) == -1
    assert max_subarray_sum([3, -7, 5, -1, 8, -4, 2, -6]) == 12

if __name__ == "__main__":
    pytest.main()