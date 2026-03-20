def gerarBaralho(qtde=1 , coringas=False,embaralhar=False):
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
    copia = baralho.copy()
    print(f'O baralho tem {len(baralho)} cartas')
    while copia:
        print(copia[:13])
        del copia[:13]

def distribuir(baralho, jogadores=2):














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