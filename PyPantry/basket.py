import requests
import json
from . import PyPantry

class PyPantryBasket:
    def __init__(self, pantry:PyPantry, basket:str):
        self.url = pantry.url+f"/basket/{basket}"
    
    def find(self, query:dict=None):
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", self.url, headers=headers, data="")
        try:
            data = json.loads(response.text)
        except:
            data = {}
        e, f = {}, {}
        if query:
            for key in data.keys():
                if key in query.keys():
                    e[key] = data[key]
            for value in e.values():
                if value in query.values():
                    key = list(e.keys())[list(e.values()).index(value)]
                    f[key] = value
            return f
        else:
            return data
    
    def insert(self, key:str, value):
        data = self.find()
        data[key] = value
        payload = json.dumps(data)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url, headers=headers, data=payload)