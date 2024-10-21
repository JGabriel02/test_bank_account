class BankAccount:
    def __init__(self, dono, saldo=0.0):
        self.dono = dono
        self.saldo = saldo

    def depositar(self, valor):
            if valor <= 0:
                raise ValueError("O valor do depósito deve ser positivo.")
            self.saldo += valor
            return self.saldo

    def sacar(self, valor):
            if valor <= 0:
                raise ValueError("O valor do saque deve ser positivo.")
            if valor > self.saldo:
                raise ValueError("Saldo insuficiente.")
            self.saldo -= valor
            return self.saldo

    def obter_saldo(self):
            return self.saldo

    def transferir(self, valor, conta_destino):
            if valor <= 0:
                raise ValueError("O valor da transferência deve ser positivo.")
            if valor > self.saldo:
                raise ValueError("Saldo insuficiente.")
            self.saldo -= valor
            conta_destino.depositar(valor)
            return self.saldo

