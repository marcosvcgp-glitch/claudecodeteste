def gerarBaralho(qtde=1 , coringas=False,embaralhar=False):
    #cria o número necessario de baralhos e embaralha
    baralho=[]
    naipes = ["♠", "♥", "♦", "♣"]
    valores = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    for _ in range(qtde):
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
    #printa o baralhon de 13 em 13 e mostra o tamanho total
    copia = baralho.copy()
    print(f'O baralho tem {len(baralho)} cartas')
    while copia:
        print(copia[:13])
        del copia[:13]

def distribuir(baralho, qtdCartas, jogadores=2):
    qtde=len(baralho)//(jogadores*qtdCartas)
    resto=len(baralho)%(jogadores*qtdCartas)
    print(f'cada jogador deve receber {qtde} cartas')
    print(f'ainda existem {resto} cartas na mesa')
    return qtde, resto

def mostrarJogadores(qtde, jogadores, baralho):
    for jogador in jogadores:
        maoDoJogador = baralho[:qtde]
        del baralho[:qtde]
        print(f'a mão do {jogador} é {" ".join(maoDoJogador)}')














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