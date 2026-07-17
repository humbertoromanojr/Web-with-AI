# Importações necessárias
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define o caminho absoluto da pasta de imagens
# Isso garante que o servidor encontre a pasta independente de onde for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "bands")

# Monta a pasta de imagens como arquivos estáticos na rota "/imgs"
# Assim, "bands/01-Chthonic.jpg" fica acessível em "/imgs/01-Chthonic.jpg"
app.mount("/images", StaticFiles(directory=PASTA_IMAGENS), name="images")

# Lista de figurinhas (bandas) com informações e URL da imagem
bands = [
    {
        "id": 1,
        "name": "Chthonic",
        "category": "ASIA",
        "imagem_url": "/images/01-Chthonic.jpg",
    },
    {
        "id": 2,
        "name": "Sigh",
        "category": "ASIA",
        "imagem_url": "/images/02-Sigh.jpg",
    },
]


# Define a rota GET para o endpoint "/bands"
@app.get("/bands")
def list_bands():
    # Retorna a lista completa de bandas
    return bands
