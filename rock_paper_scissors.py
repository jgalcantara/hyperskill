# Write your code here
import random


def player():
    namex = input("Enter your name: ")
    print(f"Hello, {namex}")
    return namex


def ratings(rating):
    scoreboard = {}
    for line in rating:
        name_, score_ = line.split()
        scoreboard[name_] = int(score_)
    return scoreboard


def choices():
    options = input().split(',')
    if options == ['']:
        options = ['paper', 'scissors', 'rock']
    return options


def listed(options_, answer_):
    while options_[int((len(options_) - 1) / 2)] != answer_:
        options_ = options_[-1:] + options_[:-1]
    return options_


def game(listx, score_):
    while True:
        answer = input()
        if answer == "!exit":
            print("Bye!")
            break
        elif answer == "!rating":
            print(f'Your rating: {score_}')
        elif answer in listx:
            in_game = listed(listx, answer)
            score_ = checker(in_game, answer, score_)
        else:
            print("Invalid input")


def checker(mod_list, answer_, score_):
    ai = random.choice(mod_list)
    if ai == answer_:
        print(f"There is a draw ({answer_})")
        score_ += 50
    elif mod_list.index(ai) < mod_list.index(answer_):
        print(f"Well done. Computer chose {ai} and failed")
        score_ += 100
    elif mod_list.index(ai) > mod_list.index(answer_):
        print(f"Sorry, but computer chose {ai}")
    return score_


def main():
    rating = open('rating.txt', 'r')
    rating_dict = ratings(rating)
    player_name = player()
    if player_name in rating_dict:
        score = rating_dict[player_name]
    else:
        score = 0
    list_ = choices()
    print("Okay, let's start")
    game(list_, score)
    rating.close()


main()
