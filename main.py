from fastapi import FastAPI

from database import db
from routers import fibonacci, signup, login

cursor = db.cursor()
cursor.execute('SELECT version()')
dbVersion = cursor.fetchone()
print('PostgreSQL database version: ')
print(dbVersion)


# Create task table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS task_table (
        task_id TEXT PRIMARY KEY,
        result BIGINT NOT NULL
    )
    """
)

# Create user talle
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_table (
        email TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
    """
)

cursor.close()
db.commit()

app = FastAPI()

app.include_router(
    fibonacci.router,
    prefix = "/fibonacci",
    tags = ["fibonacci"]
)

app.include_router(
    signup.router,
    prefix = "/signup",
    tags = ["signup"]
)

app.include_router(
    login.router,
    prefix = "/login",
    tags = ["auth"]
)

# @app.get("/login")

# @app.get("signup")