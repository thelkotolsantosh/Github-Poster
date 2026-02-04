"""
Example usage of GitHub Poster module

This file demonstrates various ways to use the github_poster library.
"""

from github_poster import GitHubPoster
import os


def example_basic_usage():
    """Basic example of using GitHubPoster"""
    
    # Get token from environment variable
    token = os.getenv("GITHUB_TOKEN")
    
    if not token:
        print("Please set GITHUB_TOKEN environment variable")
        return
    
    # Initialize poster
    poster = GitHubPoster(token)
    
    # Example 1: Create a gist
    print("=" * 50)
    print("Example 1: Creating a Gist")
    print("=" * 50)
    
    try:
        gist_result = poster.create_gist(
            filename="hello.py",
            content="def hello():\n    print('Hello from GitHub Poster!')",
            description="Sample gist created by GitHub Poster",
            public=True
        )
        print(f"✓ Gist created successfully!")
        print(f"  URL: {gist_result['html_url']}")
        print(f"  ID: {gist_result['id']}")
    except Exception as e:
        print(f"✗ Error creating gist: {e}")
    
    # Example 2: Get user information
    print("\n" + "=" * 50)
    print("Example 2: Getting User Information")
    print("=" * 50)
    
    try:
        user = poster.get_user_info()
        print(f"✓ User information retrieved!")
        print(f"  Username: {user['login']}")
        print(f"  Name: {user['name']}")
        print(f"  Public Repos: {user['public_repos']}")
        print(f"  Followers: {user['followers']}")
    except Exception as e:
        print(f"✗ Error getting user info: {e}")
    
    # Example 3: List user repositories
    print("\n" + "=" * 50)
    print("Example 3: Listing User Repositories")
    print("=" * 50)
    
    try:
        repos = poster.list_user_repos()
        print(f"✓ Found {len(repos)} repositories:")
        for i, repo in enumerate(repos[:5], 1):  # Show first 5
            print(f"  {i}. {repo['name']} - {repo['description'] or 'No description'}")
        if len(repos) > 5:
            print(f"  ... and {len(repos) - 5} more")
    except Exception as e:
        print(f"✗ Error listing repos: {e}")
    
    # Example 4: Get repository information
    # Note: Replace 'username' and 'reponame' with actual values
    print("\n" + "=" * 50)
    print("Example 4: Getting Repository Information")
    print("=" * 50)
    
    try:
        # This example assumes a repo exists - adjust as needed
        repo = poster.get_repo_info("torvalds", "linux")
        print(f"✓ Repository information retrieved!")
        print(f"  Name: {repo['name']}")
        print(f"  Description: {repo['description']}")
        print(f"  Stars: {repo['stargazers_count']}")
        print(f"  Forks: {repo['forks_count']}")
        print(f"  Language: {repo['language']}")
    except Exception as e:
        print(f"✗ Error getting repo info: {e}")
    
    # Example 5: Create an issue
    # Note: Uncomment and modify with real repo details
    print("\n" + "=" * 50)
    print("Example 5: Creating an Issue (Commented Out)")
    print("=" * 50)
    
    print("To create an issue, uncomment the code below and modify with real values:")
    print("""
    try:
        issue = poster.create_issue(
            owner="username",
            repo="repository_name",
            title="Test Issue from GitHub Poster",
            body="This is a test issue created using GitHub Poster library",
            labels=["test", "automated"]
        )
        print(f"✓ Issue created successfully!")
        print(f"  URL: {issue['html_url']}")
    except Exception as e:
        print(f"✗ Error creating issue: {e}")
    """)


if __name__ == "__main__":
    print("GitHub Poster - Examples\n")
    example_basic_usage()
