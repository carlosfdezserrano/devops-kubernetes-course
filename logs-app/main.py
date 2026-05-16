import os
import string
import secrets
import uvicorn
from datetime import datetime
from fastapi import FastAPI

app = FastAPI()

def make_random_string(length: int = 24) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))

token = make_random_string()

@app.get("/")
def read_root():
    global token
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "token": token
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"Server started in port {port}")
    uvicorn.run("main:app", host="0.0.0.0", port=port)