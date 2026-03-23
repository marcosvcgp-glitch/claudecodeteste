import pandas as pd

# Criando um DataFrame simples
dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "Idade": [25, 30, 22, 28],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba", "Salvador"]
}

df = pd.DataFrame(dados)

print("=== Tabela completa ===")
print(df)

print("\n=== Média de idade ===")
print(df["Idade"].mean())

print("\n=== Filtro: idade > 24 ===")
print(df[df["Idade"] > 24])
cle