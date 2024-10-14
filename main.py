import requests

def get_repo_status(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}"
    repo_data = requests.get(url).json()

    if 'message' in repo_data and repo_data['message'] == 'Not Found':
        return f"Repository '{repo}' not found."

    readme_url = f"{url}/contents/README.md"
    readme_response = requests.get(readme_url)
    readme_status = "README.md present" if readme_response.status_code == 200 else "README.md not found"

    issues_url = f"{url}/issues"
    issues_response = requests.get(issues_url)
    open_issues = len(issues_response.json())

    prs_url = f"{url}/pulls"
    prs_response = requests.get(prs_url)
    open_prs = len(prs_response.json())

    status = {
        "Name": repo_data.get('name', 'N/A'),
        "Description": repo_data.get('description', 'N/A'),
        "Stars": repo_data.get('stargazers_count', 'N/A'),
        "Forks": repo_data.get('forks_count', 'N/A'),
        "Open Issues": open_issues,
        "Open Pull Requests": open_prs,
        "README.md Status": readme_status
    }

    return status

def print_repo_status(status):
    for key, value in status.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    owner = "your-github-username"
    repo = "your-repository-name"
    status = get_repo_status(owner, repo)
    if isinstance(status, dict):
        print_repo_status(status)
    else:
        print(status)
