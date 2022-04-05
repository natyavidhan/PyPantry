import requests
import json
from . import PyPantry

class PyPantryBasket:
    def __init__(self, pantry:PyPantry, basket:str):
        self.url = f"{pantry.url}/basket/{basket}"
    
    def find(self, query:dict=None):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", self.url, headers=headers, data="")
        try:
            data = json.loads(response.text)
        except:
            data = {}
        if not query:
            return data
        e, f = {}, {}
        for key in data:
            if key in query:
                e[key] = data[key]
        for value in e.values():
            if value in query.values():
                key = list(e.keys())[list(e.values()).index(value)]
                f[key] = value
        return f
    
    def insert(self, key:str, value):
        data = self.find()
        data[key] = value
        payload = json.dumps(data)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url, headers=headers, data=payload)