from flask import app
import requests  # Import the requests library to handle HTTP requests
import json
import os

def entities_analyzer(text): 
    url = os.environ.get('API_URL')
    api_key = os.environ.get('API_KEY')
    json_obj = {"text": text, "features": {"entities": {}}}
    header = {'Content-Type': 'application/json'}  
    response = requests.post(url, json=json_obj, headers=header, auth=('apikey', api_key))  
    
    if response.status_code != 200:
        return {'entities': None}
    else:
        formatted_response = response.json()
        entities = []
        for entity in formatted_response['entities']:
            formatted_entity = dict(text=entity['text'], type=entity['type'])
            entities.append(formatted_entity)
        return entities

