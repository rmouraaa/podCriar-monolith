#!/bin/bash

# Cria pasta de backup com data/hora
BACKUP_DIR="backups/podcasts_$(date +%Y%m%d_%H%M%S)"
mkdir -p $BACKUP_DIR

echo "Fazendo backup dos podcasts..."
echo ""

# Copia arquivos de áudio
cp -r ./data/podcasts/* $BACKUP_DIR/ 2>/dev/null

# Conta quantos arquivos foram copiados
NUM_FILES=$(find $BACKUP_DIR -type f | wc -l)

echo "✅ Backup concluído!"
echo "✅ Local: $BACKUP_DIR"
echo "✅ Total de arquivos: $NUM_FILES"
echo ""

# Faz backup do banco também
echo "Fazendo backup do banco de dados..."
docker exec podcast-postgres pg_dump -U podcast_user podcast_db > $BACKUP_DIR/database_backup.sql

echo "✅ ackup do banco salvo em: $BACKUP_DIR/database_backup.sql"
echo ""
echo "Backup completo finalizado!"