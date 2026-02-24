import os
def limpar():
    os.system('cls')
limpar()
class contabancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self,saldo):
        self.saldo += saldo

    def exibir_saldo(self):
        return(f"titular: {self.titular} o saldo é R${self.saldo:.2f}")
    
conta1 = contabancaria("yuri",1000)
conta1.depositar(500)
print(conta1.exibir_saldo())