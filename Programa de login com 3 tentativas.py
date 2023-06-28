login="usuario"
senha="senha123"
contador=0
while True:
    entrada_login=input("Digite seu login: ")
    entrada_senha=input("Digite sua senha: ")
    if entrada_login==login and entrada_senha==senha:
        print("login bem sucedido!!!")
        break
    else:
        contador+=1
        print("Tentativas restantes: ",contador)
        print("Login ou senha incorretos!!!")
        if contador==3:
            print("Excedeu o número de tentativas, sistema finalizado!!!")
            break
