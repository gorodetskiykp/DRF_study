import requests

endpoint = 'https://httpbin.org/anything'

get_response = requests.get(
    endpoint,
    json={'hello_json': 'world'},
    # data={'hello_data': 'world'},
)
print(get_response.json())
