import pytest
from app import add

def test_add_positive_integers():
    assert add(5, 7) == 12

def test_add_floats():
    assert add(2.5, 3.5) == 6.0

def test_add_with_zero():
    assert add(10, 0) == 10
    assert add(0, 0) == 0

def test_add_negative_numbers():
    assert add(-5, -3) == -8

def test_add_mixed_numbers():
    assert add(10, -4) == 6