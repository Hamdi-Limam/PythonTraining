import requests, concurrent.futures

import requests, json

def get_github_repo(repo_name, github_username):
    request = f'https://api.github.com/repos/{github_username}/{repo_name}'
    return json.dumps(requests.get(request).json(), indent=4)

if __name__=="__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        response_one = executor.submit(get_github_repo, "LearnPython", "LetusDevops").result()
        response_two = executor.submit(get_github_repo, "PythonTraining", "Hamdi-Limam").result()
    # Fake database file
    with open("result.txt", "a") as file:
        file.write(response_one)
        file.write(response_two)