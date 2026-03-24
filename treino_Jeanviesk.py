# exercício 1:
lista_de_compras = ['leite', 'ovos', 'desinfetante', 'amido', 'coxinha', 
                    'farinha de trigo', 'creme de avelã','suco de uva', 'pão']
# Mostrar os 3 primeiros itens usando slicing
print(lista_de_compras[0:3])
# Substituir o segundo item por outro (explorando mutabilidade):
lista_de_compras[1] = 'fubá'
print(lista_de_compras)
# Adicionar 2 itens novos ao final
lista_de_compras.append('ovos')
lista_de_compras.append('guaraviton')
print(lista_de_compras)
# Mostrar a lista de trás pra frente usando slicing
print(lista_de_compras[::-1])

# exercício 2:
abastecimentos = [
    ("13/09", 8.0, 45.50),
    ("13/08", 140.0, 350.00),
    ("13/07", 25.5, 125.80),
    ("13/06", 30.0, 190.00),
]
# mostrar os dois mais recentes:
print(abastecimentos[0:2])
#total de litros e total de gastos com for:
litros = 0
valor = 0
for dado in abastecimentos:
    litros += dado[1]
    valor += dado[2]
print(f"total de litros: {litros}")
print(f"total gasto: R${valor:.2f}")

# exercicio 3:
clientes = ["Ana", "Carlos", "Bia", "Diego", "Eva", "Fábio", "Gabi", "Hugo"]
print(clientes[0:3])
print(clientes[-3:])
clientes_pares= clientes[0::2]
clientes.insert(1, 'zara')
del clientes[-1]
print(clientes)
podio=tuple(clientes[0:3])