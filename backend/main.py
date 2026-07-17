# Importações necessárias
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Configura o middleware CORS para aceitar requisições de qualquer origem
# Isso permite que o frontend acesse a API sem restrições de segurança
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define o caminho absoluto da pasta de imagens
# Isso garante que o servidor encontre a pasta independente de onde for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "images")

# Lista de figurinhas (bandas) com informações e URL da imagem
# Cada imagem_url aponta para "/images/{id}/imagem"
figurinhas = [
    {"id": 1, "nome": "Chthonic", "categoria": "ASIA", "imagem_url": "/images/1/imagem"},
    {"id": 2, "nome": "Sigh", "categoria": "ASIA", "imagem_url": "/images/2/imagem"},
    {"id": 3, "nome": "Bloodywood", "categoria": "ASIA", "imagem_url": "/images/3/imagem"},
    {"id": 4, "nome": "Abigail", "categoria": "ASIA", "imagem_url": "/images/4/imagem"},
    {"id": 5, "nome": "Demonic Resurrection", "categoria": "ASIA", "imagem_url": "/images/5/imagem"},
    {"id": 6, "nome": "Skinflint", "categoria": "AFRICA", "imagem_url": "/images/6/imagem"},
    {"id": 7, "nome": "Myrath", "categoria": "AFRICA", "imagem_url": "/images/7/imagem"},
    {"id": 8, "nome": "Overthrust", "categoria": "AFRICA", "imagem_url": "/images/8/imagem"},
    {"id": 9, "nome": "Dark Suburb", "categoria": "AFRICA", "imagem_url": "/images/9/imagem"},
    {"id": 10, "nome": "Imperious Malevolence", "categoria": "AFRICA", "imagem_url": "/images/10/imagem"},
    {"id": 11, "nome": "Gorguts", "categoria": "AMÉRICA DO NORTE", "imagem_url": "/images/11/imagem"},
    {"id": 12, "nome": "Death", "categoria": "AMÉRICA DO NORTE", "imagem_url": "/images/12/imagem"},
    {"id": 13, "nome": "Slayer", "categoria": "AMÉRICA DO NORTE", "imagem_url": "/images/13/imagem"},
    {"id": 14, "nome": "Opeth", "categoria": "EUROPA", "imagem_url": "/images/14/imagem"},
    {"id": 15, "nome": "Meshuggah", "categoria": "EUROPA", "imagem_url": "/images/15/imagem"},
    {"id": 16, "nome": "Sarcofago", "categoria": "AMÉRICA DO SUL", "imagem_url": "/images/16/imagem"},
    {"id": 17, "nome": "Krisiun", "categoria": "AMÉRICA DO SUL", "imagem_url": "/images/17/imagem"},
    {"id": 18, "nome": "Sepultura", "categoria": "AMÉRICA DO SUL", "imagem_url": "/images/18/imagem"},
    {"id": 19, "nome": "Reencarnacion", "categoria": "AMÉRICA DO SUL", "imagem_url": "/images/19/imagem"},
    {"id": 20, "nome": "Inquisition", "categoria": "AMÉRICA DO SUL", "imagem_url": "/images/20/imagem"},
    {"id": 21, "nome": "Nekropsychotic", "categoria": "AMÉRICA DO SUL", "imagem_url": "/images/21/imagem"},
    {"id": 22, "nome": "Nunatak", "categoria": "ANTÁRTIDA", "imagem_url": "/images/22/imagem"},
    {"id": 23, "nome": "Icebreaker", "categoria": "ANTÁRTIDA", "imagem_url": "/images/23/imagem"},
    {"id": 24, "nome": "Penguin Death", "categoria": "ANTÁRTIDA", "imagem_url": "/images/24/imagem"},
    {"id": 25, "nome": "90 South", "categoria": "ANTÁRTIDA", "imagem_url": "/images/25/imagem"},
    {"id": 26, "nome": "Bathory", "categoria": "EUROPA", "imagem_url": "/images/26/imagem"},
    {"id": 27, "nome": "Celtic Frost", "categoria": "EUROPA", "imagem_url": "/images/27/imagem"},
    {"id": 28, "nome": "Carcass", "categoria": "EUROPA", "imagem_url": "/images/28/imagem"},
    {"id": 29, "nome": "Emperor", "categoria": "EUROPA", "imagem_url": "/images/29/imagem"},
    {"id": 30, "nome": "Behemoth", "categoria": "EUROPA", "imagem_url": "/images/30/imagem"},
    {"id": 31, "nome": "Mortification", "categoria": "OCEANIA", "imagem_url": "/images/31/imagem"},
    {"id": 32, "nome": "Psycroptic", "categoria": "OCEANIA", "imagem_url": "/images/32/imagem"},
    {"id": 33, "nome": "Disentomb", "categoria": "OCEANIA", "imagem_url": "/images/33/imagem"},
    {"id": 34, "nome": "Alchemist", "categoria": "OCEANIA", "imagem_url": "/images/34/imagem"},
    {"id": 35, "nome": "Ne Obliviscaris", "categoria": "OCEANIA", "imagem_url": "/images/35/imagem"},
]


# Define a rota GET para o endpoint "/bands"
# Retorna a lista completa de figurinhas
@app.get("/bands")
def list_bands():
    return figurinhas


# Define a rota GET para o endpoint "/images/{id}/imagem"
# Busca e retorna a imagem da banda pelo id
@app.get("/images/{id}/imagem")
def get_band_image(id: int):
    # Monta o padrão de busca com o id formatado com 2 dígitos
    # O padrão "{id:02d}[!0-9]*" encontra arquivos que começam com o id
    # e não são seguidos por mais dígitos (ex: "01-chthonic.jpg" mas não "011-algo.jpg")
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")

    # Usa glob para encontrar arquivos que correspondem ao padrão
    arquivos = glob.glob(padrao)

    # Se nenhum arquivo foi encontrado, retorna erro 404
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    # Retorna o primeiro arquivo encontrado como resposta
    return FileResponse(arquivos[0])
