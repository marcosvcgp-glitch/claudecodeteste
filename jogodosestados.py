estados={
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio De Janeiro": "Rio De Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}
print('-'*15)
print('Jogo dos Estados! \nao aparecer um estado na tela, complete com a capital! ')
total=0
i=0
for estado in estados:
    print('caso queira encerrar o jogo, digite "Encerre"')
    chute=input(f'qual a capital do estado {estado}: \n').title()
    if chute == 'Encerre':
        break
    elif chute == estados[estado]:
        i+=1
        total +=1
        print(f'Parabéns! Você acertou!')
    else:
        total+=1
        print(f'Você errou! A capital correta é {estados[estado]}')
porcentagem= (i/total)*100
print(f'você acertou {i} capitas! isso representa {porcentagem:.2f}%!')
