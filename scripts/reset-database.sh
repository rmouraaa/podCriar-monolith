#!/bin/bash

echo "Como sua ex, seus bancos PostGreSQL vão sumir"
echo ""
read -p "Tem certeza? (digite 'sim' para confirmar): " confirmacao

if [ "$confirmacao" != "sim" ]; then
    echo "Ufa, os bancos estão salvos, a ex ..."
    exit 1
fi

echo ""
echo "Parando containers... Sem piada, isso é coisa pesada"
docker-compose down

echo ""
echo "Fazendo a faxina, tchau ex, tchau bancos"
docker volume rm podcast-generator_postgres_data 2>/dev/null || echo "Volume já estava limpo"

echo ""
echo "Limpando arquivos de áudio...Acabaram as piadas, cansei"
rm -rf ./data/podcasts/*
echo "Mantendo .gitkeep..."
touch ./data/podcasts/.gitkeep

echo ""
echo "Subindo containers novamente..."
docker-compose up -d

echo ""
echo "Aguardando PostgreSQL iniciar..."
sleep 10

echo ""
echo "Banco de dados resetado! Tudo limpo e pronto para começar."