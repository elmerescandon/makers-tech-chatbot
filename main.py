from fastapi import FastAPI, HTTPException;
from pydantic import BaseModel;
import requests;
import utils.services.Claude as cladue;


app = FastAPI()
claude = cladue.Claude()


class Message(BaseModel):
    message: str

@app.post("/message")
async def create_message(message: Message):
    message = message.message;
    try:
        data = claude.get_message(message);       
        entity_properties = data['content'][0]['text'];
        return entity_properties;

    except requests.exceptions.RequestException as e:
        return HTTPException(status_code=500, detail=str(e));
                