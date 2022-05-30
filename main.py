from fastapi import FastAPI

from .users.routers import department_routers, roles_routers, user_routers

app = FastAPI()
app.include_router(roles_routers.roles_router)
app.include_router(user_routers.user_router)
app.include_router(department_routers.dep_router)


@app.get("/add")
def read_root():
    return {"Hello": "World"}
