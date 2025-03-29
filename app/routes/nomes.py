from fastapi import APIRouter, Query
from app.services import gerador_nomes
from app.data import nomes_data

router = APIRouter()

@router.get("/gerarnome", summary="Gerar Nome Aleatório")
def gerar_nome(qtd: int = Query(1)):
    nomes = gerador_nomes.gerar_nomes(qtd, nomes_data.nomes_masculinos + nomes_data.nomes_femininos)
    categorias = ["Masculino" if nome in nomes_data.nomes_masculinos else "Feminino" for nome in nomes]

    return {
        "quantidade": len(nomes),
        "nomes": [{"nome": nome, "categoria": categoria} for nome, categoria in zip(nomes, categorias)]
    }

@router.get("/gerarnomecompleto", summary="Gerar Nome Completo")
def gerar_nome_completo(qtd: int = Query(1)):
    nomes_completos = []

    for _ in range(qtd):
        primeiro_nome = gerador_nomes.gerar_nome_aleatorio(nomes_data.nomes_masculinos + nomes_data.nomes_femininos)
        sobrenome = gerador_nomes.gerar_nome_aleatorio(nomes_data.sobrenomes)

        categoria = "Masculino" if primeiro_nome in nomes_data.nomes_masculinos else "Feminino"
        nome_completo = f"{primeiro_nome} {sobrenome}"

        nomes_completos.append({"nome": nome_completo, "categoria": categoria})

    return {
        "quantidade": len(nomes_completos),
        "nomes": nomes_completos
    }

@router.get("/gerarnomemulher", summary="Gerar Nome Feminino")
def gerar_nome_mulher(qtd: int = Query(1)):
    nomes = gerador_nomes.gerar_nomes(qtd, nomes_data.nomes_femininos)

    return {
        "quantidade": len(nomes),
        "nomes": [{"nome": nome, "categoria": "Feminino"} for nome in nomes]
    }

@router.get("/gerarnomehomem", summary="Gerar Nome Masculino")
def gerar_nome_homem(qtd: int = Query(1)):
    nomes = gerador_nomes.gerar_nomes(qtd, nomes_data.nomes_masculinos)

    return {
        "quantidade": len(nomes),
        "nomes": [{"nome": nome, "categoria": "Masculino"} for nome in nomes]
    }