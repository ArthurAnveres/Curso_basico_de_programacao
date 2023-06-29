print("____________________________")
print("|   CADASTRO DE USUÁRIOS   |")
print("____________________________")
print("|          Menu            |")
print("____________________________")
print("|1 - Cadastrar             |")
print("|2 - Listar                |")
print("|3 - Sair                  |")
print("____________________________")

#Lista Vazia
nomes=[]

#Criando um loop enquanto verdadeiro
while True:
    opcao=input("Escolha o opção desejada: ")
    if opcao=="1":
        print("**********************")
        print("*  Tela de Cadastro  *")
        print("**********************")
        nome=input("Digite o nome: ")
        nomes.append(nome)
        print
    elif opcao=="2":
        print(nomes)
    elif opcao=="3":
        print("Até breve...")
        break
    else:
        pass
