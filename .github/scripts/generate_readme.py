import requests
import json

def get_pull_request_users(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"
    response = requests.get(url)
    pull_requests = json.loads(response.text)

    users = set()
    for pr in pull_requests:
        user_login = pr['user']['login']
        users.add(user_login)

    return list(users)

def generate_readme(users):
    with open('README.md', 'w') as readme:
        readme.write('# Pull Request Contributors\n\n')
        readme.write('List of GitHub users who have submitted pull requests:\n\n')
        for user in users:
            readme.write(f'- {user}\n')

if __name__ == "__main__":
    repo_owner = "your_username"
    repo_name = "your_repository"

    contributors = get_pull_request_users(repo_owner, repo_name)
    generate_readme(contributors)
