import os
import sys
import subprocess

username = "YourGitHubUsername"
password = "YourGitHubPassword"

repo_name = sys.argv[1]
repo_description = "This is my new repository"

if not os.path.exists(repo_name):
    os.makedirs(repo_name)

os.chdir(repo_name)


subprocess.run(["git", "init"])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "--allow-empty",  "-m", "First Commit"])
