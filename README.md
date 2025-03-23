# 🚗 Ford CRM System – API REST com FastAPI

API REST desenvolvida como parte de um desafio técnico para gestão de:

- 🏭 **Fornecedores** (`/supliers`)
- 🔩 **Peças** (`/parts`)
- 🛒 **Compras** (`/purchances`)
- 🚗 **Veículos** (`/vehicle`)
- 🧾 **Garantias** (`/warranties`)
- 📊 **Analytics** (`/analytics`)
- 🔐 **Autenticação via JWT** (`/auth`)

---

## 🧰 Tecnologias e Features

- **[FastAPI](https://fastapi.tiangolo.com/)** + **Pydantic**
- **SQLAlchemy ORM** + **PostgreSQL**
- **JWT Auth** com `python-jose`
- **Criptografia (CPF)** com `cryptography`
- **Docker** + `docker-compose`
- **CI/CD** com GitHub Actions
- **Migrations** com Alembic
- **Testes Automatizados** com `requests`
- **Swagger UI** na rota `/docs`

---

## 🚀 Executando a API

### ✅ Opção 1 – Docker (recomendado)

> Apenas com `docker` e `docker-compose` instalados

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

# Subir a API + Banco
docker-compose up --build
```

## Acesse em: http://localhost:8000/docs

---

✅ Opção 2 – Execução local
Requer Python 3.11+, PostgreSQL e virtualenv

# Clonar projeto

git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo

# Criar ambiente virtual

python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

# Instalar dependências

pip install -r requirements.txt

# Criar o banco de dados PostgreSQL manualmente

# Exemplo:

# createdb FORD_DATABASE

# createuser dev_ford --pwprompt

# Configurar variável no .env

echo DATABASE_URL=postgresql://dev_ford:34852@localhost:5432/FORD_DATABASE > .env

# Rodar as migrations

alembic upgrade head

# Popular banco com dados iniciais (opcional)

python -m app.populate_db

# Iniciar servidor

uvicorn app.main:app --reload

🔐 Autenticação

1. Registre-se: POST /auth/register

2. Faça login: POST /auth/login

3. Use o token JWT retornado no header:

Authorization: Bearer <seu_token>

4. Simular logout: POST /auth/logout

🧪 Executar Testes Automatizados
Simula todo o ciclo: registro → login → CRUD → analytics

python test_all_routes.py

📊 Analytics disponíveis (JWT necessário)

- /analytics/total-purchases-by-supplier
- /analytics/total-purchases-by-part
- /analytics/warranties-by-supplier
- /analytics/average-purchance-by-type

🛠️ CI/CD com GitHub Actions
Linter + Testes rodando automaticamente em pushes/pull requests

Banco PostgreSQL mockado via container

Teste executado: python test_all_routes.py

💡 Diferenciais implementados
✅ Autenticação com JWT
✅ Criptografia de CPF com Fernet
✅ Docker + Docker Compose
✅ CI/CD com GitHub Actions
✅ Migrations com Alembic
✅ CORS habilitado
✅ Segurança com permissões de Admin x User
✅ Testes automatizados para todos os endpoints
