from temp import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5

def test_add_negative_numbers():
    assert add_numbers(-1, -2) == -3

def test_add_zero():
    assert add_numbers(0, 5) == 5
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, 0) == 0

def test_add_large_numbers():
    assert add_numbers(1000000, 2000000) == 3000000