# GitHub Poste: A simple Python utility to interact with GitHub API for creating gists, posting issues, and retrieving repository information.

## Features

- Create GitHub Gists
- Create Issues in repositories
- Get user information
- Get repository information
- List user repositories
- Command-line interface for easy usage

## Installation

### From source

```bash
git clone https://github.com/yourusername/github-poster.git
cd github-poster
pip install -r requirements.txt
pip install -e .
```

### Using pip

```bash
pip install github-poster
```

## Quick Start

### Using as a Command-Line Tool

First, set your GitHub personal access token:

```bash
export GITHUB_TOKEN="your_token_here"
```

#### Create a Gist

```bash
github-poster --token $GITHUB_TOKEN gist example.py --content "print('Hello')" --description "Hello World"
```

#### Create an Issue

```bash
github-poster --token $GITHUB_TOKEN issue username reponame --title "Bug Report" --body "Found a bug" --labels bug urgent
```

#### Get User Info

```bash
github-poster --token $GITHUB_TOKEN user
```

#### Get Repository Info

```bash
github-poster --token $GITHUB_TOKEN repo username reponame
```

#### List Your Repositories

```bash
github-poster --token $GITHUB_TOKEN list-repos
```

### Using as a Python Module

```python
from github_poster import GitHubPoster

# Initialize with your token
poster = GitHubPoster("your_github_token")

# Create a gist
gist = poster.create_gist("test.py", "print('Hello World')", "Test gist")
print(gist['html_url'])

# Create an issue
issue = poster.create_issue(
    "username", 
    "reponame", 
    "Issue Title", 
    "Issue description",
    labels=["bug"]
)
print(issue['html_url'])

# Get user info
user = poster.get_user_info()
print(f"User: {user['login']}")

# Get repo info
repo = poster.get_repo_info("username", "reponame")
print(f"Repo: {repo['name']}")

# List repos
repos = poster.list_user_repos()
for repo in repos:
    print(repo['name'])
```

## Requirements

- Python 3.7+
- requests library

## Getting a GitHub Personal Access Token

1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Click "Generate new token"
3. Select scopes: `gist`, `repo` (for public repos), `public_repo` (for public repos only)
4. Generate and copy the token
5. Keep it safe and never commit it to version control

## API Reference

### GitHubPoster

#### Methods

**`create_gist(filename, content, description="", public=True)`**
- Create a new GitHub gist
- Returns: Dictionary with gist data including `html_url`

**`create_issue(owner, repo, title, body="", labels=None)`**
- Create an issue in a repository
- Returns: Dictionary with issue data including `html_url`

**`get_user_info()`**
- Get authenticated user information
- Returns: Dictionary with user data

**`get_repo_info(owner, repo)`**
- Get repository information
- Returns: Dictionary with repository data

**`list_user_repos()`**
- List all repositories of authenticated user
- Returns: List of repository dictionaries

## Project Structure

```
github_poster/
├── __init__.py          # Package initialization
├── poster.py            # Main GitHubPoster class
├── cli.py               # Command-line interface
setup.py                 # Package setup
requirements.txt         # Dependencies
.gitignore              # Git ignore rules
README.md               # This file
```

## Error Handling

The module raises `requests.exceptions.RequestException` for API errors. Wrap API calls in try-except blocks:

```python
from github_poster import GitHubPoster
import requests

poster = GitHubPoster("token")

try:
    gist = poster.create_gist("file.py", "code here")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

## License

MIT License - see LICENSE file for details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues, questions, or suggestions, please open an issue on GitHub.


