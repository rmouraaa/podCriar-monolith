#Identificar, esse carinha indica que vai tudo de bash 
#!/bin/bash

echo "Baixando o modelo Gemma3, nosso queridinho, sim, vai demorar, são 1.87Gb, espera"
echo ""

#Biaxa a imagem já pronta do DockerHub do Gemma
docker exec podcast-ollama pull gemma:2b 

echo ""
echo "Gemma está entre a gente primata"
echo ""

echo "Modelos disponíveis" 
#Bora deixar claro que tá tudo funcionando nesse container, lista tudoooooooo 
docker exec podcast-ollama ollama list 


