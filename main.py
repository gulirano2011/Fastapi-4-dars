from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Fake database
users = [
    {"id": 1, "name": "Ali", "age": 20},
    {"id": 2, "name": "Vali", "age": 25},
    {"id": 3, "name": "Sami", "age": 20},
]

# Path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

# Query parameter (filter)
@app.get("/users/")
def get_users(age: Optional[int] = None):
    if age:
        return [user for user in users if user["age"] == age]
    return users
