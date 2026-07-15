import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)
    response.raise_for_status()

    users = response.json()

    print("===== User Details =====")

    for user in users:
        print("-" * 30)
        print("Name     :", user["name"])
        print("Username :", user["username"])
        print("Email    :", user["email"])
        print("City     :", user["address"]["city"])
        print("Phone    :", user["phone"])

except requests.exceptions.RequestException as e:
    print("Error:", e)