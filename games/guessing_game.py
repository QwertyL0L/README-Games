import random
from github import Github
from conf import *

# GitHub API token and repository information
access_token = ACCESS_TOKEN
repo_owner = USERNAME
repo_name = REPO_NAME

# Initialize GitHub API client
github = Github(access_token)

# Get the repository
repo = github.get_user(repo_owner).get_repo(repo_name)

def guessing_game():
    """a guessing game that you can play on github!!!"""
    number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Github Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Take a guess (refresh when done): "))
            attempts += 1

            if guess < number:
                new_readme_content = "Higher!"
                repo.update_file(README_PATH, "Higher!", new_readme_content, repo.get_contents(README_PATH).sha)
            elif guess > number:
                new_readme_content = "Lower!"
                repo.update_file(README_PATH, "Lower!", new_readme_content, repo.get_contents(README_PATH).sha)
            else:
                new_readme_content = f"Congratulations! You guessed the number {number} in {attempts} attempts."
                repo.update_file(README_PATH, f"Congratulations! You guessed the number {number} in {attempts} attempts.", new_readme_content, repo.get_contents(README_PATH).sha)
                break
        except ValueError:
            print("Use a number next time!")

if __name__ == "__main__":
    guessing_game()
