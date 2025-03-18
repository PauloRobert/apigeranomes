from fastapi import APIRouter, Query
from app.services import gerador_nomes
from app.data import nomes_data

router = APIRouter()

@router.get("/gerarnome", summary="Gerar Nome Aleatório")
def gerar_nome(qtd: int = Query(1)):
    return {"nomes": gerador_nomes.gerar_nomes(qtd, nomes_data.nomes_masculinos + nomes_data.nomes_femininos)}

@router.get("/gerarnomecompleto", summary="Gerar Nome Completo")
def gerar_nome_completo(qtd: int = Query(1)):
    return {"nomes_completos": gerador_nomes.gerar_nomes_completos(qtd)}

@router.get("/gerarnomemulher", summary="Gerar Nome Feminino")
def gerar_nome_mulher(qtd: int = Query(1)):
    return {"nomes_femininos": gerador_nomes.gerar_nomes(qtd, nomes_data.nomes_femininos)}

@router.get("/gerarnomehomem", summary="Gerar Nome Masculino")
def gerar_nome_homem(qtd: int = Query(1)):
    return {"nomes_masculinos": gerador_nomes.gerar_nomes(qtd, nomes_data.nomes_masculinos)}