from _ex.ex_oop.e10 import Frazione  # type: ignore


def test_addizione():
    f1 = Frazione(3, 4)
    f2 = Frazione(2, 4)
    f3 = f1 + f2
    assert str(f3) == "Frazione(5, 4)"


def test_sottrazione():
    f1 = Frazione(3, 4)
    f2 = Frazione(2, 4)
    f4 = f1 - f2
    assert str(f4) == "Frazione(1, 4)"


def test_moltiplicazione():
    f1 = Frazione(3, 4)
    f2 = Frazione(2, 4)
    f5 = f1 * f2
    assert str(f5) == "Frazione(6, 16)"


def test_rappresentazione():
    f1 = Frazione(3, 4)
    assert str(f1) == "Frazione(3, 4)"
