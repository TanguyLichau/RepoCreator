import os
import sys
import subprocess
import requests
import json

githubToken =""

repo_name = sys.argv[1]
repo_description = "This is my new repository"

if not os.path.exists(repo_name):
    os.makedirs(repo_name)

os.chdir(repo_name)


subprocess.run(["git", "init"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "--allow-empty",  "-m", "First Commit"])

url = f"https://api.github.com/user/repos"
data = json.dumps({
    "name": repo_name,
    "description": repo_description,
    "auto_init": True
})
headers = {
    "Content-Type": "application/json",
    "Authorization":"token " + githubToken
}
response = requests.post(url, data=data, headers=headers)

repo_url = json.loads(response.text)["html_url"]

subprocess.run(["git", "remote", "add", "origin", repo_url])
subprocess.run(["git", "branch", "-M", "main"])
subprocess.run(["git", "push", "-u", "origin", "main"])

print("Successfully created repository on GitHub:", repo_url)

