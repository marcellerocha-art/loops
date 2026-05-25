
# Exercício 1 - Metas de Vendas:
# Dadas as listas abaixo de vendedores e vendas, crie um loop WHILE
# que ira imprimir somente os nomes do vendedores que bateram a meta:

# venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]
# vendedores = ['maria', 'mara', 'joão', 'silva', 'santos', 'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']

# meta = 50

venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]

vendedores = ['maria', 'mara', 'joão', 'silva', 'santos',
'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']

meta = 50

i = 0

while i < len(venda):
    if venda[i] >= meta:
        print(vendedores[i])

    i += 1