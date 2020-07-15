# Write your code here
import random

print("H A N G M A N")

def menu():
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: ')
        if choice == 'play':
            hangman()
        elif choice == 'exit':
            exit()


def guess(hidden_word):
    answer_ = input(f"""\n{hidden_word}
Input a letter: """)
    return answer_


def answer(answer_l, word_to_guess_, hint_blanks_, counter_1, blank_list, blank_list_wrong):
    if len(answer_l) == 1:
        if answer_l.islower():
            if answer_l in set(word_to_guess_):
                if answer_l not in blank_list:
                    blank_list.append(answer_l)
                    hint_blanks_ = word_to_guess_
                    for i in word_to_guess_:
                        if i not in blank_list:
                            hint_blanks_ = hint_blanks_.replace(i, "-")
                elif answer_l in blank_list:
                    print("You already typed this letter")
            elif answer_l not in set(word_to_guess_) and answer_l in blank_list_wrong:
                print("You already typed this letter")
            else:
                print("No such letter in the word")
                blank_list_wrong.append(answer_l)
                counter_1 = counter_1 - 1
        else:
            print("It is not an ASCII lowercase letter")
    else:
        print("You should input a single letter")
    return hint_blanks_, counter_1


def closing(hint_blanks_, word_to_guess_):
    if hint_blanks_ == word_to_guess_:
        print(f"""You guessed the word {word_to_guess_}!
You survived!\n""")
        return True
    else:
        pass


def hangman():
        word_list = 'python', 'java', 'kotlin', 'javascript'
        word_to_guess = random.choice(word_list)
        hint_blanks = '-' * (len(word_to_guess))
        blank_list = []  # List of correct guessed letters, no duplication
        blank_list_wrong = []  # List of wrong guessed letters, no duplication
        counter = 8
        while counter > 0:
            guess_letter = guess(hint_blanks)
            hint_blanks, counter = answer(guess_letter, word_to_guess, hint_blanks, counter, blank_list,blank_list_wrong)
            if closing(hint_blanks, word_to_guess):
                break
        else:
            print("You are hanged!\n")

menu()