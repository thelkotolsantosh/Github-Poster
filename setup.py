"GitHub Poster module for creating gists and posting issues"

import requests
from typing import Optional, Dict, Any


class GitHubPoster:
    """A class to interact with GitHub API for posting content"""
    
    def __init__(self, token: str):
        """
        Initialize GitHubPoster with authentication token
        
        Args:
            token (str): GitHub personal access token
        """
        self.token = token
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.base_url = "https://api.github.com"
    
    def create_gist(self, filename: str, content: str, description: str = "", 
                   public: bool = True) -> Dict[str, Any]:
        """
        Create a GitHub gist
        
        Args:
            filename (str): Name of the file in the gist
            content (str): Content of the gist
            description (str): Description of the gist
            public (bool): Whether the gist should be public
            
        Returns:
            Dict: Response from GitHub API
        """
        url = f"{self.base_url}/gists"
        
        data = {
            "description": description,
            "public": public,
            "files": {
                filename: {
                    "content": content
                }
            }
        }
        
        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def create_issue(self, owner: str, repo: str, title: str, body: str = "", 
                    labels: Optional[list] = None) -> Dict[str, Any]:
        """
        Create an issue in a GitHub repository
        
        Args:
            owner (str): Repository owner
            repo (str): Repository name
            title (str): Issue title
            body (str): Issue body/description
            labels (list): List of labels to add to the issue
            
        Returns:
            Dict: Response from GitHub API
        """
        url = f"{self.base_url}/repos/{owner}/{repo}/issues"
        
        data = {
            "title": title,
            "body": body
        }
        
        if labels:
            data["labels"] = labels
        
        response = requests.post(url, json=data, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_user_info(self) -> Dict[str, Any]:
        """
        Get authenticated user information
        
        Returns:
            Dict: User information from GitHub API
        """
        url = f"{self.base_url}/user"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_repo_info(self, owner: str, repo: str) -> Dict[str, Any]:
        """
        Get information about a repository
        
        Args:
            owner (str): Repository owner
            repo (str): Repository name
            
        Returns:
            Dict: Repository information from GitHub API
        """
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def list_user_repos(self) -> list:
        """
        List all repositories of the authenticated user
        
        Returns:
            list: List of repositories
        """
        url = f"{self.base_url}/user/repos"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
