from fastapi import FastAPI, HTTPException;
import requests;
import json;

from utils.classes.EcommerceCollection import EcommerceCollection
from utils.classes.Message import Message;
import utils.services.Claude as cladue;
import utils.services.Mongo as mongo;

app = FastAPI()
claude = cladue.Claude()
mongo = mongo.Mongo();



@app.post("/message")
async def create_message(message: Message):
    message = message.message;
    try:
        data = claude.get_message(message);       
        entity_properties = data['content'][0]['text'];
        entity_properties_dict = json.loads(entity_properties);
        action = entity_properties_dict["actions"];
        print(entity_properties_dict);
        newProducts = await mongo.get_data(action, entity_properties_dict);
        print(newProducts);
        responseData = claude.generate_response(message, action, newProducts);
        finalMessage = responseData['content'][0]['text'];
        return finalMessage;

    except requests.exceptions.RequestException as e:
        return HTTPException(status_code=500, detail=str(e));


