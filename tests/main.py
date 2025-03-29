import pytest
import os

if __name__ == "__main__":
    # Obtém o diretório base da pasta 'tests'
    test_dir = os.path.dirname(os.path.abspath(__file__))

    # Roda o pytest garantindo que ele encontre os testes dentro das subpastas
    pytest.main([test_dir])