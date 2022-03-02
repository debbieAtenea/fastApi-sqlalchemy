import string
import secrets

from connect import db, session
from models import usersFast, base
from auth import AuthByToken
from fastapi import FastAPI

app = FastAPI()

base.metadata.create_all(db)

@app.post("/")
async def user_token(username: str, password: str) -> None:
    users = session.query(usersFast)
    for user in users:
        if user.username == username and user.password == password:
            return {"token": user.token}

@app.post("/add_user")
async def insert_user(username: str, password: str,  token: str) -> None:
    auth = AuthByToken
    if auth.auth_by_token(token):
        # create a token
        alphabet = string.ascii_letters + string.digits
        new_token = ''.join(secrets.choice(alphabet) for i in range(8))

        new_user = usersFast(username=username, password=password, token=f'{new_token}')
        print("print new user:", new_user)
        session.add(new_user)
        session.commit()
        return {"username": username, "token": f'{new_token}'}


@app.put("/update_user")
async def say_hello(username: str, password: str,  token: str):
    auth = AuthByToken
    if auth.auth_by_token(token):
        users = session.query(usersFast)
        for user in users:
            if user.username != username and user.password != password:
                if user.token == token:
                    user.username = username
                    user.password = password
                    session.commit()
            elif user.username != username:
                if user.token == token:
                    user.username = username
                    session.commit()
            elif user.password != password:
                if user.token == token:
                    user.password = password
                    session.commit()
        return {"username": username, "token": token}

@app.delete("/delete_user")
async def delete_user(id: int, token: str) -> None:
    auth = AuthByToken
    if auth.auth_by_token(token):
        users = session.query(usersFast)
        for user in users:
            if user.id == id:
                print("id_user: ", user.id)
                session.delete(user)
                session.commit()
    return {"message": "User delted"}

