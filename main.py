from fastapi import FastAPI

from routers import fibonacci

app = FastAPI()

app.include_router(fibonacci.router)


# @app.get("/login")

# @app.get("signup")