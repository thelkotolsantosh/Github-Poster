"""CLI for for GitHub Poster"""

import argparse
import json
from github_poster import GitHubPoster


def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Post content to GitHub (Gists and Issues)"
    )
    
    parser.add_argument("--token", required=True, help="GitHub personal access token")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Gist command
    gist_parser = subparsers.add_parser("gist", help="Create a gist")
    gist_parser.add_argument("filename", help="Filename for the gist")
    gist_parser.add_argument("--content", required=True, help="Content of the gist")
    gist_parser.add_argument("--description", default="", help="Gist description")
    gist_parser.add_argument("--public", action="store_true", default=True, 
                             help="Make gist public")
    
    # Issue command
    issue_parser = subparsers.add_parser("issue", help="Create an issue")
    issue_parser.add_argument("owner", help="Repository owner")
    issue_parser.add_argument("repo", help="Repository name")
    issue_parser.add_argument("--title", required=True, help="Issue title")
    issue_parser.add_argument("--body", default="", help="Issue body")
    issue_parser.add_argument("--labels", nargs="+", help="Labels for the issue")
    
    # User info command
    user_parser = subparsers.add_parser("user", help="Get user information")
    
    # Repo info command
    repo_parser = subparsers.add_parser("repo", help="Get repository information")
    repo_parser.add_argument("owner", help="Repository owner")
    repo_parser.add_argument("repo", help="Repository name")
    
    # List repos command
    list_parser = subparsers.add_parser("list-repos", help="List user repositories")
    
    args = parser.parse_args()
    
    poster = GitHubPoster(args.token)
    
    try:
        if args.command == "gist":
            result = poster.create_gist(
                args.filename,
                args.content,
                args.description,
                args.public
            )
            print("✓ Gist created successfully!")
            print(f"URL: {result['html_url']}")
            print(json.dumps(result, indent=2))
        
        elif args.command == "issue":
            result = poster.create_issue(
                args.owner,
                args.repo,
                args.title,
                args.body,
                args.labels
            )
            print("✓ Issue created successfully!")
            print(f"URL: {result['html_url']}")
            print(json.dumps(result, indent=2))
        
        elif args.command == "user":
            result = poster.get_user_info()
            print("✓ User information retrieved!")
            print(json.dumps(result, indent=2))
        
        elif args.command == "repo":
            result = poster.get_repo_info(args.owner, args.repo)
            print("✓ Repository information retrieved!")
            print(json.dumps(result, indent=2))
        
        elif args.command == "list-repos":
            result = poster.list_user_repos()
            print(f"✓ Found {len(result)} repositories!")
            for repo in result:
                print(f"  - {repo['name']} ({repo['url']})")
        
        else:
            parser.print_help()
    
    except requests.exceptions.RequestException as e:
        print(f"✗ Error: {e}")
        exit(1)


if __name__ == "__main__":
    import requests
    main()
