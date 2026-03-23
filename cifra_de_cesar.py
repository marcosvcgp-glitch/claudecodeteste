print('-'*25)

print('CIFRA DE CÉSAR')

print('-'*25)

alfabeto='abcdefghijklmnopqrstuvwxyz'

ALFABETO='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

frase=input('coloque a frase que deseja codificar aqui: \n')

chave=int(input('coloque quantas chaves deseja mover as letras: \n'))

resultado=[]

for letra in frase:
    if letra in ALFABETO:
        indice=ALFABETO.index(letra)
        letra=ALFABETO[(indice+chave) %26]
        resultado.append(letra)
        
    elif letra in alfabeto:
        indice=alfabeto.index(letra)
        letra=alfabeto[(indice+chave) %26]
        resultado.append(letra)
        
    else: #acentos, ç, simbolos e sinais não se alteram 
        resultado.append(letra)
        continue
        
resultado="".join(resultado)

print('-'*25)

print(f'O seu texto secreto e cidificado: \n{resultado}')

print('-'*25)
