# 4. DESAFIO: FOR DENTRO DE FOR
# Você tem uma lista com várias listas de números:

# numeros = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# Faça um programa que:

# - Percorra todas as listas usando for
# - Mostre cada número na tela
# - No final, mostre a soma total de todos os números

numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = 0

for lista in numeros:

    for numero in lista:
        print(numero)

        soma += numero

print("Soma total:", soma)