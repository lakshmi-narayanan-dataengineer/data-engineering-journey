"""
Unit Tests for Math Utilities
-----------------------------
Testing is critical for production code to ensure reliability 
and prevent regression bugs.
"""
import logging
from math_utils import safe_divide

logging.basicConfig(filename="test_case_op.txt",level=logging.INFO)

def test_safe_divide_valid():
    """Test valid division operation."""
    assert safe_divide(6, 2) == 3.0


def test_safe_divide_zero_division():
    """Test handling of division by zero."""
    assert safe_divide(6, 0) == "Cannot Divide By Zero"


if __name__ == "__main__":
    # Manual execution for quick debugging
    test_safe_divide_valid()
    test_safe_divide_zero_division()
    logging.info("All test cases passed successfully!")