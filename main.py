from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

from config import read_config


@app.get("/")
def read_root():
    """ Info """
    return {"IIOT_stack":"alhpa-v0.1","Author":"Rukshan H", "Email":"rukshan_h@artc.a-star.edu.sg"}

@app.get("/read_config")
def read_read_config():
    """Read config.json file """
    return read_config()





if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)