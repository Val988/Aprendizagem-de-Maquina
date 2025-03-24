import pandas as pd
import random

# Lista de frutas com duplicatas
frutas = ["maçã", "banana", "laranja", "uva", "maçã", "melão", "mamão", "banana"]

# Criar um conjunto para remover duplicatas
frutas_unicas = set(frutas)

# Gerar um dicionário com quantidades aleatórias
frutas_quantidade = {fruta: random.randint(0, 100) for fruta in frutas_unicas}

# Escrever no arquivo minhas_frutas.txt
with open("minhas_frutas.txt", "w") as arquivo:
    for fruta, quantidade in frutas_quantidade.items():
        arquivo.write(f"{fruta},{quantidade}\n")

# Ler o arquivo e armazenar os dados
dados = {}
with open("minhas_frutas.txt", "r") as arquivo:
    for linha in arquivo:
        fruta, quantidade = linha.strip().split(",")
        quantidade = int(quantidade)
        if fruta in dados:
            dados[fruta] += quantidade
        else:
            dados[fruta] = quantidade

# Criar DataFrame
df = pd.DataFrame(list(dados.items()), columns=["Fruta", "Quantidade"])

# Exibir o DataFrame
print(df)
