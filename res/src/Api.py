import requests

from ..typing import Dict, List, Model, Any

from .headers.default import get_headers

class Api(object):

    def __init__(self):

        self.__headers = get_headers()
        self.__url = "https://chatgptnologin.com/api/chat"

    def get_models(self) -> List[Dict[str, Any]]:
    
            return [
                {"id": "gpt-3.5-turbo", "name": "GPT-3.5"},
                {"id": "gpt-4", "name": "GPT-4"},
                {"id": "gpt-4-0125-preview", "name": "GPT-4"},
                {"id": "gpt-4-1106-preview", "name": "GPT-4"}
            ]

    def chat(self, messages: List[Dict[str, str]], model: Model, temperature: float = 0.7) -> str:

        data = {
            "key": "",
            "messages": messages,
            "model": model,
            "prompt": "",
            "temperature": temperature
        }

        response = requests.post(self.__url, headers=self.__headers, json=data, timeout=100)

        # raise an error if the response is not 200
        response.raise_for_status()

        # shuffle the headers
        self.__headers = get_headers()

        return response.content.decode("utf-8")
    




