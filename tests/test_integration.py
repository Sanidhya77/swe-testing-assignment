from app.controller import CalculatorController


def test_full_addition_flow():
    controller = CalculatorController()

    controller.input("5")
    controller.input("+")
    controller.input("3")
    result = controller.input("=")

    assert result == "8.0"


def test_clear_resets_expression():
    controller = CalculatorController()

    controller.input("9")
    controller.input("+")
    controller.input("1")
    controller.input("=")

    result = controller.input("C")

    assert result == "0"