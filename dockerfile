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

# Garantir que o script tenha o interpretador certo
RUN chmod +x entrypoint.sh

# Variáveis de ambiente padrão
ENV PYTHONUNBUFFERED=1

# Evita erro de "entrypoint.sh: not found" em sistemas baseados em sh
SHELL ["/bin/bash", "-c"]

# Executar o script de entrada
CMD ["./entrypoint.sh"]
