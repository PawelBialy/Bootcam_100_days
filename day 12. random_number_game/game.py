from random import randint

HARD_LEVEL = 5
EASY_LEVEL = 10

turns = 0


def check_answer(guess, answer, turns):
    """Checks answer against guess."""
    if guess > answer:
        print("To high")
        return turns - 1
    elif guess < answer:
        print("To low!")
        return turns - 1
    else:
        print(f"You catch it! Selected number is {answer}")


def set_difficulty():
    level = input("Choose a dificulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a nummber between 1 and 100. ")
    answer = randint(1, 100)
    print(f"psst, the answer is {answer} ")

    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} remaining to guess a number.")
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")


game()