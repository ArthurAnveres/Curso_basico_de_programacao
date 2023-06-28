print("*******************************")
print("         Cálculo do IMC       *")
print("*******************************")
altura=float(input("Insira sua altura: "))
peso=float(input("Insira seu peso: "))
imc = peso/(altura**2)

if (imc<18.5):
    print("Magresa")
elif(imc>=18.5 and imc<=24.9):
    print("Normal")
elif(imc>=25.0) and imc<=29.9:
    print("Sobre peso")
elif(imc>=30.0) and imc<=39.9:
    print("Obesidade")
else:
    print("Obesidade Grave")
