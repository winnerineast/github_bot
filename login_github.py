from github import Github

# Authentication is defined via github.Auth
from github import Auth

# using an access token
import os

access_token = os.environ.get("GITHUB_TOKEN")

if not access_token:
    print("Error: Please set the GITHUB_TOKEN environment variable.")
    exit(1)

auth = Auth.Token(access_token)

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    if repo.name == "legal-intelligence" or \
       repo.name == "winnerineast.github.io" or \
       repo.name == "crewAI" or \
       repo.name == "quivr" or \
       repo.name == "crawlab" or \
       repo.name == "guessbit" or \
       repo.name == "rag-from-scratch" or \
       repo.name == "MaxKB" or \
       repo.name == "llm.c" or \
       repo.name == "calibre" or \
       repo.name == "30dayMakeOS" or \
       repo.name == "EasySpider" or \
       repo.name == "btc-address-dump" or \
       repo.name == "ollama-pdf-bot" or \
       repo.name == "Origae-6" or \
       repo.name == "MLKX":
        print(repo.name)
    else:
        repo.delete()

# To close connections after use
g.close()