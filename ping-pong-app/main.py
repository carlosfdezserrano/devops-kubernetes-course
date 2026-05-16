import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()
counter = -1

@app.get("/pingpong")
def get_pong():
    global counter
    counter += 1
    return f"pong {counter}"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print(f"Server started in port {port}")
    uvicorn.run("main:app", host="0.0.0.0", port=port)