# app/main.py
from fastapi import FastAPI
from app.routes import nomes

app = FastAPI(title="API Geradora de Nomes",
              description="API para gerar nomes aleatórios",
              version="1.0")

app.include_router(nomes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)