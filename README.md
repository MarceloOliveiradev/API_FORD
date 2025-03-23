# 🚗 Ford CRM System – API REST com FastAPI
API REST desenvolvida como parte de um desafio técnico para gestão de:

🏭 Fornecedores (/supliers)

🔩 Peças (/parts)

🛒 Compras (/purchances)

🚗 Veículos (/vehicle)

🧾 Garantias (/warranties)

📊 Relatórios Analíticos (/analytics)

🔐 Autenticação JWT (/auth)

# 🧰 Tecnologias Utilizadas
FastAPI + Pydantic

PostgreSQL + SQLAlchemy

JWT Auth com python-jose

Criptografia CPF com cryptography

Migrations com Alembic

Testes automatizados com requests

Docker + docker-compose

CI/CD com GitHub Actions

Swagger UI disponível em /docs

# 🚀 Como Executar
# ✅ Opção 1 – Docker (recomendado)
Requer docker e docker-compose instalados

git clone https://github.com/MarceloOliveiradev/API_FORD.git
cd API_FORD

docker-compose up --build

🔗 Acesse: http://localhost:8000/docs

📝 Importante:
Para rodar com Docker, seu arquivo .env deve conter:

# DATABASE_URL=postgresql://dev_ford:34852@db:5432/FORD_DATABASE
# ⚠️ Use db como host no Docker.

# 🖥️ Opção 2 – Execução Local
Requer Python 3.11+, PostgreSQL e virtualenv
git clone https://github.com/MarceloOliveiradev/API_FORD.git

cd API_FORD

Crie o ambiente virtual:
python -m venv venv

source venv/bin/activate     # Linux/macOS

venv\Scripts\activate        # Windows

# Instale as dependências:
pip install -r requirements.txt

Configure o banco:

1. Crie o banco de dados PostgreSQL:
createdb FORD_DATABASE

createuser dev_ford --pwprompt

2. Configure o arquivo .env:
DATABASE_URL=postgresql://dev_ford:34852@localhost:5432/FORD_DATABASE
# ⚠️ Use localhost como host fora do Docker.

3. Rode as migrations:
alembic upgrade head
   
4. Popule com dados de exemplo (opcional):
python -m app.populate_db

5. Inicie o servidor:
uvicorn app.main:app --reload

# 🔐 Autenticação JWT

1. Registrar: POST /auth/register

2. Login: POST /auth/login

3. Token: adicione no header como:

Authorization: Bearer <seu_token>

# 🧪 Testes Automatizados
Execute:

python test_all_routes.py

O script cobre:

* Registro e login

* CRUD completo

* Relatórios analíticos

* Permissões Admin/User

# 📊 Endpoints de Analytics (JWT necessário)

* /analytics/total-purchases-by-supplier
* /analytics/total-purchases-by-part
* /analytics/warranties-by-supplier
* /analytics/average-purchance-by-type

# ⚙️ CI/CD com GitHub Actions

* Testes automatizados rodam a cada push
* PostgreSQL simulado via container
* Validação via test_all_routes.py

# 🌟 Diferenciais Entregues
✅ Autenticação com JWT
✅ Criptografia de CPF com Fernet
✅ Docker + Docker Compose
✅ Alembic com Migrations
✅ Testes automatizados
✅ Permissões Admin x User
✅ CORS habilitado
✅ CI/CD com GitHub Actions
✅ Documentação com Swagger



