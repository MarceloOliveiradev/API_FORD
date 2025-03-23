# 🚗 Ford CRM System – API REST com FastAPI
API REST desenvolvida como parte de um desafio técnico, com foco na gestão de:

🏭 Fornecedores (/supliers)

🔩 Peças (/parts)

🛒 Compras (/purchances)

🚗 Veículos (/vehicle)

🧾 Garantias (/warranties)

📊 Relatórios Analíticos (/analytics)

🔐 Autenticação JWT (/auth)

🧰 Tecnologias Utilizadas
FastAPI + Pydantic

SQLAlchemy ORM + PostgreSQL

Autenticação JWT com python-jose

Criptografia de CPF com cryptography

Migrations com Alembic

Testes Automatizados com requests

Docker + Docker Compose

CI/CD com GitHub Actions

Swagger UI disponível em /docs

# 🚀 Como Executar o Projeto
Requisitos: Docker e Docker Compose instalados em sua máquina

# 1️⃣ Clonar o Repositório
git clone https://github.com/MarceloOliveiradev/API_FORD.git

cd API_FORD

# 2️⃣ Criar Ambiente Virtual e Instalar Dependências
Isso garante o bom funcionamento do script de testes e ferramentas de apoio local
python -m venv venv

Ativar ambiente virtual:

* Linux/macOS:
  source venv/bin/activate

* Windows:
  venv\Scripts\activate
  
Instalar dependências:

pip install -r requirements.txt

# 3️⃣ Executar com Docker

docker-compose up --build

Acesse a documentação Swagger em:
# 👉 http://localhost:8000/docs

⚙️ Variáveis de Ambiente (.env)

Crie um arquivo .env com:

DATABASE_URL=postgresql://dev_ford:34852@db:5432/FORD_DATABASE

✅ Importante: use db no host ao usar Docker (não localhost).

🔐 Autenticação com JWT

* Registro: POST /auth/register

* Login: POST /auth/login

* Enviar token no cabeçalho:
   Authorization: Bearer <seu_token>

#🧪 Testes Automatizados

✅ Os testes rodam automaticamente ao subir a API.

👉 Ou execute manualmente dentro do container:

docker exec -it ford_api bash

python test_all_routes.py

Este script cobre:

* Registro e Login

* CRUD de todas as entidades

* Relatórios analíticos

* Permissões: usuário comum vs admin

# 📊 Endpoints de Analytics (JWT necessário)

* GET /analytics/total-purchases-by-supplier

* GET /analytics/total-purchases-by-part

* GET /analytics/warranties-by-supplier

* GET /analytics/average-purchance-by-type

# 🚀 CI/CD com GitHub Actions

* Linter + Testes executados automaticamente

* Banco PostgreSQL mockado via container

* Execução dos testes: python test_all_routes.py

# 🌟 Diferenciais Implementados

✅ Autenticação com JWT

✅ Criptografia de CPF com Fernet

✅ Migrations com Alembic

✅ Docker + Docker Compose

✅ CI/CD com GitHub Actions

✅ Testes Automatizados

✅ Permissões diferenciadas (Admin x User)

✅ CORS habilitado

✅ Documentação Swagger interativa



