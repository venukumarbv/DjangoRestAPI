import requests

# endpoint = "https://httpbin.org/" # HTML response
# endpoint = "https://httpbin.org/anything" # Json response - API


# endpoint = "http://127.0.0.1:8000/"
endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint)

print(get_response.text)
print(get_response.status_code)
print(get_response.json()['message'])

