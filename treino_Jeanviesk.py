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


# desafios 2:
vendas = [1250.00, 980.50, 1540.75, 1100.00, 2010.30, 2500.00, 1890.45]
dias = ("Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom")
# Mostre cada dia com sua venda no formato: Seg: R$1250.00
# Calcule e mostre o total de vendas da semana
# Encontre o dia com a maior venda e mostre: Melhor dia: Sáb com R$2500.00
# Mostre quantos dias tiveram vendas acima de R$1500.00
total = 0
for dia, venda in zip(dias, vendas):
    print(f'{dia}: R${venda:.2f}')
for valor in vendas:
    total += valor
print(total)
melhor_dia = 0
for dia in vendas:
    if melhor_dia < dia:
        melhor_dia = dia
        indice_melhor_dia = vendas.index(dia)
print(f'Melhor dia: {dias[indice_melhor_dia]} com valor de {melhor_dia}')
contador_de_dias = 0
for valor in vendas:
    if valor > 1500:
        contador_de_dias += 1
print(contador_de_dias)

# desafio 2 parte 2
senhas = ["abc", "Senh@Forte123", "12345678", "MinhaSenha", "P@ss1", "Prog#2024ok"]

# Para cada senha, usando `for`, verifique e mostre:

# 1. Se tem pelo menos 8 caracteres
# 2. Se contém pelo menos um número (itere sobre os caracteres da senha com outro `for`)
# 3. Se contém pelo menos um caractere especial (`@`, `#`, `!`, `$`, `%`)
# 4. No final, classifique cada senha como `"APROVADA"` (passou nas 3 condições) ou `"REPROVADA"` (falhou em alguma)

# **Exemplo de saída esperada:**
# "abc" -> REPROVADA (menos de 8 caracteres, sem número, sem especial)
# "Senh@Forte123" -> APROVADA
caractere_especial = ('@', '#', '!', '$', '%' )
for senha in senhas:
    problemas=[]
    if len(senha) <= 7:
        problemas.append('menos de oito caracteres')
    numero = False
    for caractere in senha:
        if caractere.isdigit():
            numero = True
            break
    if numero == False:
        problemas.append('a senha deve conter ao menos um número')
    especial = False
    for caracter in senha:
        if caracter in caractere_especial:
            especial=True
            break
    if especial == False:
        problemas.append('a senha deve conter ao menos um caractere especial')
    if problemas:
        problemas = ' '.join(problemas)
        print(f'"{senha}" -> REPROVADA ({problemas}) ')
    else:
        print(f'"{senha}" -> APROVADA')
        