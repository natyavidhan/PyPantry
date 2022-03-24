import requests
import json

class PyPantry:
    def __init__(self, pantryID:str):
        self.pantryID = pantryID
        self.url = f"https://getpantry.cloud/apiv1/pantry/{self.pantryID}"
    
    def get(self):
        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("GET", self.url, headers=headers, data="")
        return json.loads(response.text)
    
    def post(self, basket:str, data:dict):
        payload = json.dumps(data)
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", self.url+f"/basket/{basket}", headers=headers, data=payload)
        print(response.text)