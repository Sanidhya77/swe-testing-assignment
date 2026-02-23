
#Tkinter graphical interface for Calculator.


import tkinter as tk
from app.controller import CalculatorController


class CalculatorGUI:
    #GUI layer interacting with controller.

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Basic Calculator")
        self.controller = CalculatorController()

        self.display = tk.Entry(root, width=20, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4)

        self._create_buttons()

    def _create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for text, row, col in buttons:
            tk.Button(
                self.root,
                text=text,
                width=5,
                height=2,
                command=lambda t=text: self._on_click(t)
            ).grid(row=row, column=col)

    def _on_click(self, char):
        result = self.controller.input(char)
        self.display.delete(0, tk.END)
        self.display.insert(0, result)


def run():
    root = tk.Tk()
    CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run()