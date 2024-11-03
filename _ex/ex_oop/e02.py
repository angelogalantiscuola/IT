class ContoBancario:
    def __init__(self, numero_conto, intestatario, saldo_iniziale):
        self.numero_conto = numero_conto
        self.intestatario = intestatario
        self._saldo = saldo_iniziale

    def get_saldo(self):
        return self._saldo

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo

    def preleva(self, importo):
        if 0 < importo <= self._saldo:
            self._saldo -= importo


# Esempio di utilizzo
conto = ContoBancario("123456789", "Mario Rossi", 1000.0)
print(conto.get_saldo())  # Output: 1000.0
conto.deposita(500.0)
print(conto.get_saldo())  # Output: 1500.0
conto.preleva(200.0)
print(conto.get_saldo())  # Output: 1300.0
