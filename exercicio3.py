# Exercício 3: Adivinhe o número
# Situação Problema: Você está brincando de adivinhar o número que um computador escolheu entre 1 e 100. 
# Cada vez que você adivinha, o computador lhe dirá se o número é maior ou menor. 
# Escreva um programa que permita que o jogador adivinhe o número e conte quantas tentativas foram necessárias.

import random

numero_secreto = random.randint(1, 100)

palpite = 0
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Digite um número entre 1 e 100: "))
    
    tentativas += 1

    if palpite < numero_secreto:
        print("O número é maior!")

    elif palpite > numero_secreto:
        print("O número é menor!")

    else:
        print("Parabéns! Você acertou!")
        print("Tentativas:", tentativas)