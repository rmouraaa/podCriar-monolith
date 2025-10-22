#!/bin/bash

#Bora testar o backend - Nossa API FastAPI 
echo "Bora negada, manda o salve que o cria tá esperando"
echo ""

echo "API, tá viva minha filha?"
if curl -s http://localhost:8000/health > /dev/null; then
    echo "Backend ativo: Tô vivo e tô rodando no http://localhost:8000"
else 
    echo "Puts, foi mals, mas não tô ativo não"
fi 

echo ""


#Bora Testa o Banco de dados 

echo "Banco de dados, tá vivo? Responde ai do PostGreSQL"
if docker exec podcast-postgres pg_isready -U podcast_user > /dev/null 2>&1; then
    echo "Tô vivo e tô ativo, tá tudo aqui comigo, manda mais"
else    
    echo "Deu ruim, cai bebê, nada de banco de dados pra você"
fi

echo ""

#Bora de Ollama 

echo "Ollama, tá cuspindo tudo?"
if curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "Cuspindo em tudo, até nas Big Techs"
else 
    echo "Mals, essa Ollama já pastou hehe, deu ruim"
fi

echo ""
echo "Tá tudo funcionando, pelo menos por enquanto primata" 