# Importa a classe FastAPI do framework FastAPI
from fastapi import FastAPI

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define a rota GET para o endpoint raiz "/"
@app.get("/")
def hello_world():
    # Retorna uma mensagem de boas-vindas em formato JSON
    return {"mensagem": "Olá, mundo! 🌍"}
