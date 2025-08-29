from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

# Import dos routers
from workinapi.routers import api_router

# Cria app FastAPI
app = FastAPI(title="Workout API")

# Cors pra não dar erro de navegador se testar front-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui todos os routers do projeto
app.include_router(api_router)

# Habilita paginação global
add_pagination(app)

# Rota raiz só pra teste rápido
@app.get("/")
async def raiz():
    return {"mensagem": "API tá funcionando!"}

# Rota de teste isolada, sem depender do DB
@app.get("/teste")
async def teste():
    return {"status": "ok", "info": "Esta rota não depende de banco"}
