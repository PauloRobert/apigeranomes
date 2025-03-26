# app/main.py
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.routes import nomes

app = FastAPI(title="API Geradora de Nomes",
              description="API para gerar nomes aleatórios",
              version="1.0")

app.include_router(nomes.router)

# Criando uma rota raiz para redirecionar para o Swagger UI
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")  # Redireciona automaticamente para a documentação do Swagger


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Correto para Render