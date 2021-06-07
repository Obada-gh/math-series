from math_series.math_series import fibonacci
from math_series.math_series import lucas
from math_series.math_series import sum_series

def test_five():
    assert fibonacci(5) == 5
    assert lucas(5) == 11
   


def test_one():
    assert fibonacci(1) == 1
    assert lucas(1) == 1

def test_zero():
    assert fibonacci(0) == 0
    assert lucas(0) == 2

def test_sum():
    assert sum_series(5,5,5) == 40    #new series 
    assert sum_series(5) == 5         #same lucas
    assert sum_series(5,0,1) == 5 
    assert sum_series(5,2,1) == 11    #same fibonacci

