vogais={
"a":0,
"e":0,
"i":0,
"o":0,
"u":0
}

texto=input("insira o seu texto: ").lower()

for letra in texto:
    if letra in vogais:
        vogais[letra]+=1

for x,v  in vogais.items():
    print(f'{x} -> {v}')

total=sum(vogais.values())

print(f'o total foi {total}')
print('>>>>>>>>>>>>')