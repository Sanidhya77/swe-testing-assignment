# Controller layer managing user session stats which separates business logic from GUI.


from app.calculator import Calculator


class CalculatorController:
    #Handles expression building and evaluation.

    def __init__(self):
        self.calculator = Calculator()
        self.expression = ""

    def input(self, char: str) -> str:
        if char == "C":
            self.expression = ""
            return "0"

        if char == "=":
            return self._evaluate()

        self.expression += char
        return self.expression

    def _evaluate(self) -> str:
        for operator in ["+", "-", "*", "/"]:
            if operator in self.expression:
                left, right = self.expression.split(operator)
                a, b = float(left), float(right)

                operations = {
                    "+": self.calculator.add,
                    "-": self.calculator.subtract,
                    "*": self.calculator.multiply,
                    "/": self.calculator.divide,
                }

                result = operations[operator](a, b)
                self.expression = str(result)
                return str(result)

        return "0"