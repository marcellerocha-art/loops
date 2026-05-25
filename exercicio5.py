# Exercício 5: Contagem de vogais
# Você está analisando palavras e deseja saber quantas vogais cada palavra contém. Escreva um programa que conte e exiba o número de vogais em uma palavra inserida pelo usuário.

palavra = input("Digite uma palavra: ")

vogais = 0
i = 0

while i < len(palavra):
    if palavra[i] in "aeiouAEIOU":
        vogais += 1

    i += 1

print("Quantidade de vogais:", vogais)