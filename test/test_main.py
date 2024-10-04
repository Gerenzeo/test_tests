import pytest


@pytest.fixture()
def before_after():
    print("\nBefore test")
    yield None
    print("\nAfter test")

def test_demo1(before_after):
    assert 1 == 1

def test_demo2():
    assert 2 == 2

# Command run for target_function
# pytest -v -s <filename>::<function name>
# pytest -v -s test_main.py::test_demo1