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

def distribuirBaralho(baralho, qtdeCartas, qtdejogadores=2):
    # calcula a quantidade de cartas necessárias pra cada jogador 
    resto=len(baralho)-(qtdejogadores*qtdeCartas)
    print(f'cada jogador deve receber {qtdeCartas} cartas')
    print(f'ainda existem {resto} cartas na mesa')

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

listaJogos=('Canastra', 'Paciencia','Truco','Blackjack','Poker','Buraco')

validarCoringa =True

validarJogadores= True

print('-'*30)

print('SIMULADOR DE BARALHO')

print('-'*30)

# seletor de modo, aqui o usuário deve selecionar se deseja
# usar regras de um jogo existente ou um inédito.

validação=True
while validação:
    print('deseja fazer a seleção com regras arbitrárias ou jogar um jogo já existente?')
    modo=input('modo manual ou modo automático?(m/a): \n').lower()
    if modo in ('m','a'):
        validação=False
    else:
        print('por favor escolha um modo de seleção!')
if modo == 'a':
    jogo=input(f'por favor, selceione um jogo da lista: \n{listaJogos} :\n').capitalize()
    if jogo not in listaJogos:
        print('infelizmente ainda não possuímos esse jogo em nosso banco de jogos!')
        print('por favor selecione as regras de maneira manual!')
    else:
        qtdeJogadoresMAX = jogosPadrão[jogo]['qtdeJogadoresMAX']
        qtdeJogadoresMIN = jogosPadrão[jogo]['qtdeJogadoresMIN']
        qtdeCartas = jogosPadrão[jogo]['qtdeCartas']
        qtdeBaralhos = jogosPadrão[jogo]['qtdeBaralhos']
        coringas = jogosPadrão[jogo]['coringas']
        while validarJogadores:
            qtdejogadores=int(input('coloque a quantidade de jogadores que desejam jogar: \n'))
            if qtdejogadores > qtdeJogadoresMAX or qtdejogadores < qtdeJogadoresMIN:
                print(f'a quntidade de jogadores deve estar entre {qtdeJogadoresMIN} e {qtdeJogadoresMAX}')
            else:
                validarJogadores = False
else:
        qtdeCartas = int(input('quantas cartas cada jogador deve receber? : \n'))

        qtdeBaralhos = int(input('quantos baralhos desejam usar? : \n'))

        while validarCoringa:
            coringas = input('deseja usar coringas(s/n)? : \n').lower()
            if coringas  == 'n':
                coringas = False
                validarCoringa=False
            else: 
                coringas = True
                validarCoringa=False
        
        qtdejogadores= int(input('quantos jogadores desejam jogar? \n'))

jogadores=[]
i=1
for _ in range(qtdejogadores):
    nome=input(f'escreva o nome do jogador {i}: \n').title()
    i+=1
    jogadores.append(nome)

desejaEmb= True
while desejaEmb:
    embaralhar=input('deseja emaralhar(s/n)?: \n').lower()
    if embaralhar == 's':
        embaralhar = True
        desejaEmb = False
    elif embaralhar == 'n':
        embaralhar=False
        desejaEmb=False
    else:
        print('por favor, decida se quer ou não embaralhar.')

baralho= gerarBaralho(qtdeBaralhos, coringas, embaralhar)
mostrarBaralho(baralho)
distribuirBaralho(baralho,qtdeCartas,qtdejogadores)
mostrarJogadores(qtdeCartas, jogadores, baralho)