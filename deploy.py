import os
import subprocess

# GitHub repository URL (replace this with your repository URL)
REPO_URL = "https://github.com/choksi2212/Antakshari-Software.git"

# Folder name of your project
PROJECT_DIR = "Antakshari-Software"

def initialize_git():
    # Initialize the git repository if it doesn't exist
    if not os.path.exists(f"./{PROJECT_DIR}/.git"):
        subprocess.run(["git", "init"], cwd=PROJECT_DIR)
        subprocess.run(["git", "remote", "add", "origin", REPO_URL], cwd=PROJECT_DIR)

def add_and_commit_changes():
    # Add and commit changes to the repository
    subprocess.run(["git", "add", "."], cwd=PROJECT_DIR)
    subprocess.run(["git", "commit", "-m", "Initial commit for GitHub Pages deployment"], cwd=PROJECT_DIR)

def push_to_github():
    # Push the changes to GitHub
    subprocess.run(["git", "branch", "-M", "main"], cwd=PROJECT_DIR)
    subprocess.run(["git", "push", "-u", "origin", "main"], cwd=PROJECT_DIR)

def enable_github_pages():
    # Enable GitHub Pages by pushing to the `gh-pages` branch
    subprocess.run(["git", "checkout", "-b", "gh-pages"], cwd=PROJECT_DIR)
    subprocess.run(["git", "push", "-u", "origin", "gh-pages"], cwd=PROJECT_DIR)

if __name__ == "__main__":
    print("Initializing Git repository...")
    initialize_git()

    print("Adding and committing changes...")
    add_and_commit_changes()

    print("Pushing to GitHub...")
    push_to_github()

    print("Enabling GitHub Pages...")
    enable_github_pages()

    print("Your project is now hosted on GitHub Pages!")
