from src.math_operation import add, sub, mul

def test_addition():
    assert add(3, 2) == 5
    assert add(4, 2) == 6

def test_subtracting():
    assert sub(5, 2) == 3
    assert sub(8, 2) == 6

def test_multiplication():
    assert mul(5, 2) == 10
    assert mul(8, 2) == 16
