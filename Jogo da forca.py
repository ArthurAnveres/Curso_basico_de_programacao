print("______________________________")
print("|        Jogo da forca       |")
print("______________________________")
print("|         Criado por:        |")
print("|        Arthur Anveres      |")
print("|         30/06/2023         |")
print("______________________________")

import random

def jogar_forca():
    palavras = ['python', 'programacao', 'computador', 'jogo', 'desenvolvimento']
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ['_'] * len(palavra_secreta)
    tentativas = 6
    letras_erradas = []
    
    print("Bem-vindo ao jogo da forca!")
    
    while True:
        print()
        print("Palavra: " + ' '.join(letras_acertadas))
        print("Tentativas restantes: " + str(tentativas))
        print("Letras erradas: " + ' '.join(letras_erradas))
        
        if '_' not in letras_acertadas:
            print("Parabéns! Você acertou a palavra!")
            break
        
        if tentativas == 0:
            print("Suas tentativas acabaram! A palavra era: " + palavra_secreta)
            break
        
        letra = input("Digite uma letra: ").lower()
        
        if len(letra) != 1:
            print("Por favor, digite apenas uma letra.")
            continue
        
        if letra in letras_erradas or letra in letras_acertadas:
            print("Essa letra já foi tentada. Tente novamente.")
            continue
        
        if letra in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == letra:
                    letras_acertadas[i] = letra
        else:
            letras_erradas.append(letra)
            tentativas -= 1

if __name__ == '__main__':
    jogar_forca()
