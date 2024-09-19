import os

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
USER = os.getenv("USER")


def create_repo(repo_name):
    try:
        url = "https://api.github.com/user/repos"
        headers = {
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github+json",
        }
        data = {"name": repo_name}
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        print(f"Repo {repo_name} created.")
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(
            f'Error creating repository "{repo_name}": {e.response.status_code} - {e.response.text}'
        )
        return False


def get_repos():
    try:
        url = f"https://api.github.com/users/{USER}/repos"
        response = requests.get(url)
        response.raise_for_status()
        repos = response.json()
        print(f'Get {[repo["name"] for repo in repos]}')
        return [repo["name"] for repo in repos]
    except requests.exceptions.HTTPError as e:
        print(
            f"Error when retrieving a list of repositories from a user {USER}: {e.response.status_code} - {e.response.text}"
        )
        return []


def check_repo(repo_name):
    repos = get_repos()
    if repo_name in repos:
        print(f"Find {repo_name}")
        return True
    return False


def delete_repo(repo_name):
    try:
        url = f"https://api.github.com/repos/{USER}/{repo_name}"
        headers = {
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github+json",
        }
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        print(f"Repo {repo_name} deleted.")
        return True
    except requests.exceptions.HTTPError as e:
        print(
            f"Error when deleting repository {repo_name}: {e.response.status_code} - {e.response.text}"
        )
        return False
