# API Geradora de Nomes

## Descrição
A **API Geradora de Nomes** é uma aplicação desenvolvida com **FastAPI** para gerar nomes aleatórios, nomes completos e nomes categorizados por gênero (masculino e feminino).

## Como acessar

### URL da API
A API está disponível localmente no seguinte endereço: http://127.0.0.1:8000


### Swagger UI
A documentação interativa da API, onde você pode testar os endpoints diretamente, pode ser acessada no seguinte endereço:
http://127.0.0.1:8000/docs


---

## Personalização da Quantidade de Nomes
Você pode especificar a quantidade de nomes a ser gerada utilizando o parâmetro **qtd** nos endpoints. Caso o parâmetro não seja informado, a API irá gerar apenas **1 nome** por padrão.

---

## Bibliotecas Utilizadas

- **FastAPI**: Framework para criação da API.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **random**: Biblioteca padrão do Python usada para gerar nomes aleatórios.

---

Isso é tudo! Basta seguir as instruções de execução para rodar a API localmente e acessar os endpoints através do Swagger.

---