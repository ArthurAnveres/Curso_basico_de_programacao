"""Calculadora:
    Crie uma calculadora que seja capaz de realizar operações matemáticas básicas, como adição,
    subtração, multiplicação e divisão."""

print("--------------------------------------")
print("-            Calculadora             -")
print("--------------------------------------")
print("-            Criado por:             -")
print("-           Arthur Anveres           -")
print("-            30/06/2023              -")
print("--------------------------------------")

continua=True
#Escolha de operação
while True:
    print("Escolha uma opção: ")
    print("1 - Adição")
    print("2 - subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    opcao=input()
#Adicionar os números
    numero1=float(input("Digite o primeiro número: "))
    numero2=float(input("Digite o segundo número: "))
#Mostrando os resultados
    if opcao == "1":
        print(f"({numero1})","+",f"({numero2})","=",numero1+numero2)
    elif opcao == "2":
          print(f"({numero1})","-",f"({numero2})","=",numero1-numero2)
    elif opcao == "3":
         if numero2==0:
             print("Não é possivel dividir por zero")
         print(f"({numero1})","*",f"({numero2})","=",numero1**numero2)
    elif opcao == "3":
          print(f"({numero1})","/",f"({numero2})","=",numero1/numero2)
#Adicionar os números
