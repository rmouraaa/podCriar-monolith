#Começa uma imagem já pronta do python lá do dockerhub, mas a versão leve slim
FROM python:3.11-slim

#Indica que essa é a pasta principal dentro do container / Tipo fazer cd /app
WORKDIR /app

#Instalar tudo que é minimamente necessário para rodar

#Atualiza a lista de pacote disponíveis -y sem perdir permissão
RUN apt-get update && apt-get install -y \
    #Compilador C
    gcc \
    #Ferramentas para conexão com postgres
    postgresql-client \
    #Vamos de requests HTTP
    curl \
    #Limpa o cache para deixar a imagem menor
    && rm -fr /var/lib/apt/lists/*

#Copia o requirements para o container, saindo do meu pc
#Docker cria cache de camadas, por isso precisamos copiar primeiro o requirements.txt
#Se mudar o código e não as dependências não precisa reinstalar tudo.
COPY requirements.txt .

#Instala a porra toda
RUN pip install --no-cache-dir -r requirements.txt 

#Mandando copiar todos os arquivos que tem na pasta do dockerfile, nesse caso o meu backend
# "." - Pasta atual do meu PC
# "." - pasta principal do container, app 
COPY . . 

#Gera a pasta onde os arquivos temporários do podcasts serão guardados
RUN mkdir -p /data/podcasts

#Define que o container vai usar a porta 8000, se não definir usa a padrão, e os containers vão se comunicar via porta
EXPOSE 8000

#Bora inicar negada
# arquivo main variável app
#0.0.0.0 - Aceita conexões de fora 
#Reload - reinicia automaticamente quando o código mudar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


