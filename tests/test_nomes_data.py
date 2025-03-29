from app.data import nomes_data

def test_nomes_masculinos_nao_vazio():
    assert len(nomes_data.nomes_masculinos) > 0

def test_nomes_femininos_nao_vazio():
    assert len(nomes_data.nomes_femininos) > 0

def test_sobrenomes_nao_vazio():
    assert len(nomes_data.sobrenomes) > 0

def test_nomes_masculinos_sao_strings():
    assert all(isinstance(nome, str) for nome in nomes_data.nomes_masculinos)

def test_nomes_femininos_sao_strings():
    assert all(isinstance(nome, str) for nome in nomes_data.nomes_femininos)

def test_sobrenomes_sao_strings():
    assert all(isinstance(sobrenome, str) for sobrenome in nomes_data.sobrenomes)