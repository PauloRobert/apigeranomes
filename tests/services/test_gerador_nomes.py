from app.services import gerador_nomes
from app.data import nomes_data

def test_gerar_nome_aleatorio():
    nome = gerador_nomes.gerar_nome_aleatorio(nomes_data.nomes_masculinos)
    assert isinstance(nome, str)
    assert nome in nomes_data.nomes_masculinos

def test_gerar_nomes():
    qtd = 5
    nomes = gerador_nomes.gerar_nomes(qtd, nomes_data.nomes_masculinos)
    assert len(nomes) == qtd
    assert all(nome in nomes_data.nomes_masculinos for nome in nomes)

def test_gerar_nomes_completos():
    qtd = 3
    nomes_completos = gerador_nomes.gerar_nomes_completos(qtd)
    assert len(nomes_completos) == qtd
    assert all(" " in nome for nome in nomes_completos)  # Nome + Sobrenome