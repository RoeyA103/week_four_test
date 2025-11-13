from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Literal
import json
from utils import encrypt , file_handler , statics_handler

app = FastAPI()

class Ceasar(BaseModel):
    text:str
    offset:int | None = None
    mode: Literal["encrypt","decrypt"] 

class Fence(BaseModel):
    text : str

@app.get('/test')
def test(): 
    return { 'msg': 'hi from test'}

@app.get('/test/{user_name}')
def get_user(user_name):
    file_handler.save_user(user_name)
    return { 'msg': f'saved user ({user_name})'}


@app.post('/caesar')
def caesar(data:Ceasar):

    if data.mode == "encrypt":
       resolt = encrypt.caesar_encrypt(data.text , data.offset)
    else:
       resolt = encrypt.caesar_decrypt(data.text,data.offset)

    return {"msg":f"The data was {data.mode}ed successfully.",
            f"{data.mode}ed" : resolt }        


@app.get("/fence/encrypt")
def fence(data:str):

    resolt = encrypt.fence_encrypt(data)

    return {"msg":"The data was encrypted successfully.",
            "encrypted" : resolt } 

@app.post("/fence/decrypt")
def fence(data:Fence):

    resolt = encrypt.fence_decrypt(data)

    return {"msg":"The data was decrypted successfully.",
            "decrypted" : resolt }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='localhost',
        port=8080,
        reload=True
    )