# API Router é o organizador das rotas, e o HTTPException retorna os erros mapeados pelo FastAPI.
from fastapi import APIRouter, HTTPException

# Confirmação da mágica feita nas pastas: como transformamos as pastas em módulos (com __init__.py),
# agora podemos chamar com '..pasta' sem crise existencial.
from schemas import PodcastScriptRequest, PodcastScriptResponse
from services.ollama_service import generate_podcast_script

# Organizador de rotas (nosso maestro)
router = APIRouter(
    # Todas as rotas começam com /api — padronizei, que nem show sertanejo: só dá padrão.
    prefix="/api",
    # Agrupa a visualização no Swagger com a tag (lê-se: “sou chique, tenho categoria!”).
    tags=["podcast"]
)


@router.post(
    # Esse carinha é o endpoint do script — POST /api/generate-script
    "/generate-script",
    response_model=PodcastScriptResponse,
    # Aparência no Swagger — tudo organizadinho (meu TOC agradece).
    summary="Generate Podcast Script",
    # Famoso “documente pra não ter que responder no Slack depois”.
    description="Generate a complete podcast script using AI based on theme, duration, and tone."
)
async def generate_script(request: PodcastScriptRequest):
    """
    Endpoint para gerar o roteiro do podcast.
    Recebe tema, duração e tom, e devolve o script gerado pelo Ollama.
    """
    # Calma, jovem, deixa o serviçal (ollama_service) trabalhar.
    result = await generate_podcast_script(
        theme=request.theme,
        duration=request.duration,
        tone=request.tone
    )

    # Minimalista e direto: o serviço já faz todo o tratamento de erro.
    return result
