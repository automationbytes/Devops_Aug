import pytest


def test_firstMethod():
    assert 1 == 1
    print("Hello World")

@pytest.mark.regression
def test_aMethod():
    print("Regression")
    assert 1 == 2