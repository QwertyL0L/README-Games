import random
from github import Github
import time
from conf import *

# GitHub API token and repository information
access_token = ACCESS_TOKEN
repo_owner = USERNAME
repo_name = REPO_NAME

# Initialize GitHub API client
github = Github(access_token)

# Get the repository
repo = github.get_user(repo_owner).get_repo(repo_name)

def rps_game():
    """a version of rock paper scissors that you can play on github!!!"""
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Welcome to RPS!")
    player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if player_choice not in choices:
        invalid_choice_message = ("Invalid choice. Please choose rock, paper, or scissors.")
        repo.update_file(README_PATH, "Try Again!", invalid_choice_message, repo.get_contents(README_PATH).sha)
        return

    computer_choice_message = (f"Computer chooses {computer_choice}")
    repo.update_file(README_PATH, f"Computer chose {computer_choice}", computer_choice_message, repo.get_contents(README_PATH).sha)
    time.sleep(5)
    player_choice_message = (f"{USERNAME} chooses {player_choice}")
    repo.update_file(README_PATH, f"{USERNAME} chose {player_choice}", player_choice_message, repo.get_contents(README_PATH).sha)

    if player_choice == computer_choice:
        tie_message = "It\'s a tie!"
        repo.update_file(README_PATH, "It's a tie!", tie_message, repo.get_contents(README_PATH).sha)
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        player_win_message = f"{USERNAME} won!"
        repo.update_file(README_PATH, f"{USERNAME} won!", player_win_message, repo.get_contents(README_PATH).sha)
    else:
        computer_win_message = "Computer won!"
        repo.update_file(README_PATH, "Computer won!", computer_win_message, repo.get_contents(README_PATH).sha)

rps_game()