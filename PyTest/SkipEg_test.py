import pytest

@pytest.mark.skip
def test_greater():
    num = 10
    assert 10 > 20


@pytest.mark.skipif(1 == 1,reason="Need to skip based on condition")
def test_greatskip():
    num = 10
    assert 10 > 20

def test_greatcheck():
    num = 10
    assert 10 > 20

@pytest.mark.xfail
def test_equal():
    num = 10
    assert num == 10


@pytest.mark.xfail
def test_smaller():
    num = 100
    assert num < 10