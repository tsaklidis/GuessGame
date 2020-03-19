# -*- coding: utf-8 -*-
import time
import random

# Cange to True in order to see secret info
DEBUG = False


def clear_scr(msg=None):
    # Change the line to clear the screen
    for i in range(0, 100):
        print("\n")
    if msg:
        # if there is a msg print after cleaning
        print(msg)


def animate_load():
    gif = "|"
    for i in range(0, 50):
        clear_scr("Loading the magic numbers...")
        print(gif)
        gif = gif + "|"
        # simulate loading, begin with slow, finish with fast.
        if i < 3:
            time.sleep(0.5)
        elif i < 6:
            time.sleep(0.2)
        elif i < 8:
            time.sleep(0.1)
        elif i > 30 and i < 35:
            time.sleep(0.5)
        else:
            time.sleep(0.05)
    clear_scr()
    print("#######################################\n")
    print(" \tLoading Completed! \n")
    print(" You started the game -Guess the number- \n")
    print("#######################################\n")


def get_number():
    while True:
        # Ask until number is [1-100]
        try:
            unfiltered = input("Type your guess:")
            if DEBUG:
                print("User gave:", unfiltered)
            if unfiltered in accepted[6:10]:
                # if user enter b on any input, exit
                quit("You selected to exit, thank you.")
            else:
                # If no exit, try to convert the number.
                unfiltered = int(unfiltered)
        except ValueError:
            # On not number we have ValueError
            print("\n\nPlease enter a *number* from 1 to 100")
            print("Try again.")
            # Ask again for the number
            continue
        if unfiltered > 0 and unfiltered <= 100:
            # unfiltered is a number in range
            # also 'return unfiltered' can be used
            good_guess = unfiltered
            break
        else:
            print("You are out of range [1-100]\n")
            continue
    return good_guess


if __name__ == "__main__":
    msg = "[A] In order to start press A or enter.\n[B] For exit press B.\nSelect: "  # noqa
    accepted = "ΑΆάαAaβΒbB"
    ok = guess = "a"  # simulate enter

    if not DEBUG:
        animate_load()
    select = input(msg)

    while select not in accepted:
        if DEBUG:
            print("User selected:", select)
        select = input("Select an available option. [Α] ή [Β]:")

    if select in accepted[:6]:
        while ok in accepted[:6]:
            # user selected to play
            tries = 0
            clear_scr()
            print("*******************************")
            print(" \tSo let's play... \n")
            print(" If you want to exit press [Β] ")
            print("*******************************\n")

            secret = random.randint(1, 100)
            print("I am thinking a number, from 1 to 100.")
            if DEBUG:
                print("Secret num is:", secret)
            print("Try to guess it.")

            # Ask for number until it is 1-100
            guess = get_number()
            tries = tries + 1  # save first try
            while guess != secret:
                # user didn't find the number, inform him
                if DEBUG:
                    print("Tries:", tries)
                if secret < guess:
                    tries = tries + 1
                    print("\nMy number is less than {0}".format(guess))  # noqa
                    guess = get_number()
                if secret > guess:
                    tries = tries + 1
                    print("\nMy number is greater than {0}".format(guess))  # noqa
                    guess = get_number()
            if secret == guess:
                clear_scr()
                print("*******************************\n")
                print("\tBRAVO !\nyou guessed it with the {0} try.".format(tries))  # noqa
                pnt = "points"
                if tries == 1:
                    score = 10
                else:
                    score = 10 - tries
                if score == 1:
                    pnt = "point"
                if score < 0:
                    score = 0
                print("You earned {0} {1}.".format(score, pnt))
                print("*******************************\n")
                print("[A] If you want to play again selet Α or enter.\n[B] For exit select anything else.\n")  # noqa
                ok = input("Select:")

        print("Thank you for playing.")

    else:
        clear_scr("Sorry for spending your time...")
