import requests;

from utils.functions import createEntityMessage, createResponseMessage;

class Claude:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.BASE_URL = "https://api.anthropic.com/v1/messages";
        self.VERSION = "2023-06-01";
        pass


    @staticmethod
    def get_instance():
        if not Claude._instance:
            Claude._instance = Claude()
        return Claude._instance

    def get_message(self, message):
        try:
            response = requests.post(
            self.BASE_URL,
            headers={
                "x-api-key": self.API_KEY,
                "anthropic-version": self.VERSION,
                "Content-Type": "application/json"
            },
            json={
                "model": "claude-3-opus-20240229",
                "max_tokens": 1024,
                "messages": [
                {
                    "role": "user",
                    "content": createEntityMessage(message)
                }
                ]
            }
            )

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle exception here
            print("An error occurred:", e)
            return None
    
    def generate_response(self, prevMessage, action, data):
        try:
            response = requests.post(
            self.BASE_URL,
            headers={
                "x-api-key": self.API_KEY,
                "anthropic-version": self.VERSION,
                "Content-Type": "application/json"
            },
            json={
                "model": "claude-3-opus-20240229",
                "max_tokens": 1024,
                "messages": [
                {
                    "role": "user",
                    "content": createResponseMessage(prevMessage, action, data)
                }
                ]
            }
            )

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle exception here
            print("An error occurred:", e)
            return None