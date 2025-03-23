# 🚗 Ford CRM System – API REST com FastAPI

API REST desenvolvida como parte de um desafio técnico para gestão de:

- 🏭 **Fornecedores** (`/supliers`)
- 🔩 **Peças** (`/parts`)
- 🛒 **Compras** (`/purchances`)
- 🚗 **Veículos** (`/vehicle`)
- 🧾 **Garantias** (`/warranties`)
- 📊 **Relatórios Analíticos** (`/analytics`)
- 🔐 **Autenticação JWT** (`/auth`)

---

## 🧰 Tecnologias e Funcionalidades

- **FastAPI** + **Pydantic**
- **SQLAlchemy ORM** + **PostgreSQL**
- **Autenticação JWT** com `python-jose`
- **Criptografia de CPF** com `cryptography`
- **Migrations** com Alembic
- **Testes Automatizados** com `requests`
- **Docker + Docker Compose**
- **CI/CD** com GitHub Actions
- **Swagger UI** disponível em `/docs`

---

## 🚀 Como Executar

### ✅ Opção 1 – Com Docker (recomendado)

> Requer `docker` e `docker-compose`

git https://github.com/MarceloOliveiradev/API_FORD.git

cd seu-repo

docker-compose up --build

##Acesse em: http://localhost:8000/docs##

📝 Importante: Para rodar com Docker, o seu .env deve conter:

DATABASE_URL=postgresql://dev_ford:34852@db:5432/FORD_DATABASE

### 🖥️ Opção 2 – Execução Local
Requer: Python 3.11+, PostgreSQL e virtualenv

# Clonar o projeto
git clone https://github.com/MarceloOliveiradev/API_FORD.git

cd seu-repo

# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

1. Crie o banco PostgreSQL:
createdb FORD_DATABASE
createuser dev_ford --pwprompt

2. Configure o .env com:
DATABASE_URL=postgresql://dev_ford:34852@localhost:5432/FORD_DATABASE

3. Rode as migrations:
alembic upgrade head

4. (Opcional) Popular com dados iniciais:
python -m app.populate_db

5. Subir o servidor:
uvicorn app.main:app --reload

_________________________________________________________

🔐 Autenticação

1. Registrar usuário: POST /auth/register

2. Login: POST /auth/login

3. Enviar token JWT no header:
Authorization: Bearer <seu_token>


🧪 Testes Automatizados
Execute:
python test_all_routes.py

O script simula:

* Registro e login

* CRUD completo

* Relatórios analíticos

* Permissões de Admin/User

⚠️ Importante:

Para testes locais: use localhost no .env

Para subir com Docker: use db no .env

📊 Endpoints Analytics
Necessário JWT:

* /analytics/total-purchases-by-supplier
* /analytics/total-purchases-by-part
* /analytics/warranties-by-supplier
* /analytics/average-purchance-by-type


⚙️ CI/CD – GitHub Actions

* Linter + Testes executados automaticamente

* PostgreSQL mockado via container

* Execução: python test_all_routes.py

🌟 Diferenciais Implementados

✅ Autenticação com JWT
✅ Criptografia de CPF com Fernet
✅ Migrations com Alembic
✅ Docker + Docker Compose
✅ CI/CD com GitHub Actions
✅ Testes Automatizados
✅ Permissões diferenciadas (Admin x User)
✅ CORS habilitado
✅ Documentação automática via Swagger

