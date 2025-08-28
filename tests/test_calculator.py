"""Tests for the calculator module."""

import pytest
from pytest_workshop.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.calculator = Calculator()

    def test_add(self):
        """Test addition functionality."""
        assert self.calculator.add(2, 3) == 5
        assert self.calculator.add(-1, 1) == 0
        assert self.calculator.add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction functionality."""
        assert self.calculator.subtract(5, 3) == 2
        assert self.calculator.subtract(1, 1) == 0
        assert self.calculator.subtract(-1, -1) == 0

    def test_multiply(self):
        """Test multiplication functionality."""
        assert self.calculator.multiply(3, 4) == 12
        assert self.calculator.multiply(-2, 3) == -6
        assert self.calculator.multiply(0, 5) == 0

    def test_divide(self):
        """Test division functionality."""
        assert self.calculator.divide(10, 2) == 5
        assert self.calculator.divide(-6, 2) == -3
        assert self.calculator.divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calculator.divide(5, 0)

    def test_power(self):
        """Test power functionality."""
        assert self.calculator.power(2, 3) == 8
        assert self.calculator.power(5, 0) == 1
        assert self.calculator.power(3, 2) == 9


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
])
def test_add_parametrized(a, b, expected):
    """Test addition with parametrized inputs."""
    calculator = Calculator()
    assert calculator.add(a, b) == expected