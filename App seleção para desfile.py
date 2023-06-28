print("*******************************")
print("*  App Seleção para desfile   *")
print("*      Criado por Arthur      *")
print("*        Em 27/06/2023        *")
print("*******************************")
#Esse aplicativo é para selecionar candidatos(as) para desfile de moda
#Para ser aprovada(o) o candidato deve ser maior de 18 anos
#Ou ter altura acima de 1.60m
#operadores lógico do Python: and, or, not
nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
altura=float(input("Digite a sua altura: "))
if (idade>=18 or altura>=1.70):
    print(nome,"pode participar!!!")
else:
    print(nome, "não atende aos requisitos")
