# Requests is an elegant and simple HTTP library for Python, built for human beings.
# Requests module is a way to make these API calls. You can use this to call any endpoint. For example
import requests, json

github_username = "LetusDevops"
repo_name = "LearnPython"
# API url to grab user data
request = f'https://api.github.com/repos/{github_username}/{repo_name}'

# send get request
response = requests.get(request)

print("Status code :", response.status_code)
print("Headers content-type :", response.headers['content-type'])

# Get the data in json or equivalent dict format
data = response.json()
data = sorted(data.items())


for i in data:
    print(f"* {i[0]}: {i[1]}")
