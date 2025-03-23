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

### ✅ Única opção – Via Docker (recomendado)

> Requisitos: `docker` e `docker-compose` instalados

git clone https://github.com/MarceloOliveiradev/API_FORD.git

cd seu_repositório

docker-compose up --build

📄 Acesse a documentação Swagger em: http://localhost:8000/docs

📝 Certifique-se de que o arquivo .env contenha:
DATABASE_URL=postgresql://dev_ford:34852@db:5432/FORD_DATABASE
Importante: use db e não localhost dentro do Docker.

# 🧪 Ambiente Virtual e Instalação de Dependências (Dentro do Container)
Após subir o projeto com #docker-compose up --build#, você pode acessar o container com:

docker exec -it ford_api bash

Dentro do container, crie o ambiente virtual:

python -m venv venv

source venv/bin/activate #LINUX

venv\Scripts\Activate #WINDOWS

Instale as dependências:
pip install -r requirements.txt


# 🔐 Autenticação

1. Registrar usuário: POST /auth/register

2. Login: POST /auth/login

3. Envie o token JWT no cabeçalho:
   Authorization: Bearer <seu_token>


# 🧪 Testes Automatizados (dentro do Docker)
Os testes são executados automaticamente no container ao subir a aplicação.

Ou, se quiser rodar manualmente dentro do container:
   docker exec -it ford_api bash

   python test_all_routes.py

O script cobre:

* Registro e login
* Todas as rotas CRUD
* Relatórios analíticos
* Permissões (admin vs usuário comum)

  
# 📊 Endpoints de Analytics (JWT obrigatório)

*/analytics/total-purchases-by-supplier

*/analytics/total-purchases-by-part

*/analytics/warranties-by-supplier

*/analytics/average-purchance-by-type

# ⚙️ CI/CD – GitHub Actions
* Linter + Testes automatizados
* PostgreSQL mockado em container
* Execução: python test_all_routes.py

# 🌟 Diferenciais Implementados
✅ Autenticação com JWT

✅ Criptografia de CPF com Fernet

✅ Migrations com Alembic

✅ Docker + Docker Compose

✅ CI/CD com GitHub Actions

✅ Testes Automatizados

✅ Permissões diferenciadas (Admin x User)

✅ CORS habilitado

✅ Documentação automática via Swagger


   
