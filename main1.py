import requests

response = requests.get("https://gitlab.com/api/v4/projects")

my_project = response.json()

for project in my_project:
    print(f"project Name:{project['name']}\nproject url:{project['web_url']}\n")
