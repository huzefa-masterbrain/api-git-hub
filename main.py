import requests

response = requests.get("https://gitlab.com/api/v4/projects")

ls

print(response.json())
print(type(response.json()))
print(response.json()[0])

