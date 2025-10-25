# BaseModel é a classe base do Pydantic — todos os schemas herdam dela.
# Pydantic aproveita o melhor do reaproveitamento do Python, por isso usamos uma classe base herdada.

from pydantic import BaseModel, Field
from typing import Optional


# Define o que o endpoint recebe no POST — as infos que o usuário vai preencher.
# (No caso, eu mesmo, já que é um projeto Gasparzinho, o projetinho infernal versão monolito 👻)
class PodcastScriptRequest(BaseModel):
    theme: str = Field(
        ...,
        # Esse carinha '...' significa que o item é obrigatório.
        # Validação do tamanho da resposta:
        min_length=3,
        max_length=600,
        # Famoso “quer que eu desenhe?” — explicação que aparece no Swagger:
        description="The main topic or theme of the podcast",
        example="Artificial Intelligence and the Future of Work"
    )
    duration: str = Field(
        ...,
        description="Expected duration of the podcast",
        example="10 minutes"
    )
    tone: str = Field(
        ...,
        description="The tone or style of the podcast",
        example="conversational"
    )


# Esse carinha é o famoso “boa experiência do usuário”.
# Define o que a API retorna em cada um dos estados possíveis.
class PodcastScriptResponse(BaseModel):
    success: bool = Field(
        ...,
        description="Whether the script generation was successful"
    )
    script: Optional[str] = Field(
        None,
        description="The generated podcast script"
    )
    model: Optional[str] = Field(
        None,
        description="The AI model used to generate the script"
    )
    error: Optional[str] = Field(
        None,
        description="Error message if generation failed"
    )

    # Cereja do bolo — padronização e exemplo de estrutura de resposta.
    class Config:
        json_schema_extra = {
            "example": {
                "success": True,
                "script": "Welcome to today's podcast about Artificial Intelligence",
                "model": "gemma:2b",
                "error": None
            }
        }
