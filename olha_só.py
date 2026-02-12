import os
def limpar():
    os.system('cls')
limpar()
numero = int(input("digite seu numero ate onde vai: "))
numero1 = numero + 1
for i in range (1,numero1,1):
    print(f"{i}: oii mundo")