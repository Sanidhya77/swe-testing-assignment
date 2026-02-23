import pytest
from app.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


def test_addition(calc):
    assert calc.add(5, 3) == 8


def test_subtraction(calc):
    assert calc.subtract(10, 4) == 6


def test_multiplication(calc):
    assert calc.multiply(6, 7) == 42


def test_division(calc):
    assert calc.divide(8, 2) == 4


def test_division_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)


def test_negative_numbers(calc):
    assert calc.add(-5, -3) == -8


def test_decimal_numbers(calc):
    assert calc.multiply(2.5, 2) == 5.0


def test_large_numbers(calc):
    assert calc.multiply(1_000_000, 3) == 3_000_000


def test_subtract_negative(calc):
    assert calc.subtract(5, -3) == 8


def test_divide_decimal(calc):
    assert calc.divide(7.5, 2.5) == 3