<h1 align="center">
  <img src="https://drive.google.com/uc?export=view&id=1LIANYV5KFDXVq1-5dOIakSCIgZzUlAeH" alt="" width="100%" border="0" />
<br>

# The Web Architecture with AI Immersion

</h1>

> Status from Project: <img src="https://drive.google.com/uc?export=view&id=1Tak2fjuusuwdzNI_rwhPqLHGVLVKNTm1" alt="" width="32" border="0" /> F I N I S H E D <img src="https://drive.google.com/uc?export=view&id=1Tak2fjuusuwdzNI_rwhPqLHGVLVKNTm1" alt="" width="32" border="0" />

## Shields

![Badge](https://img.shields.io/github/issues/humbertoromanojr/Web-with-AI?logo=visual-studio-code&style=plastic&logo=appveyor)
![Badge](https://img.shields.io/github/forks/humbertoromanojr/Web-with-AI)
![Badge](https://img.shields.io/github/stars/humbertoromanojr/Web-with-AI)
![Badge](https://img.shields.io/github/license/humbertoromanojr/Web-with-AI)
![Badge](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fhumbertoromanojr%2FWeb-with-AI)

## IAs

- [Antigravity IDE](https://antigravity.google/product/antigravity-ide)
- [Opencode IDE](https://opencode.ai/brand)

## Libraries

- [Fastapi](https://fastapi.tiangolo.com/)
- [Python](https://www.python.org/downloads/)

## Demonstration

<h2 align="center">
  <img src="https://drive.google.com/uc?export=view&id=1Bg-PMWDtcxgFb1ane0pdK7Akht9Eto0V" alt="" width="100%" border="0" />
</h2>

<div align="center">
  <img src="https://drive.google.com/uc?export=view&id=" alt="" width="100%" border="0" />
</div>
<br />

## Frontend

Prompts <br />
`No arquivo @index.html da pasta /frontend tem seis páginas de conteúdo, alterar e adiciona mais uma página que siga a arquitetura, para ter sete páginas, para conter os sete continentes: Ásia, África, América do Norte, América do Sul, Antártida, Europa e Oceania, com isso pode trocar os continentes pelos nomes que contem "tech-badge" para os "continents-badge" e nos "page-title" alterar para as cinco bandas de Death e Black Metal que eu irei escolher, só altera para as cinco bandas, exemplo: "Cinco bandas Asiáticas".` <br />

`alterar a contracapa para virar como as outras páginas, está sem o click que vira igual a capa, corrigir a @index.html na pasta /frontend e se precisar, alterar também o arquivo @app.js para poder fazer o flip a index.html`<br />

fix bug contracapa<br />
`verifica o arquivo o arquivo @frontend/index_bkp.html e altera a contracapa do arquivo @frontend/index.html e se precisar alterar o arquivo @frontend/app.js`<br />

`Crie um readme.md do projeto que explique o seu objetivos e as funcionalidades dos arquivos envolvidos da pasta /frontend e gere o arquivo na pasta raiz`<br />

Clone project to repository:<br />
<img src="https://drive.google.com/uc?export=view&id=16QqYlur8qtl5ao_XyEb4IthGyveQmELo" alt="" width="22" border="0" />
git clone `https://github.com/humbertoromanojr/Web-with-AI`

<img src="https://drive.google.com/uc?export=view&id=16QqYlur8qtl5ao_XyEb4IthGyveQmELo" alt="" width="22" border="0" /> Go to `Web-with-AI/frontend` folder <br />

##

## API - Backend

Enabling a Python virtual machine on Windows 11<br />
`C:\...\Web-with-AI\backend\venv> Scripts\Activate.ps1`<br />
`(venv) C:\...\Web-with-AI\backend>`<br />

Install FastAPI<br />
`pip install fastapi`<br /><br />

Prompts <br />

- `instale o uvicorn na venv deste projeto` <br /><br />
- `Você vai criar o primeiro servidor de uma API de álbum de figurinhas.
  <br />
  Crie um arquivo main.py com um servidor FastAPI que tenha apenas 1 endpoint:
  <br />
  1.  GET "/" → retorna o JSON {"mensagem": "Olá, mundo! 🌍"}
      (use uma função chamada hello_world)

  Requisitos:<br />

  01 - Use apenas Python com FastAPI (import: from fastapi import FastAPI)<br />
  02 - Crie a aplicação com app = FastAPI()<br />
  03 - Adicione comentários em português explicando cada parte<br />
  04 - Não adicione nenhum outro endpoint<br />
  05 - Você vai olhar o python dentro da pasta venv` <br /><br />

- `alterar as cores na pasta  /frontend/style.css o arquivo style.css as cores em :root para ser em cores preto para vermelho, um degrade de preto para vermelho`<br />

Prompt: Create the /bandas endpoint<br />

- `1. Evolua o servidor da API de álbum de figurinhas para também servir
  as imagens das bandas como arquivos estáticos.<br />

  Atualize o arquivo main.py com um servidor FastAPI que:<br />
  1.  Use a aplicação com app = FastAPI()<br />

  2.  Defina o caminho absoluto da pasta de imagens (para o servidor encontrar
      a pasta independente de onde for executado):<br />
      PASTA_BASE = os.path.dirname(os.path.abspath(**file**))
      PASTA_IMAGENS = os.path.join(PASTA_BASE, "bands")

  3.  Configure os arquivos estáticos: "monte" a pasta PASTA_IMAGENS na rota "/images"
      usando StaticFiles, com name="images".<br />
      Assim, "bands/01-Chthonic.jpg" fica acessível em "/images/01-Chthonic.jpg".<br />

  4.  Tenha uma lista chamada "figurinhas" com 2 itens, cada um com os campos
      id, nome, categoria e imagem_url:<br />
      - {id: 1, name: "Chthonic", category: "ASIA", imagem_url: "/images/01-Chthonic.jpg"}<br />
      - {id: 2, name: "Sigh", category: "ASIA", imagem_url: "/images/02-Sigh.jpg"}<br />

  5.  Tenha apenas um endpoint: GET "/bands" (função list_bands)
      que retorna a lista de bandas.<br />

  Requisitos:<br />

  01 - Use Python com FastAPI<br />
  02 - Adicione comentários em português explicando cada parte<br />
  03 - Imports necessários:<br />
  from fastapi import FastAPI
  from fastapi.staticfiles import StaticFiles
  import os
  `<br />

- `Você vai criar a versão final do servidor da API de álbum de bandas. Ele precisa liberar acesso para o frontend (CORS), listar as figurinhas e entregar a imagem de cada uma por um endpoint próprio.<br />

  Crie um arquivo main.py com um servidor FastAPI que:<br />

  Configure o middleware CORS para aceitar requisições de qualquer origem<br />

  Defina caminhos absolutos para a pasta de imagens usando: PASTA_BASE = os.path.dirname(os.path.abspath(file)) PASTA_IMAGENS = os.path.join(PASTA_BASE, "images")<br />

  Crie uma lista chamada figurinhas com as 35 figurinhas, cada uma com: id, nome, categoria, imagem_url O imagem_url deve apontar para "/images/{id}/imagem" Comente as figurinhas que ainda não estão disponíveis (ex: ids 3, 4, 5...) Deixe ativas apenas as figurinhas cujas imagens existem na pasta images/<br />

  Crie o endpoint GET "/bands" que retorna a lista<br />

  Crie o endpoint GET "/bands/{id}/nome da imagem que esta na pasta images/" que:<br />

  Usa glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]\*" na pasta images/<br />
  Retorna 404 se não encontrar<br />
  Retorna FileResponse com o arquivo encontrado<br />
  Imports necessários: from fastapi import FastAPI, HTTPException from fastapi.responses import FileResponse from fastapi.middleware.cors import CORSMiddleware import os import glob`<br />

`Agora link para o arquivo da pasta frontend/index.html possa mostrar as figurinhas armazenadas na pasta backend/images/`<br /><br />

<img src="https://drive.google.com/uc?export=view&id=16QqYlur8qtl5ao_XyEb4IthGyveQmELo" alt="" width="22" border="0" /> Go to `Web-with-AI/backend` folder <br />

<img src="https://drive.google.com/uc?export=view&id=16QqYlur8qtl5ao_XyEb4IthGyveQmELo" alt="" width="22" border="0" /> Run server `uvicorn main:app --reload` <br />

## Sources

- https://www.youtube.com/watch?v=oSkBkYxr1sU
- https://wallpaperaccess.com

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/licenses/MIT) page for details.

## Author

<img src="https://avatars1.githubusercontent.com/u/6500430?s=460&u=42d7e22fa1c77b061505fe1cfc3fcaa3e2a4d1e5&v=4" width="80" alt="linkedin.com/in/junior-dev" />
<img src="https://drive.google.com/uc?export=view&id=1-y6rFrn4uqPfLx3nuUTXh14OeRGSZzHu" alt="" width="42" border="0" />
:guitar: Humberto Jr :guitar:
<br />

LinkedIn: linkedin.com/in/humbertoromanojr <br />
GitLab: gitlab.com/humbertoromanojr <br />
<img src="https://drive.google.com/uc?export=view&id=160InxEPlK0IynTEGEmQJDETo_8grncjI" alt="" width="22" border="0" />: astronomi@gmail.com <br />
<br />

Made with <img src="https://drive.google.com/uc?export=view&id=1bb7UVQdQc1QpCIGqaI2bh4YdAn6Ihah-" alt="" width="22" border="0" /> and lots of animation by :guitar: Humberto Jr :guitar:

##

<img src="https://drive.google.com/uc?export=view&id=1lAPQY5CLSU4ofNI7-kTS8SMtKo6NZt-B" alt="" width="22" border="0" /> Read more below <img src="https://drive.google.com/uc?export=view&id=1lAPQY5CLSU4ofNI7-kTS8SMtKo6NZt-B" alt="" width="22" border="0" />

##

## Alura Album - Web with AI

Album interativo inspirado em figurinhas de copa do mundo, utilizado como projeto de estudo de programação com apoio de IA. O tema atual apresenta **bandas de Death e Black Metal dos sete continentes**.

## Objetivo

Demonstrar como programar um projeto web completo (frontend + backend) com auxílio de IA, desde a estruturação do HTML e CSS até a lógica de interação em JavaScript e integração com API.

## Estrutura do projeto

```
Web-with-AI/
├── backend/
│   ├── images/
├── frontend/
│   ├── index.html      # Estrutura principal do álbum
│   ├── style.css       # Estilos e responsividade
│   ├── app.js          # Lógica de virada de páginas, som e API
└── README.md
```

## Arquivos do Frontend

### `index.html`

Pagina principal do album, construida com a biblioteca [page-flip](https://github.com/nickel2/nickel2.github.io). Estrutura:

| Pagina         | Content                                                                      |
| -------------- | ---------------------------------------------------------------------------- |
| Capa           | Capa com efeito glitch, esfera 3D e mini-cards flutuantes                    |
| Pag. 1         | Asia - 5 bandas                                                              |
| Pag. 2         | Africa - 5 bandas                                                            |
| Pag. 3         | America do Norte - 5 bandas                                                  |
| Pag. 4         | America do Sul - 5 bandas                                                    |
| Pag. 5         | Antartida - 5 bandas                                                         |
| Pag. 6         | Europa - 5 bandas                                                            |
| Pag. 7         | Oceania - 5 bandas                                                           |
| Pag. em branco | Necessaria para manter total par de paginas (requisito do `showCover: true`) |
| Contracapa     | Resumo e codigo de barras                                                    |

Cada pagina de continente possui 5 slots de figurinhas (`sticker-slot`) com numeracao sequencial (#01 a #35). Os slots estao com placeholders prontos para preenchimento.

**Nota tecnica:** O page-flip com `showCover: true` exige numero **par** total de paginas. A pagina em branco apos Oceania e necessaria para que a contracapa seja posicionada corretamente.

### `style.css`

Estilos do album organizados em secoes:

- **Variaveis CSS** (`:root`): Paleta de cores (azuis, preto, branco)
- **Layout do album**: Viewport centralizado com perspectiva 3D
- **Paginas**: Dimensoes 550x800px, efeito de lombada (crease shadow), cursor de arraste
- **Badges**: `.tech-badge` (tema original) e `.continents-badge` (tema metal, fundo escuro)
- **Figurinhas**: Grid 2 colunas, slots com borda tracejada, animacao de entrada (`sticker-aparecer`), estado preenchido com imagem
- **Capa**: Efeito glitch no titulo, esfera 3D com aneis giratórios, mini-cards flutuantes, brilho animado no seal
- **Contracapa**: Gradiente, codigo de barras simulado
- **Responsivo**: Adaptacoes para 1200px (tablet) e 768px (mobile)

### `app.js`

Logica de interacao do album com 4 modulos principais:

#### 1. Inicializacao do PageFlip

Configuracao da biblioteca `St.PageFlip` com as opcoes:

- `showCover: true` - Capa exibida como pagina solta
- `useMouseEvents: false` - Eventos de mouse nativos desativados (usa logica customizada)
- `disableFlipByClick: true` - Virada por clique desativada (apenas arraste)
- `flippingTime: 800` - Transicao de 800ms

#### 2. Sistema de arraste customizado

Substitui os eventos nativos do library por um sistema proprio:

- Detecta `mousedown`/`touchstart` em cada pagina
- Calcula distancia do arraste (threshold de 10px para evitar cliques acidentais)
- Determina canto de origem baseado no indice da pagina (par = direito, impar = esquerdo)
- Usa `startUserTouch`, `userMove` e `userStop` da API do page-flip

#### 3. Efeito sonoro de virada

Gera som sintetizado de papel via Web Audio API:

- Ruído branco com envelope de volume (pico em 30% da duracao)
- Filtro bandpass com varredura dinamica (1500Hz -> 350Hz)
- Lowpass para suavizar artefatos digitais
- Botao de mute/unmute

#### 4. Integracao com API (`preencherFigurinhas`)

Funcao assincrona que busca figurinhas do backend FastAPI:

- `GET /bands` retorna JSON com id, nome e imagem_url
- Percorre os slots do HTML, extrai o numero (`#01` -> 1)
- Insere `<img>` no slot correspondente com animacao de entrada
- Trata erros de conexao silenciosamente (album funciona sem backend)

**Endpoint da API:** `http://localhost:8000` (configuravel via `API_BASE_URL`)

## Como executar

### Apenas o frontend (estatico)

Basta abrir `frontend/index.html` no navegador. As figurinhas ficarao vazias (placeholders) ja que o backend nao estara rodando.

### Com backend (Dia 3)

```bash
# Terminal 1 - Backend
cd backend/dia-3
uvicorn main:app --reload

# Terminal 2 - Frontend
# Abrir frontend/index.html no navegador
```

## Tecnologias

- **HTML5** - Estrutura semantica
- **CSS3** - Grid, flexbox, animacoes, CSS custom properties
- **JavaScript (ES6+)** - Async/await, Web Audio API, DOM manipulation
- **page-flip 2.0.7** - Biblioteca de viracao de paginas
- **FastAPI** (backend) - API REST para servir figurinhas
- **Google Fonts** - Inter e Outfit
