from fastapi import FastAPI

app = FastAPI()
from auth_router import auth_router
from order_router import order_router

app.include_router(auth_router)
app.include_router(order_router)


# para rodar o nosso código, executar no terminal: uvicorn main:app --reload

# endpoint:
# dominio.com/pedidos

# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> edição
# Delete -> deletar
