from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

from config import read_config


@app.get("/")
def read_root():
    return {"IIOT_stack":"alhpa-v0.1","Author":"Rukshan H", "Email":"rukshan_h@artc.a-star.edu.sg"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)