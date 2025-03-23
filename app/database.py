from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê a URL do banco do .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("A variável DATABASE_URL não está definida no arquivo .env!")

# Cria o engine do SQLAlchemy
engine = create_engine(DATABASE_URL)

# Cria o SessionLocal para fazer queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos
Base = declarative_base()

# Dependência que será usada nas rotas FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
