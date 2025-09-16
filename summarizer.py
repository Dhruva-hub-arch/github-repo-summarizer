import requests

def fetch_repo_readme(user, repo):
    """Fetch README.md content from a public GitHub repository."""
    url = f"https://api.github.com/repos/{user}/{repo}/readme"
    headers = {"Accept": "application/vnd.github.v3.raw"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return "README not found."

def summarize_text(text, limit=80):
    """Make a short summary from README text."""
    words = text.split()
    if len(words) <= limit:
        return text
    return " ".join(words[:limit]) + "..."

if _name_ == "_main_":
    # Example repo (replace with any GitHub repo you want to test)
    user = "Dhruva-hub-arch"
    repo = "github-repo-summarizer"

    print(f"Fetching README from {user}/{repo} ...\n")
    readme_content = fetch_repo_readme(user, repo)
    summary = summarize_text(readme_content) 

   print("README Summary:\n")
   print(summary)


