import requests

from ..typing import Dict, List, Model, Any

from .headers.default import get_headers

class Api(object):

    def __init__(self):

        self.__headers = get_headers()
        self.__url = "https://chatgptnologin.com/api/chat"

    def get_models(self) -> List[Dict[str, Any]]:

        response = requests.post("https://chatgptnologin.com/api/models", headers=self.__headers, json={"key": ""})

        # raise an error if the response is not 200
        response.raise_for_status()

        # shuffle the headers
        self.__headers = get_headers()

        return response.json()

    def chat(self, messages: List[Dict[str, str]], model: Model, temperature: float = 0.7) -> str:

        data = {
            "key": "",
            "messages": messages,
            "model": model,
            "prompt": "",
            "temperature": temperature
        }

        # check if messages has a first message by role 'system'
        if messages[0]['role'] == 'system':
            
            # if yes, add that as the prompt (cuz why not)
            data['prompt'] = messages[0]['content']

        response = requests.post(self.__url, headers=self.__headers, json=data)

        # raise an error if the response is not 200
        response.raise_for_status()

        # shuffle the headers
        self.__headers = get_headers()

        return response.text
    




