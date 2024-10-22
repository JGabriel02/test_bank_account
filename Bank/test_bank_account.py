import pytest
from bank_account import BankAccount

# Cenário Unitário
def test_criacao_conta():
    conta = BankAccount("João")
    assert conta.obter_saldo() == 0.0, "O saldo inicial deve ser 0.0"

def test_criacao_conta_com_saldo_inicial():
    conta = BankAccount("Maria", 150.0)
    assert conta.obter_saldo() == 150.0, "O saldo inicial deve ser 150.0"


def test_deposito_valido():
    conta = BankAccount("Maria", 100.0)
    saldo_atual = conta.depositar(50.0)
    assert saldo_atual == 150.0, "O saldo deve ser 150 após o depósito de 50"

def test_deposito_invalido():
    conta = BankAccount("Maria", 100.0)
    with pytest.raises(ValueError, match="O valor do depósito deve ser positivo"):
        conta.depositar(-10.0)

# Cenário 3: Saques
def test_saque_valido():
    conta = BankAccount("Carlos", 200.0)
    saldo_atual = conta.sacar(50.0)
    assert saldo_atual == 150.0, "O saldo deve ser 150 após o saque de 50"

# Cenário Funcional:


def test_saque_invalido():
    conta = BankAccount("Carlos", 50.0)
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        conta.sacar(100.0)


def test_transferencia_valida():
    conta1 = BankAccount("Ana", 300.0)
    conta2 = BankAccount("Pedro", 100.0)
    saldo_atual = conta1.transferir(50.0, conta2)
    assert saldo_atual == 250.0, "O saldo da conta1 deve ser 250 após a transferência de 50"
    assert conta2.obter_saldo() == 150.0, "O saldo da conta2 deve ser 150 após receber a transferência de 50"

def test_transferencia_invalida():
    conta1 = BankAccount("Ana", 100.0)
    conta2 = BankAccount("Pedro", 100.0)
    with pytest.raises(ValueError, match="Saldo insuficiente"):
        conta1.transferir(200.0, conta2)

def test_obter_saldo_deposito():
    conta = BankAccount("Maria", 100.0)
    conta.depositar(50.0)
    assert conta.obter_saldo() == 150.0, "O saldo deve ser 150 após o depósito de 50"

def test_obter_saldo_saque():
    conta = BankAccount("Carlos", 200.0)
    conta.sacar(50.0)
    assert conta.obter_saldo() == 150.0, "O saldo deve ser 150 após o saque de 50"

