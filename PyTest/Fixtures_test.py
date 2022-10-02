import pytest

@pytest.fixture()
def metdname():
    name = "Devlabs"
    return name

def test_greetName(metdname):
    print(metdname)