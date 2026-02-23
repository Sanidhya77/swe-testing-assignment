
# The arithmetic logic of calculator this contains no UI or session logic.


from typing import Union

Number = Union[int, float]


class Calculator:
    #Performs basic arithmetic operations.

    def add(self, a: Number, b: Number) -> Number:
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        return a * b

    def divide(self, a: Number, b: Number) -> Number:
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b