import requests
from requests import Request

endpoint_home = 'http://127.0.0.1:8000/api'
endpoint_echo = 'http://127.0.0.1:8000/api/echo'

get_response = requests.get(endpoint_home)
print(get_response.text)
print(get_response.status_code)
print(get_response.json())

get_response = Request(
    'GET',
    endpoint_echo,
    params={
        "message": "hello world params",
    },
    json={
        "message": "hello world json",
    },
    headers={
        "Content-Type": "application/json",
    },

)
r = get_response.prepare()
s = requests.Session()
result = s.send(r)

print(result.text)
# print(get_response.status_code)
print(result.json())
