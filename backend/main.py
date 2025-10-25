# Arquivo principal da minha API. É aqui que o FastAPI vai brilhar #GlowUp
# Bora das importações das bibliotecas que instalei lá no requirements.txt
from fastapi import FastAPI
# o FastAPI usa pra permitir que outros sites ou aplicações façam requisições à tua API
from fastapi.middleware.cors import CORSMiddleware
# Puxar nossas rotas: health (teste) e podcast (geração de roteiro)
from routes import health, podcast

# Esse carinha é que estou chamando quando rodo 'uvicorn main:app', o app é a minha variável
app = FastAPI(
    title="PodCriar - Podcast Generator API",
    description="O coração do meu monolito, minha API que gera roteiro e audio",
    version="1.0.0"
)

# Configuração do CORS, meu porteiro que permite que o frontend acesse a API
# Sem esse carinha, o navegador pode bloquear minha requisição

# Na minha variável app adicione o método middleware, meu porteiro
app.add_middleware(
    CORSMiddleware,
    # Depois tenho que listar todos os domínios permitidos, agora, tá tudo liberadooo
    allow_origins=["*"],
    allow_credentials=True,
    # Permite GET, POST, PUT, DELETE, etc
    allow_methods=["*"],
    # Esse carinha é meu conjunto de informações de acesso a API - Meu crachá de acesso com código de barra de identificação. Basicamente o CORS está pedindo, me mostra seu crachá pra entrar
    allow_headers=["*"]
)

# Catalogação das minhas rotas
# Aqui tô falando: app, adiciona o método "include_router", esse carinha vai ser minha rota de teste. Tá tudo funcionando?
# Estamos usando "routes" pra deixar tudo organizado e não ficar aquela gambiarra no main.py é um glowUp girl
app.include_router(health.router, tags=["Health"])
app.include_router(podcast.router, tags=["Podcast"])

# Estou definindo uma classe do tipo get. E ele vai pegar o que está no retorno da raiz e retornar uma mensagem para o primata, no caso eu


@app.get("/")
def read_root():
    return {
        # Não esquece da vírgula sempre
        "message": "Ae caralho, você fez uma API com FastAPI e ainda funciona, isso é raro",
        # Ei, me dá esse json ai pra ver se tá tudo certo
        "docs": "http://localhost:8000/docs",
        # Aqui primata, você tem o retorno da sua execução do health que testa se tudo está funcionando antes de seguir.
        "health": "http://localhost:8000/health"
    }
