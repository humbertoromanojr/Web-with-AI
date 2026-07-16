# Importa a classe FastAPI do framework FastAPI
from fastapi import FastAPI

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define a rota GET para o endpoint raiz "/"
@app.get("/")
def hello_world():
    # Retorna uma mensagem de boas-vindas em formato JSON
    return {"mensagem": "Olá, mundo! 🌍"}


# Define a rota GET para o endpoint "/bands"
@app.get("/bands")
def list_bands():
    # Retorna uma lista com bands de exemplo
    return [
        {"id": 1, "nome": "Sarcofago", "categoria": "AMÉRICA DO SUL"},
        {"id": 2, "nome": "Slayer", "categoria": "AMÉRICA DO NORTE"},
    ]
