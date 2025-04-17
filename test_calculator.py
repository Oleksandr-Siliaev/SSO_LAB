import pytest
from calculator_module import Calculator
import tkinter as tk


@pytest.fixture
def calc():
    root = tk.Tk()
    root.withdraw()  # не відкриває вікно під час тестів
    return Calculator(root)


def test_addition(calc):
    calc.expression = "2+3"
    calc.equal()
    assert calc.input_text.get() == "5"


def test_subtraction(calc):
    calc.expression = "10-4"
    calc.equal()
    assert calc.input_text.get() == "6"


def test_multiplication(calc):
    calc.expression = "6*7"
    calc.equal()
    assert calc.input_text.get() == "42"


def test_division(calc):
    calc.expression = "15/3"
    calc.equal()
    assert calc.input_text.get() == "5.0"


def test_invalid_expression(calc):
    calc.expression = "5/0"
    calc.equal()
    assert calc.input_text.get() == "Помилка"


def test_history_saving(calc, tmp_path):
    test_file = tmp_path / "test_history.txt"
    calc.save_to_file = lambda record: test_file.write_text(
        f"{record}\n"
    )  # перезаписує метод
    calc.expression = "1+1"
    calc.equal()
    assert test_file.read_text().strip().endswith("1+1 = 2")
