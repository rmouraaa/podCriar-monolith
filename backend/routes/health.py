# esse carinha me permite criar aquelas rotas que deixam o main.py organizado, lá da função no main
# Isso deixa tudo mais organizado
from fastapi import APIRouter

# Esse carinha é o mesmo que declarei lá no main
router = APIRouter()

# Esse carinha está testando o meu health - Tá vivo health?


@router.get("/health")
# É aqui que estou perguntando e definindo que resposta que ver pra confirmar
# A função retorna um dicionário json que o fastapi converte sozinho
def health_check():
    """
    Endpoint do meu health - escrevendo bonito
    Retorna o status da API
    """
    # Definindo a resposta que quero ver e validar
    # Quando eu acessar 'http://localhost:8000/health vou ver essa mensagem de resposta da API
    return {
        "status": "ok",
        "message": "PodCriar está vivo e funcionando"
    }

# Esse carinha é meu supevisor que está por aí perguntando para o postgres e o ollama estão 100%


@router.get("/health/detailed")
# Essa é a minha função que cobra as respostas que deseja (Tipo você, carente s2)
def health_check_detailed():
    """Resposta da API pra validar se ollama e postgres estão traquilos
    """
    health_status = {
        "api": "Ok",
        "database": "not_checked",
        "ollama": "not_checked"
    }

    return {
        "status": "ok",
        "services": health_status,
        "message": "Sucesso, tudo funcionando, ollama e Postgress"
    }
