def gerar_baralho(qtde_baralhos=1, coringas=False, embaralhar=False):
    # cria o número necessario de baralhos e embaralha
    baralho = []
    naipes = ["♠", "♥", "♦", "♣"]
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for _ in range(qtde_baralhos):
        for naipe in naipes:
            for numero in valores:
                baralho.append(f'{numero}{naipe}')
        if coringas:
            baralho.append('Coringa Vermelho')
            baralho.append('Coringa Preto')
    if embaralhar:
        import random
        random.shuffle(baralho)
    return baralho

def mostrar_baralho(baralho):
    # printa o baralho de 13 em 13 e mostra o tamanho total
    copia = baralho.copy()
    print(f'O baralho tem {len(baralho)} cartas')
    while copia:
        print(copia[:13])
        del copia[:13]

def calcular_baralho(baralho, qtde_cartas, qtde_jogadores=2):
    # calcula a quantidade de cartas necessárias pra cada jogador
    resto = len(baralho) - (qtde_jogadores * qtde_cartas)
    print(f'cada jogador deve receber {qtde_cartas} cartas')
    print(f'ainda existem {resto} cartas na mesa')

def mostrar_jogadores(qtde, jogadores, baralho):
    # mostra a mão de cada um dos jogadores.
    baralho_copia = baralho.copy()
    for jogador in jogadores:
        mao_do_jogador = baralho_copia[:qtde]
        del baralho_copia[:qtde]
        print(f'a mão do {jogador} é {" ".join(mao_do_jogador)}')

def validar_termos(mg):
    while True:
        try:
            return int(input(mg))
        except ValueError:
            print('Digite um valor inteiro!')

# seleção automatica de baralhos: criar um dicionário com os cinco jogos mais populares
# de cartas para que a seleção seja mais simplificada.

jogos_padrão = {
        'Truco': {
            'qtde_jogadores_max': 4,
            'qtde_jogadores_min': 2,
            'qtde_cartas': 3,
            'qtde_baralhos': 1,
            'coringas': False
        },

        'Buraco': {
            'qtde_jogadores_max': 4,
            'qtde_jogadores_min': 2,
            'qtde_cartas': 11,
            'qtde_baralhos': 2,
            'coringas': True
        },

        'Poker': {
            'qtde_jogadores_max': 10,
            'qtde_jogadores_min': 2,
            'qtde_cartas': 2,
            'qtde_baralhos': 1,
            'coringas': False
        },

        'Blackjack': {
            'qtde_jogadores_max': 7,
            'qtde_jogadores_min': 1,
            'qtde_cartas': 2,
            'qtde_baralhos': 1,
            'coringas': False
        },

        'Paciencia': {
            'qtde_jogadores_max': 1,
            'qtde_jogadores_min': 1,
            'qtde_cartas': 0,
            'qtde_baralhos': 1,
            'coringas': False
        },

        'Canastra': {
            'qtde_jogadores_max': 4,
            'qtde_jogadores_min': 2,
            'qtde_cartas': 11,
            'qtde_baralhos': 2,
            'coringas': True
        },
}

lista_jogos = ('Canastra', 'Paciencia', 'Truco', 'Blackjack', 'Poker', 'Buraco')

validar_coringa = True

validar_jogadores = True

print('-'*30)

print('SIMULADOR DE BARALHO')

print('-'*30)

# seletor de modo, aqui o usuário deve selecionar se deseja
# usar regras de um jogo existente ou um inédito.

validação = True
while validação:
    print('deseja fazer a seleção com regras arbitrárias ou jogar um jogo já existente?')
    modo = input('modo manual ou modo automático?(m/a): \n').lower()
    if modo in ('m', 'a'):
        validação = False
    else:
        print('por favor escolha um modo de seleção!')

if modo == 'a':
    jogo = input(f'por favor, selecione um jogo da lista: \n{lista_jogos} :\n').capitalize()
    if jogo not in lista_jogos:
        print('infelizmente ainda não possuímos esse jogo em nosso banco de jogos!')
        print('por favor selecione as regras de maneira manual!')
        modo = 'm'
    else:
        qtde_jogadores_max = jogos_padrão[jogo]['qtde_jogadores_max']
        qtde_jogadores_min = jogos_padrão[jogo]['qtde_jogadores_min']
        qtde_cartas = jogos_padrão[jogo]['qtde_cartas']
        qtde_baralhos = jogos_padrão[jogo]['qtde_baralhos']
        coringas = jogos_padrão[jogo]['coringas']
        while validar_jogadores:
            qtde_jogadores = validar_termos('coloque a quantidade de jogadores que desejam jogar: \n')
            if qtde_jogadores > qtde_jogadores_max or qtde_jogadores < qtde_jogadores_min:
                print(f'a quantidade de jogadores deve estar entre {qtde_jogadores_min} e {qtde_jogadores_max}')
            else:
                validar_jogadores = False

if modo == 'm':
        qtde_cartas = validar_termos('quantas cartas cada jogador deve receber? : \n')

        qtde_baralhos = validar_termos('quantos baralhos desejam usar? : \n')

        while validar_coringa:
            coringas = input('deseja usar coringas(s/n)? : \n').lower()
            if coringas == 'n':
                coringas = False
                validar_coringa = False
            else:
                coringas = True
                validar_coringa = False

        qtde_jogadores = validar_termos('quantos jogadores desejam jogar? \n')

deseja_emb = True
while deseja_emb:
    embaralhar = input('deseja embaralhar(s/n)?: \n').lower()
    if embaralhar == 's':
        embaralhar = True
        deseja_emb = False
    elif embaralhar == 'n':
        embaralhar = False
        deseja_emb = False
    else:
        print('por favor, decida se quer ou não embaralhar.')

baralho = gerar_baralho(qtde_baralhos, coringas, embaralhar)
while True:
    if qtde_jogadores * qtde_cartas > len(baralho):
        print('sentimos muito, mas o tamanho do baralho não comporta essa quantia de cartas')
        print('tente reduzir o numero de cartas por jogador ou o numero de jogadores!')
        qtde_jogadores = validar_termos('quantos jogadores desejam jogar? \n')
        qtde_cartas = validar_termos('quantas cartas cada jogador deve receber? : \n')
    else:
        break

jogadores = []
i = 1
for _ in range(qtde_jogadores):
    nome = input(f'escreva o nome do jogador {i}: \n').title()
    i += 1
    jogadores.append(nome)

mostrar_baralho(baralho)
calcular_baralho(baralho, qtde_cartas, qtde_jogadores)
mostrar_jogadores(qtde_cartas, jogadores, baralho)
