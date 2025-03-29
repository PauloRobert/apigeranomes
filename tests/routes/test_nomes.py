from fastapi.testclient import TestClient
from app.main import app  # Importa a aplicação FastAPI

client = TestClient(app)  # Criando o cliente de testes

def test_gerar_nome_completo():
    response = client.get("/gerarnomecompleto?qtd=3")
    assert response.status_code == 200
    data = response.json()

    assert "nomes" in data
    assert "quantidade" in data
    assert len(data["nomes"]) == 3
    assert all("categoria" in nome and "nome" in nome for nome in data["nomes"])

def test_gerar_nome_mulher():
    response = client.get("/gerarnomemulher?qtd=1")
    assert response.status_code == 200
    data = response.json()

    assert "nomes" in data
    assert "quantidade" in data
    assert len(data["nomes"]) == 1
    assert data["nomes"][0]["categoria"] == "Feminino"

def test_gerar_nome_homem():
    response = client.get("/gerarnomehomem?qtd=1")
    assert response.status_code == 200
    data = response.json()

    assert "nomes" in data
    assert "quantidade" in data
    assert len(data["nomes"]) == 1
    assert data["nomes"][0]["categoria"] == "Masculino"