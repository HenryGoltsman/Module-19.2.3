import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): # умножение
        assert self.calc.multiply(self, 4, 4) == 16

    def test_division_calculate_correctly(self): # деление
        assert self.calc.division(self, 25, 5) == 5

    def test_subtraction_calculate_correctly(self): # вычитание
        assert self.calc.subtraction(self, 14, 4) == 10

    def test_adding_calculate_correctly(self): # сложение
        assert self.calc.adding(self, 21, 2) == 23



    def test_multiply_calculation_failed(self): # умножение
        assert self.calc.multiply(self, 4, 4) == 8 # негативный

    def test_division_calculation_failed(self): # деление
        assert self.calc.division(self, 25, 5) == 4 # негативный

    def test_subtraction_calculation_failed(self):  # вычитание
        assert self.calc.subtraction(self, 14, 4) == 5  # негативный

    def test_adding_calculation_failed(self): # сложение
        assert self.calc.adding(self, 21, 2) == 32 # негативный
