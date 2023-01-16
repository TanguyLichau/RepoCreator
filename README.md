# Repo Creator

This project is a python script coupled with a batch file .  
The goal is to use a custom windows terminal command to be able to create a folder, initialize a git repo inside it and link the local repo to a remote repo created on Github

---

## Requirements

You need to have Python installed in order for this project to work.  
You will also need to generate a Github token with the permissions to add a new repo on your account.

---

## Installation

Once you download the project, you will have to copy the absolute path of the python script and put it inside the .bat.txt file.  
You will also need to put your Github token in the python script.

After you do all of the above you just need to remove the .txt from the file and move it in a system variable path.  
C:\Windows should be fine, also if you want to change the name of the windows terminal command you just have to rename the .bat file and name it as you want.  
To use it, open the cmd terminal and type :

```
createGit <name of the repository>
```
