import pytest

@pytest.fixture()
def setup():
    print("setup")
    yield
    print("Teardown")

def test_1_sample(setup):
    print("Hello World")

def test_2_sample2(setup):
    print("Good Morning")