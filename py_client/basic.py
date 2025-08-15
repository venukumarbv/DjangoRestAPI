import requests

# endpoint = "https://httpbin.org/" # HTML response
# endpoint = "https://httpbin.org/anything" # Json response - API


# endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, params={"abc": 123},json={"query": "Hello world from client"}) # Json - Only for Post request

# get_response = requests.post(endpoint, json={"title": "Hello world from client", "newfield": "Dummy12345"}) # Json - Only for Post request

# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())

