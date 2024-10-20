from _ex.ex_oop.e06 import CartaDiCredito, PayPal, effettua_pagamento  # type: ignore


def test_carta_di_credito_processa_pagamento(capfd):
    pagamento_carta = CartaDiCredito(
        "Mario Rossi", "1234 5678 9012 3456", "12/23", "123"
    )
    pagamento_carta.processa_pagamento()
    captured = capfd.readouterr()
    assert "Elaborazione pagamento con Carta di Credito per Mario Rossi" in captured.out


def test_paypal_processa_pagamento(capfd):
    pagamento_paypal = PayPal("mario.rossi@example.com", "password123")
    pagamento_paypal.processa_pagamento()
    captured = capfd.readouterr()
    assert (
        "Elaborazione pagamento con PayPal per mario.rossi@example.com" in captured.out
    )


def test_effettua_pagamento_carta_di_credito(capfd):
    pagamento_carta = CartaDiCredito(
        "Mario Rossi", "1234 5678 9012 3456", "12/23", "123"
    )
    effettua_pagamento(pagamento_carta)
    captured = capfd.readouterr()
    assert "Elaborazione pagamento con Carta di Credito per Mario Rossi" in captured.out


def test_effettua_pagamento_paypal(capfd):
    pagamento_paypal = PayPal("mario.rossi@example.com", "password123")
    effettua_pagamento(pagamento_paypal)
    captured = capfd.readouterr()
    assert (
        "Elaborazione pagamento con PayPal per mario.rossi@example.com" in captured.out
    )
