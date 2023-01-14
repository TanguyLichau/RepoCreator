import os

username = "YourGitHubUsername"
password = "YourGitHubPassword"

repo_name = os.argv[1]
repo_description = "This is my new repository"

if not os.path.exists(repo_name):
    os.makedirs(repo_name)

os.chdir(repo_name)