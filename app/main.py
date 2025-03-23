from fastapi import FastAPI
from app.routers import suplier, parts, vehicle, purchance, warranty, auth, analytics
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="API REST para Gestão de Clientes, Transações e Analytics FORD")

app.include_router(auth.router)
app.include_router(parts.router)
app.include_router(suplier.router)
app.include_router(vehicle.router)
app.include_router(purchance.router)
app.include_router(warranty.router)
app.include_router(analytics.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou defina domínios específicos em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#COMANDO PARA RODAR O SERVIDOR: uvicorn app.main:app --reload
#PORTA: http://127.0.0.1:8000/docs


