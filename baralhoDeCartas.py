def gerarBaralho(qtdeBaralhos=1 , coringas=False,embaralhar=False):
    # cria o número necessario de baralhos e embaralha
    baralho=[]
    naipes = ["♠", "♥", "♦", "♣"]
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for _ in range(qtdeBaralhos):
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

def mostrarBaralho(baralho):
    # printa o baralhon de 13 em 13 e mostra o tamanho total
    copia = baralho.copy()
    print(f'O baralho tem {len(baralho)} cartas')
    while copia:
        print(copia[:13])
        del copia[:13]

def distribuir(baralho, qtdeCartas, qtdejogadores=2):
    # calcula a quantidade de cartas necessárias pra cada jogador 
    resto=len(baralho)%(qtdejogadores*qtdeCartas)
    qtde= len(baralho)//(qtdejogadores*qtdeCartas)
    print(f'cada jogador deve receber {qtde} cartas')
    print(f'ainda existem {resto} cartas na mesa')
    return qtde, resto

def mostrarJogadores(qtde, jogadores, baralho):
    # mostra  amão de cada um dos jogadores.
    for jogador in jogadores:
        maoDoJogador = baralho[:qtde]
        del baralho[:qtde]
        print(f'a mão do {jogador} é {" ".join(maoDoJogador)}')

# selção automatica de baralhos: criarie um dicionário com os cinco jogos mais popilares
# de cartas para que a seleção seja mais simplificada.

jogosPadrão = {
        'Truco' :{
            'qtdeJogadoresMAX' : 4,
            'qtdeJogadoresMIN' : 2,
            'qtdeCartas' : 3,
            'qtdeBaralhos' : 1,
            'coringas' : False
        },

        'Buraco' : {
            'qtdeJogadoresMAX' : 4,
            'qtdeJogadoresMIN' : 2,
            'qtdeCartas': 11,
            'qtdeBaralhos' : 2,
            'coringas' : True
        },

        'Poker' : {
            'qtdeJogadoresMAX' : 10,
            'qtdeJogadoresMIN':  2,
            'qtdeCartas' : 2,
            'qtdeBaralhos' : 1,
            'coringas' : False
        },

        'Blackjack': {
        'qtdeJogadoresMAX': 7,
        'qtdeJogadoresMIN': 1,
        'qtdeCartas': 2,
        'qtdeBaralhos': 1,
        'coringas': False
    },

    'Paciencia': {
        'qtdeJogadoresMAX': 1,
        'qtdeJogadoresMIN': 1,
        'qtdeCartas': 0,
        'qtdeBaralhos': 1,
        'coringas': False
    },

    'Canastra': {
        'qtdeJogadoresMAX': 4,
        'qtdeJogadoresMIN': 2,
        'qtdeCartas': 11,
        'qtdeBaralhos': 2,
        'coringas': True
    },
}


print('-'*30)

print('SIMULADOR DE BARALHO')

print('-'*30)

validação=True
while validação:
    print('deseja fazer a seleção com regras arbitrárias ou jogar um jogo já existente?')
    modo=input('modo manual ou modo automático?(m/a): \n').lower()
    if modo in ('m','a'):
        validação=False
    else:
        print('por favor escolha um modo de seleção!')