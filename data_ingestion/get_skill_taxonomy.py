import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

url = "https://auth.emsicloud.com/connect/token"

client_id = os.environ.get('emsi_client_id')
client_secret = os.environ.get('emsi_client_secret')
client_scope = os.environ.get('emsi_client_scope')

payload = f"client_id={client_id}&client_secret={client_secret}&grant_type=client_credentials&scope={client_scope}"
headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

access_token = response.json()['access_token']

url = "https://emsiservices.com/skills/versions"

url = "https://emsiservices.com/skills/versions/latest/skills"

headers = {'Authorization': 'Bearer ' + access_token}

response = requests.request("GET", url, headers=headers).json()

print(response)