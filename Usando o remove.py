frutas=["banana","uva","pera","abacate"]
print(frutas)
nome=input("Digite o nome da fruta para remover: ")
if nome in frutas:
    frutas.remove(nome)
    print("Fruta deletada com sucesso!!!")
    print(frutas)
else:
    print("Fruta não encontrada!!!")
    print(frutas)
