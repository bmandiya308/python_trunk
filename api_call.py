##web/rest api calls
import requests
from requests.auth import HTTPBasicAuth as auth
import json
response = requests.get("http://127.0.0.1:5000/index",auth=auth('Bhaskar','mandiya'))
print(response)
print(response.status_code)
json_d = json.dumps(eval(response.content))
print(type(json.loads(json_d)))
print(json.loads(json_d)['details'])
