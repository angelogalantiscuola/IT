# pylint: disable=import-error
# pylint: disable=no-name-in-module
# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=redefined-outer-name

import pytest
from _ex.ex_oop.e02 import ContoBancario  # type: ignore


@pytest.fixture
def conto():
    return ContoBancario("123456789", "Mario Rossi", 1000.0)


def test_get_saldo(conto):
    assert conto.get_saldo() == 1000.0


def test_deposita(conto):
    conto.deposita(500.0)
    assert conto.get_saldo() == 1500.0


def test_preleva(conto):
    conto.preleva(200.0)
    assert conto.get_saldo() == 800.0


def test_preleva_insufficient_funds(conto):
    conto.preleva(2000.0)
    assert conto.get_saldo() == 1000.0  # Saldo should remain unchanged


def test_deposita_negative_amount(conto):
    conto.deposita(-500.0)
    assert conto.get_saldo() == 1000.0  # Saldo should remain unchanged
