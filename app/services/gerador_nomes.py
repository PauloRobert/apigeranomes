import random
from app.data import nomes_data

def gerar_nome_aleatorio(lista_nomes):
    return random.choice(lista_nomes)

def gerar_nomes(qtd, lista_nomes):
    return [gerar_nome_aleatorio(lista_nomes) for _ in range(qtd)]

def gerar_nomes_completos(qtd):
    return [f"{gerar_nome_aleatorio(nomes_data.nomes_masculinos + nomes_data.nomes_femininos)} {gerar_nome_aleatorio(nomes_data.sobrenomes)}" for _ in range(qtd)]