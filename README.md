# Alura Album - Web with AI

Album interativo inspirado em figurinhas de copa do mundo, utilizado como projeto de estudo de programação com apoio de IA. O tema atual apresenta **bandas de Death e Black Metal dos sete continentes**.

## Objetivo

Demonstrar como programar um projeto web completo (frontend + backend) com auxílio de IA, desde a estruturação do HTML e CSS até a lógica de interação em JavaScript e integração com API.

## Estrutura do projeto

```
Web-with-AI/
├── frontend/
│   ├── index.html      # Estrutura principal do álbum
│   ├── style.css       # Estilos e responsividade
│   ├── app.js          # Lógica de virada de páginas, som e API
│   └── index_bkp.html  # Backup do HTML original (tema tech)
└── README.md
```

## Arquivos do Frontend

### `index.html`

Pagina principal do album, construida com a biblioteca [page-flip](https://github.com/nickel2/nickel2.github.io). Estrutura:

| Pagina | Conteudo |
|--------|----------|
| Capa | Capa com efeito glitch, esfera 3D e mini-cards flutuantes |
| Pag. 1 | Asia - 5 bandas |
| Pag. 2 | Africa - 5 bandas |
| Pag. 3 | America do Norte - 5 bandas |
| Pag. 4 | America do Sul - 5 bandas |
| Pag. 5 | Antartida - 5 bandas |
| Pag. 6 | Europa - 5 bandas |
| Pag. 7 | Oceania - 5 bandas |
| Pag. em branco | Necessaria para manter total par de paginas (requisito do `showCover: true`) |
| Contracapa | Resumo e codigo de barras |

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
- `GET /figurinhas` retorna JSON com id, nome e imagem_url
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
