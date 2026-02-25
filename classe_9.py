import os
def limpar():
    os.system('cls')
limpar()
class contabancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self,valor):
        if valor > 0:
            self.saldo += valor
    
    def sacar(self,valor):
        if self.saldo > valor:
            return(f"saque feito {valor}, conta atual :{self.saldo - valor}")
        else:
            return ("saldo insuficiente")

    def exibir_saldo(self):
        return (f"titular: {self.titular} o saldo é R${self.saldo:.2f}")
    
conta1 = contabancaria("yuri",1000)
conta1.depositar(500)
print(conta1.exibir_saldo())
print(conta1.sacar(200))
