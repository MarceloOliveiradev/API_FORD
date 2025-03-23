#!/bin/bash

# Aguarda o banco ficar disponível com Python
echo "⏳ Aguardando o banco ficar disponível com Python..."
python << END
import time
import socket

host = "db"
port = 5432

while True:
    try:
        with socket.create_connection((host, port), timeout=3):
            break
    except OSError:
        time.sleep(1)
END

echo "✅ Banco disponível!"

# Aplica as migrations
echo "⚙️ Aplicando migrations..."
alembic upgrade head

# Aguarda 2 segundos para garantir que as tabelas foram criadas
sleep 2

# Popula o banco com dados iniciais (opcional)
echo "🌱 Populando banco com dados de exemplo..."
python -m app.populate_db

# Inicia o servidor FastAPI com Uvicorn
echo "🚀 Iniciando servidor Uvicorn..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
