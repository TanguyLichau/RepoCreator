import os
import sys
import subprocess
import requests
import json

GITHUB_TOKEN ="" # You need to create a token in Github

REPO_NAME = sys.argv[1]
REPO_DESCRIPTION = "New repository"

if not os.path.exists(REPO_NAME):
    os.makedirs(REPO_NAME)

os.chdir(REPO_NAME)


subprocess.run(["git", "init"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "--allow-empty",  "-m", "First Commit"])

url = "https://api.github.com/user/repos"
data = json.dumps({
    "name": REPO_NAME,
    "description": REPO_DESCRIPTION,
    "auto_init": False
})
headers = {
    "Content-Type": "application/json",
    "Authorization":"token " + GITHUB_TOKEN
}
response = requests.post(url, data=data, headers=headers)

repo_url = json.loads(response.text)["html_url"]

subprocess.run(["git", "remote", "add", "origin", repo_url])
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "push", "-u", "origin", "main"])

print("Repo created on GitHub:", repo_url)