#Executa o bloco usando o bash - Identificador 
#!/bin/bash 

echo "Iniciando o PodGerar... Espera primata, que o trabalho agora é comigo"
#Segundo log é para dar uma quebra de linha, para o retorno ser mais amigável
echo ""

echo "Subindo seus container, nem isso precisa fazer ... Ahhh, como eu sofro"
#Subindo o container, tem que ter o comando, né? 
docker-compose up -d

echo ""
#Aguardando o tempo dos containers subirem
echo "Esperando os containers terminando de se arrumar, tá pensando o que?"
sleep 15

echo ""
#Baixando o Ollama, precisamos dele
echo " Bora, ollama, acorda preguiçoso, tô colocando o Ollama pra trabalhar"
./scripts/init-ollama.sh

echo ""
#Testando automaticamente se tá todo mundo vivo
echo "Hey, responde ai, tá todo mundo vivo?"
./scripts/test-health.sh 




