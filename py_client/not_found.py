import requests


endpoint = "http://localhost:8000/api/products/1123456789098732"

get_response = requests.get(endpoint)

print(get_response.json())