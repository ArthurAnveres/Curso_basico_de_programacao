login="usuario"
senha="senha123"
tentativas=0

print("*********************")
print("*   TELA DE LOGIN   *")
print("*     DO USUÁRIO    *")
print("*     Criado por:   *")
print("*   Arthur Anveres  *")
print("*  Data: 29/06/2023 *")
print("*     Versão 1.0    *")
print("*********************")
while True:
    entrada_login=input("Digite seu login: ")
    entrada_senha=input("Digite sua senha: ")
    if entrada_login==login and entrada_senha==senha:
        while True:
            print("********************")
            print("* TELA DE CADASTRO *")
            print("********************")
            print("1-CADASTRAR")
            print("2-ALTERAR")
            print("3-APAGAR")
            print("4-LISTAR")
            print("5-SAIR")
            escolha=input("Digite a opção desejada e tecle ENTER: ")
            if escolha=="1":
                print("Cadastrado com sucesso!!!")
            elif escolha=="2":
                print("Cadastro alterado com sucesso!!!")
            elif escolha=="3":
                print("Cadastro apagado com sucesso!!!")
            elif escolha=="4":
                print("Cadastro listado com sucesso!!!")
            elif escolha=="5":
                print("Até logo!!!")
                break
            else:
                print("Você escolheu uma opção que não existe!!!")
                print("Escolha de 1 a 5 e pressione ENTER!!!")
    else:
        tentativas+=1
        print("Login ou senha incorretos!!!")
        if tentativas>=3:
            print("Excedeu o número de tentativas, sistema finalizado!!!")
            break
