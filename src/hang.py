"""This is where the magic happens for the hangman game which I'm using to learn some Python"""

# SORRY FOR THE LACK OF OR OVER-COMMENTING, THIS WAS MORE FOR ME THAN SOMEONE ELSE. I JUST NEEDED
# SOME NOTES WHILE I LEARNED PYTHON.
# HOPEFULLY YOU ENJOY THE GAME !! (IF YOU EVEN SEE THIS LOL)

import random
import os
import subprocess
import sys
import time
import urllib.request
import json
from art import (
    beginning,
    first_wrong,
    second_wrong,
    third_wrong,
    fourth_wrong,
    fifth_wrong,
    hangman_saved,
)
from art import final_wrong, main_menu_screen, help_screen_menu, one_player_screen
from art import two_player_screen, you_win_screen, game_over_screen

# if you would like to add more words, in python, to add something to a dictionary you would do:
# "word": "hint for the word",  <- make sure to also put the comma for more words that you would
# like to add later

# Software information
VERSION = "v1.0.0"
REPO = "John35653/Hangman-py"

# def program_update():
#     """A function to check if the program is up to date and if so, to get the new
#     version from Github releases.
#     """
#     print("Checking for update",end=" ")
#     sys.stdout.flush()
#     time.sleep(1)
#     for _ in range(3):
#         print(".",end=" ")
#         sys.stdout.flush()
#         time.sleep(1)

POSSIBLE_WORDS_1P: dict = {
    "hello": "A greeting",
    "goodbye": "A farewell",
    "pancake": "A breakfast item",
    "syrup": "A condiment that goes on top of a breakfast food",
    "eggs": "An animal makes this",
    "coffee": "Something that you drink in the morning",
    "hamster": "A pet that you may give to your child",
    "video": "Something that you watch",
    "jazz": "Known as the ____ age, popular exploding in the 1920s",
    "quiz": "Something that you take in school",
    "pizza": "Some say this food tastes better cold in the morning",
    "jacket": "You wear this when it is cold outside",
    "shadow": "Everyone has one, and you see it when it is sunny out",
    "zombie": "Commonly referred to as the walking dead",
    "subway": "Both a sandwich shop and a way to get around places",
    "flamingo": "A pink bird that likes to stand on one leg",
    "backpack": "Something that students wear to school to hold their books",
    "camping": "Something that people do on the weekends, mmm s'mores",
    "fishing": "Something that kids would do with their dad or grandpa",
    "marshmallow": "This sugary food item tastes good roasted",
}

BASE_LETTERS = [
   "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


# BASE_LETTERS = [
#    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
#    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
#    ]
#
# this is for when black formatting makes the list super long height wise, just copy and paste this
# instead of manually fixing

AVAILABLE_LETTERS = BASE_LETTERS.copy()
MAIN_MENU_DONE: bool = False
ANSWER: str = ""
ONE_PLAYER_SCREEN_DONE: bool = False
TWO_PLAYER_SCREEN_DONE: bool = False
ONE_PLAYER: bool = False
TWO_PLAYER: bool = False
ONE_PLAYER_GIVE_HINT: bool = False
ONE_PLAYER_OPTIONAL_HINT: bool = False
HINT_DENIAL: bool = False
GAME_BEGINS: bool = False
GAME_WIN: bool = False
GAME_OVER: bool = False
UNDERSCORE_WORD: str = ""
DIFFICULTY_CHOICE: str = ""
PLAYER_HINT: str = ""
GUESSES: int = 0


def clear_terminal() -> None:
    """This function clears the terminal using the built-in clear command regardless of what
    platform the user is on
    """
    subprocess.call(["cls"] if os.name == "nt" else ["clear"], shell=True)


def exit_message() -> None:
    """Prints a goodbye message, just to clean the code base up."""
    print("Thanks for playing, have a wonderful day!")


def exit_check(user_answer: str) -> None:
    """This is a function that checks if the user has typed "exit" or "Exit" to quit the program

    Args:
        user_answer (str): The answer that the user gives when prompted for input. If the answer
        is exit, the program will exit.
    """
    if user_answer == "exit":
        exit_message()
        time.sleep(1)
        sys.exit()


def is_number(user_answer: str) -> bool:
    """This is a riff on the is number to check if the user is typing numbers. By turning it into
    a double, with try and except we can convert the answer to a double, which will accept integers.
    Anything else and it returns false.

    Args:
        user_answer (str): A string the user gives

    Returns:
        bool: True if the number was able to be cast as a double, otherwise returns false, likely
        indicating the user gave either a char or string.
    """
    try:
        float(user_answer)
        return True
    except ValueError:
        return False


def usage_message() -> None:
    """A generic message telling the user they didn't give the right answer
    and need to try again.
    """
    print("\nThat is not a valid option. Please choose from the possible options\n")
    time.sleep(1.5)

def trying_something(x: int)  -> int:
    """This is for practicing unit testing in Python.

    Args:
        x (int): This is the input that is to be squared.

    Returns:
        int: This is the return result of squaring the given input.
    """
    return x * x


def main() -> None:  # pylint: disable=too-many-branches, too-many-statements
    """This is the main function of the hangman program"""
    global ONE_PLAYER_SCREEN_DONE, TWO_PLAYER_SCREEN_DONE, ONE_PLAYER, ONE_PLAYER_GIVE_HINT  # pylint: disable=global-statement
    global TWO_PLAYER, GUESSES, MAIN_MENU_DONE, DIFFICULTY_CHOICE, UNDERSCORE_WORD  # pylint: disable=global-statement
    global ONE_PLAYER_OPTIONAL_HINT, PLAYER_HINT, ANSWER, GAME_BEGINS, GAME_OVER, GAME_WIN  # pylint: disable=global-statement
    global AVAILABLE_LETTERS, HINT_DENIAL  # pylint: disable=global-statement

    # ----------------------------------------MAIN-MENU---------------------------------------------

    while True:

        while not MAIN_MENU_DONE:
            clear_terminal()
            main_menu_screen()

            print("Please make a selection: ", end="")
            user_answer: str = input().lower()
            exit_check(user_answer)

            match user_answer:
                case "o" | "one":
                    print("Great! Let's get started!")
                    while not ONE_PLAYER_SCREEN_DONE:
                        clear_terminal()
                        one_player_screen()
                        ANSWER = random.choice(list(POSSIBLE_WORDS_1P))
                        PLAYER_HINT = POSSIBLE_WORDS_1P[ANSWER]
                        DIFFICULTY_CHOICE = input(
                            "Would you like to play Easy, Medium, or Hard?: "
                        ).lower()
                        exit_check(DIFFICULTY_CHOICE)
                        match DIFFICULTY_CHOICE:
                            case "b":
                                break
                            case "e" | "easy":
                                ONE_PLAYER_GIVE_HINT = True
                                ONE_PLAYER_SCREEN_DONE = True
                                ONE_PLAYER = True
                                MAIN_MENU_DONE = True
                            case "m" | "medium":
                                ONE_PLAYER_OPTIONAL_HINT = True
                                ONE_PLAYER_SCREEN_DONE = True
                                ONE_PLAYER = True
                                MAIN_MENU_DONE = True
                            case "h" | "hard":
                                ONE_PLAYER_SCREEN_DONE = True
                                ONE_PLAYER = True
                                MAIN_MENU_DONE = True
                            case _:
                                usage_message()
                    if DIFFICULTY_CHOICE == "b":
                        DIFFICULTY_CHOICE = ""
                        continue
                    if ONE_PLAYER_SCREEN_DONE:
                        break
                case "t" | "two":
                    while not TWO_PLAYER_SCREEN_DONE:
                        clear_terminal()
                        two_player_screen()
                        user_answer = input(
                            "Would you like to give the player a hint ( y)es or n)o )?: "
                        ).lower()
                        exit_check(user_answer)
                        match user_answer:
                            case "b":
                                break
                            case "y" | "yes":
                                ANSWER = input(
                                    "Please enter the word you want the user to guess: "
                                ).lower()
                                if ANSWER == "b":
                                    break
                                PLAYER_HINT = input("Please put in the hint: ").lower()
                                if PLAYER_HINT == "b":
                                    break
                                TWO_PLAYER = True
                                TWO_PLAYER_SCREEN_DONE = True
                                MAIN_MENU_DONE = True
                                ONE_PLAYER_OPTIONAL_HINT = True
                                # tired of making flags, reusing this ^ one for two player hint
                                break
                            case "n" | "no":
                                ANSWER = input(
                                    "Please enter the word you want the user to guess: "
                                ).lower()
                                if ANSWER == "b":
                                    break
                                TWO_PLAYER = True
                                TWO_PLAYER_SCREEN_DONE = True
                                MAIN_MENU_DONE = True
                                HINT_DENIAL = True
                                break
                            case _:
                                usage_message()
                        if user_answer == "b" or ANSWER == "b" or PLAYER_HINT == "b":
                            break
                    if user_answer == "b" or ANSWER == "b" or PLAYER_HINT == "b":
                        user_answer = ""
                        ANSWER = ""
                        PLAYER_HINT = ""
                        continue
                    if TWO_PLAYER_SCREEN_DONE:
                        break
                case "h" | "help":
                    clear_terminal()
                    help_screen_menu()
                    input()
                    continue
                case "e" | "exit":
                    exit_message()
                    sys.exit()
                case _:
                    usage_message()

            if ONE_PLAYER_SCREEN_DONE or TWO_PLAYER_SCREEN_DONE:
                MAIN_MENU_DONE = True
                break

        # ---------------------------------------END-OF-MAIN-MENU-----------------------------------
        # ------------------------------------------GAME-BEGINS-------------------------------------
        # PRINTING HANGMAN
        while MAIN_MENU_DONE and not GAME_OVER:
            if GUESSES == 0:
                clear_terminal()
                beginning()
            elif GUESSES == 1:
                clear_terminal()
                first_wrong()
            elif GUESSES == 2:
                clear_terminal()
                second_wrong()
            elif GUESSES == 3:
                clear_terminal()
                third_wrong()
            elif GUESSES == 4:
                clear_terminal()
                fourth_wrong()
            elif GUESSES == 5:
                clear_terminal()
                fifth_wrong()
            elif GUESSES == 6:
                clear_terminal()
                final_wrong()
                game_over_screen()
                GAME_OVER = True
                break

            # PRINTING THE UNDERSCORE WORD AND THE AVAILABLE LETTERS LEFT TO USE
            if not GAME_BEGINS:
                UNDERSCORE_WORD = "_" * len(ANSWER)
                GAME_BEGINS = True
            if ONE_PLAYER_GIVE_HINT:
                print(
                    "Word: "
                    + UNDERSCORE_WORD
                    + "     Guesses left: "
                    + str(6 - GUESSES)
                    + "    hint: "
                    + PLAYER_HINT
                )
            else:
                print(
                    "Word: "
                    + UNDERSCORE_WORD
                    + "     Guesses left: "
                    + str(6 - GUESSES)
                )
            print("\nAvailable Letters:")
            for letter in AVAILABLE_LETTERS:
                print(letter.upper(), end=" ")

            # GET CHAR FROM THE USER
            guessed_char = input(
                "\nPlease enter your choice from Available Letters: "
            ).lower()
            exit_check(guessed_char)

            # CHECKING IF THE USER WANTS A HINT OR TO QUIT THE GAME
            if len(guessed_char) > 1:
                if guessed_char == "hint" and DIFFICULTY_CHOICE != "h":
                    if HINT_DENIAL:
                        print(
                            "\nThe other person you are playing with has decided to not "
                            "provide a hint to you."
                        )
                        time.sleep(1.5)
                    elif ONE_PLAYER_OPTIONAL_HINT:
                        ONE_PLAYER_GIVE_HINT = True
                elif guessed_char == "hint" and DIFFICULTY_CHOICE == "h":
                    print("\nYou are on hard and can not receive hints.")
                    time.sleep(1.5)
                else:
                    usage_message()
                continue

                # CHECKING TO SEE IF THE CHAR IS AVAILABLE OR IF THEY EVEN ENTERED A LETTER
            is_num: bool = is_number(guessed_char)
            # Looking back, I didn't need to do this but was still cool to be able to differentiate
            # if the user had entered a number or a char.
            if is_num:
                print(
                    f"\nYour choice: {guessed_char} is not part of the available letters. "
                    "Please try again."
                )
                time.sleep(1.5)
                continue
            if guessed_char not in AVAILABLE_LETTERS:
                print(
                    f"\nThe character {guessed_char.upper()} is not available. Please try again."
                )
                time.sleep(1.5)
                continue

                # REMOVING THE CHAR FROM AVAILABLE_LETTERS
            for i, char in enumerate(AVAILABLE_LETTERS):
                if guessed_char == char:
                    AVAILABLE_LETTERS[i] = "_"
                    break

                # CHECKING TO SEE IF THE GUESSED CHAR IS CORRECT OR NOT
            if guessed_char in ANSWER:
                new_word = ""
                for i, char in enumerate(ANSWER):
                    if guessed_char == char:
                        new_word += guessed_char
                    else:
                        new_word += UNDERSCORE_WORD[i]
                UNDERSCORE_WORD = new_word
                if UNDERSCORE_WORD == ANSWER:
                    clear_terminal()
                    hangman_saved()
                    you_win_screen()
                    GAME_WIN = True
                    break
                continue

                # IF THE LETTER IS WRONG, TELL THE USER IT'S WRONG, RAISE THE GUESS COUNT,
                # AND LET THE USER TRY AGAIN
            elif guessed_char not in ANSWER:
                GUESSES += 1
                if 0 < GUESSES < 6:
                    print("\nThat is not correct. Plase try again.")
                    time.sleep(1.5)
                elif GUESSES == 6:
                    print("\nOops, you're all out of guesses.")
                    time.sleep(1.5)
                    break
                continue

        # -----------------------------GAME-LOOP-ENDS-----------------------------------------------
        # SEEING IF THE USER WOULD LIKE TO PLAY AGAIN
        while GAME_OVER or GAME_WIN:
            user_answer = input("Would you like to play again? ( Y)es or N)o ): ")
            exit_check(user_answer)

            # RESET FLAGS AND VARIABLES TO THEIR BEGINNING STATE IF THE USER WANTS TO PLAY AGAIN,
            # USE ONE_PLAYER AND TWO_PLAYER FLAGS. SEPARATING THIS TO REDUCE ACTIONS
            match user_answer:
                case "y" | "yes":  # IF YES, RESTART THE LOOP
                    if ONE_PLAYER:
                        ONE_PLAYER_SCREEN_DONE = False
                        ONE_PLAYER = False
                        DIFFICULTY_CHOICE = ""
                    if TWO_PLAYER:
                        TWO_PLAYER_SCREEN_DONE = False
                        TWO_PLAYER = False
                    ONE_PLAYER_GIVE_HINT = False
                    ONE_PLAYER_OPTIONAL_HINT = False
                    PLAYER_HINT = ""
                    MAIN_MENU_DONE = False
                    ANSWER = ""
                    GAME_BEGINS = False
                    UNDERSCORE_WORD = ""
                    GUESSES = 0
                    GAME_WIN = False
                    GAME_OVER = False
                    HINT_DENIAL = False
                    AVAILABLE_LETTERS = BASE_LETTERS.copy()
                case "n" | "no":  # IF NO, SAY GOOBYE AND QUIT THE GAME NICELY
                    print("Thank you for playing, have a wonderful day!")
                    sys.exit()
                case _:
                    usage_message()


if __name__ == "__main__":
    main()
