# print logos
import random
from art import logo, vs
from game_data import data

import os
clear = lambda: os.system('cls')

# apresentar de forma indica, nome, o que faz e de onde é

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc} from {account_country}!"


def check_anwser(guess, account_a_followers, account_b_followers):
    if account_a_followers > account_b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo)
    should_continue = True
    score = 0
    # gerar uma escolha random from game_data
    account_a = random.choice(data)
    account_b = random.choice(data)

    while should_continue:
        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        # pedir ao user um input
        guess = input("Who has more followers? Type A or B : ").lower()

        # checkar se a resposta esta correta
        ##obter followers count
        ##if para comparar

        account_a_followers = account_a["follower_count"]
        account_b_followers = account_b["follower_count"]
        is_correct = check_anwser(guess, account_a_followers, account_b_followers)

        clear()
        if is_correct:
            score += 1
            print(f"You are right, your current score is {score}!")
        else:
            should_continue = False
            print(f"You are wrong! Your final score is {score}!")


game()

        # scorekeeping

        # fazer o jogo repetitivo

        # faz B tornar-se A

        # clear entre jogos
