# Basic-Calculator

Basic-Calculator is a simple calculator application built in Python.  
The goal of this project is not only to implement arithmetic operations, but also to apply software testing principles and professional Git workflow practices discussed in Lecture 3.

The calculator supports:

- Addition  
- Subtraction  
- Multiplication  
- Division (with proper zero-division handling)  
- Clear functionality  
- Graphical User Interface using Tkinter  

---

## Project Structure

The project follows a layered design:

```
swe-testing-assignment/
│
├── app/
│   ├── calculator.py      # Core arithmetic logic
│   ├── controller.py      # Session and input management
│   └── gui.py             # Tkinter graphical interface
│
├── tests/
│   ├── test_calculator.py
│   └── test_integration.py
│
├── pytest.ini
├── requirements.txt
├── README.md
├── TESTING.md
```

### Architecture Layers

- **Calculator (Business Logic Layer)** – Contains pure arithmetic operations.
- **Controller Layer** – Manages user input and expression state.
- **GUI Layer** – Tkinter interface that interacts only with the controller.

This separation ensures that business logic is independently testable without depending on the user interface, improving maintainability and testability.

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Sanidhya77/swe-testing-assignment
cd swe-testing-assignment
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python -m app.gui
```

---

## Running the Test Suite

All tests can be executed using:

```bash
pytest
```

The test suite includes both unit and integration tests and supports regression testing.

---

## Testing Framework Research: Pytest vs Unittest

Python provides multiple testing frameworks, including `unittest` (built-in) and `pytest`.

### unittest

- Part of Python standard library  
- Class-based test structure  
- More verbose syntax  
- Requires more boilerplate code  
- Less flexible fixtures  

### pytest

- Cleaner and more concise syntax  
- Powerful fixture system  
- Better readability  
- Easier scalability for larger projects  
- Advanced features such as parameterization and plugins  

For this project, **pytest** was chosen due to its concise syntax, flexibility, and strong alignment with the Testing Pyramid model. Its minimal boilerplate enables clearer test expression and improves overall maintainability.