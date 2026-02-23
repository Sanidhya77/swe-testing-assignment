# Testing Strategy – Quick-Calc

## Overview

The testing approach for this project follows a structured, multi-layered strategy aligned with the concepts presented in Lecture 3.  
The primary objective is to ensure correctness of arithmetic operations while verifying proper interaction between system components.

Testing was integrated throughout development rather than being added at the end, supporting quality assurance across the Software Development Life Cycle (SDLC).

---

## Testing Pyramid

The test suite reflects the **Testing Pyramid** principle:

- A larger number of **Unit Tests** verify core arithmetic logic.
- A smaller number of **Integration Tests** verify interaction between architectural layers.

Unit tests form the foundation of the test suite because they are fast, isolated, deterministic, and easier to maintain.

This distribution aligns with modern best practices in software engineering.

---

## Unit Testing (White-Box Testing)

Unit tests focus on the `Calculator` class, which contains pure arithmetic logic.

These tests directly verify:

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero
- Negative numbers
- Decimal numbers
- Large numbers
- Mixed-sign subtraction
- Decimal division

This represents a **white-box testing approach**, as the internal logic of arithmetic operations is directly tested with knowledge of implementation details.

Each function is tested independently to ensure correctness under normal and edge-case conditions.

---

## Integration Testing (Black-Box Testing)

Integration tests focus on the `CalculatorController`.

These tests simulate realistic user interaction flows:

- Enter digits
- Select an operator
- Press equals
- Clear expression

The controller is tested strictly through its public interface (`input()` method), without accessing internal state or implementation details. This reflects a **black-box testing approach**.

The purpose of integration testing here is to verify that:

- Controller logic correctly delegates operations to the Calculator
- Expression state is maintained properly
- Clear functionality resets state as expected

---

## Functional vs Non-Functional Testing

### Functional Testing (Implemented)

The project focuses primarily on functional correctness, including:

- Accurate arithmetic results
- Proper zero-division handling
- Correct state reset using the clear command
- Correct evaluation of expressions

### Non-Functional Testing (Not Implemented)

The following were intentionally excluded due to assignment scope:

- Performance testing
- GUI usability testing
- Load or stress testing
- Cross-platform compatibility testing

The emphasis of this project is on software testing strategy rather than UI or performance validation.

---

## Regression Testing

The complete Pytest suite acts as a regression safety mechanism.

After any code modification, running:

```bash
pytest
```

ensures that previously implemented functionality remains stable and correct.

This supports safe refactoring and continuous improvement.

---

## Test Results Summary

| Test Name                    | Type        | Status |
|------------------------------|------------|--------|
| test_addition                | Unit        | Pass   |
| test_subtraction             | Unit        | Pass   |
| test_multiplication          | Unit        | Pass   |
| test_division                | Unit        | Pass   |
| test_division_by_zero        | Unit        | Pass   |
| test_negative_numbers        | Unit        | Pass   |
| test_decimal_numbers         | Unit        | Pass   |
| test_large_numbers           | Unit        | Pass   |
| test_subtract_negative       | Unit        | Pass   |
| test_divide_decimal          | Unit        | Pass   |
| test_full_addition_flow      | Integration | Pass   |
| test_clear_resets_expression | Integration | Pass   |

All tests pass successfully under Python 3.11.

---

## Conclusion

The testing strategy demonstrates structured application of unit and integration testing aligned with modern software engineering principles and Lecture 3 concepts.

The layered architecture (Calculator → Controller → GUI) enables independent testing of business logic and interaction logic, ensuring clarity, maintainability, and reliability.

The project reflects correct application of:

- The Testing Pyramid
- White-box and Black-box testing approaches
- Functional testing principles
- Regression testing practices