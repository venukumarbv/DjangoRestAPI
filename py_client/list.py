import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("Enter the Username:")
password = getpass()

auth_response = requests.post(endpoint, json={
    "username": username,
    "password": password
})

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    endpoint = "http://localhost:8000/api/products/"
    # headers = {
    #     "Authorization": f"Token {token}"
    # }

    # Keyword is overridden to have ''Bearer
    headers = {
        "Authorization": f"Bearer {token}"
    }

    get_response = requests.get(endpoint, headers=headers)

    print(get_response.json())
