from fastapi import FastAPI

from routes import router

app = FastAPI()
app.include_router(router)

@app.get("/add")
def read_root():
    return {"Hello": "World"}