import pytest
import os
import sys

# Adiciona o diretório apigeranomes ao sys.path para garantir que o Python o encontre
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    # Obtém o diretório base da pasta 'tests'
    test_dir = os.path.dirname(os.path.abspath(__file__))

    # Define o caminho para o arquivo coverage.xml
    coverage_path = os.path.join(os.getcwd(), "coverage.xml")

    # Executa os testes e gera o relatório de cobertura em XML
    pytest.main([
        test_dir,
        "--cov=apigeranomes",  # Certifique-se de que o nome do pacote está correto
        "--cov-report=term-missing",  # Exibe no terminal os arquivos sem cobertura
        f"--cov-report=xml:{coverage_path}"  # Gera o arquivo coverage.xml
    ])