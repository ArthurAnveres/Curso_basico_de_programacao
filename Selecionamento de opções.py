while True:
    print("1-cadastrar")
    print("2-alterar")
    print("3-Apagar")
    print("4-mostrar")
    print("5-sair")
    escolha=input("Escolha uma opção!")
    if escolha=="1":
        print("Cadastro efetuado com sucesso!!!")
    elif escolha=="2":
        print("Cadastro alterado com sucesso!!!")
    elif escolha=="3":
        print("Cadastro apagado com sucesso")
    elif escolha=="4":
        print("Cadastro mostrado com sucesso!!!")
    elif escolha=="5":
        print("Desligando sistema saida bem sucedida")
        break
    else:
        print("Você digitou um valor fora da faixa 1-5!!!!")
