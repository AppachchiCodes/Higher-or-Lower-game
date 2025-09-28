from art import logo, vs
from Game_Data import data
import random

def account_data (account):
    """takes the account data and returns printable format"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description},from {country}"

def follow_count_answer (guess, a_followers, b_followers):
    """takes user guess and follower a and b return if it's correct  or not"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    # Generate a random account from the game data & make account b equal to account a
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)


    print(f"Compare: {account_data(account_a)}")
    print(vs)
    print(f"Against: {account_data(account_b)}")

    # Ask user for a guess.
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    # - Get follower count of each account
    follow_count_a = account_a["follower_count"]
    follow_count_b = account_b["follower_count"]

    #Check if user is correct
    is_correct = follow_count_answer(user_guess, follow_count_a, follow_count_b)
    # Give user feedback on their guess.
    # score keeping.
    if is_correct:
        score += 1
        print(f"You are right!, Current Score {score}")
    else:
        print(f"You are wrong, Final score {score}")
        should_continue = False
