import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App!"}

if __name__ == "__main__":
    # Read PORT from environment variable, default to 8000 if not set
    port = int(os.getenv("PORT", 8000))
    print(f"Server started in port {port}")
    uvicorn.run("main:app", host="0.0.0.0", port=port)