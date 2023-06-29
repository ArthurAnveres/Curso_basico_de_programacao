#Lista
frutas=["banana","uva","pera","abacate"]
print(frutas)

nome=input("Qual fruta deseja alterar? ")

if nome in frutas:
    indice=frutas.index(nome)
    novo_nome=input("Digite o novo nome alterado: ")
    frutas[indice]=novo_nome
    print(frutas)
else:
    print("Fruta não encontrada!!!")
    print(frutas)
