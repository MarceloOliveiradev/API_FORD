# Etapa base
FROM python:3.11-slim

# Diretório de trabalho no container
WORKDIR /app

# Copiar arquivos de requirements e instalar dependências
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar toda a aplicação para o container
COPY . .

# Variáveis de ambiente padrão (você pode sobrescrever no docker-compose)
ENV PYTHONUNBUFFERED=1

# Rodar a aplicação com Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]