import pytest

def test_one():
    assert "hello" == "Hello".lower()

def test_two():
    assert "hello" != "Hello"

@pytest.mark.regression
def test_three():
    a = 5
    b = 3
    c = a>b
    assert c == True
    print("Regression")