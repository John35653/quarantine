"""This is where the magic happens for the hangman game which I'm using to learn some Python"""

import random
import os
import subprocess
import sys
import time
from art import *  # pylint: disable=wildcard-import

POSSIBLE_WORDS_1P: dict = (
    [  # TODO: maybe change this to a dict to be able to give hints
        "hello",
        "goodbye",
        "pancake",
        "syrup",
        "eggs",
        "coffee",
        "hamster",
        "video",
    ]
)

# POSSIBLE_WORDS_1P: dict = (
#     {  # TODO: maybe change this to a dict to be able to give hints
#         "hello":"A greeting",
#         "goodbye": "A farewell",
#         "pancake": "A breakfast item",
#         "syrup": "A condiment that goes on top of a breakfast food",
#         "eggs": "An animal makes this",
#         "coffee": "Something that you drink in the morning",
#         "hamster": "A pet that you may give to your child",
#         "video": "Something that you watch"
#     }
# )

# COPY_OF_WORDS = POSSIBLE_WORDS_1P.copy()
# print(COPY_OF_WORDS)
# theanswer = random.choice(list(COPY_OF_WORDS))
# print("\n\n\n" + theanswer)
# print(COPY_OF_WORDS[theanswer])

# time.sleep(10)

BASE_LETTERS = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

AVAILABLE_LETTERS = BASE_LETTERS.copy()

MAIN_MENU_DONE: bool = False
ANSWER: str = ""
ONE_PLAYER_SCREEN_DONE: bool = False
TWO_PLAYER_SCREEN_DONE: bool = False
ONE_PLAYER: bool = False
TWO_PLAYER: bool = False
ONE_PLAYER_GIVE_HINT: bool = False
ONE_PLAYER_OPTIONAL_HINT: bool = False
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
        user_answer (str): The answer that the user gives when prompted for input
    """
    if user_answer == "exit":
        exit_message()
        time.sleep(1)
        sys.exit()


def usage_message() -> None:
    """A generic message telling the user they didn't give the right answer
    and need to try again.
    """
    print("\nThat is not a valid option. Please choose from the possible options\n")
    time.sleep(1.5)


def main() -> None:
    """This is the main function of the hangman program"""
    global ONE_PLAYER_SCREEN_DONE, TWO_PLAYER_SCREEN_DONE, ONE_PLAYER, ONE_PLAYER_GIVE_HINT
    global TWO_PLAYER, GUESSES, MAIN_MENU_DONE, DIFFICULTY_CHOICE, UNDERSCORE_WORD
    global ONE_PLAYER_OPTIONAL_HINT, PLAYER_HINT, ANSWER, GAME_BEGINS, GAME_OVER, GAME_WIN
    global AVAILABLE_LETTERS

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
                        ANSWER = random.choice(POSSIBLE_WORDS_1P)
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
                                break
                            case "n" | "no":
                                ANSWER = input(
                                    "Please enter the word you want the user to guess: "
                                ).lower()
                                TWO_PLAYER = True
                                TWO_PLAYER_SCREEN_DONE = True
                                MAIN_MENU_DONE = True
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
                    # TODO make a help screen, just for funsies
                    print("""
At any given time, you can type Exit or exit to quit the program.
At the Main Menu however you can just type Exit/exit/E/e to quit the program.
If you choose just one player, you can choose between Easy, Medium, or Hard.
Easy will give you a hint that you can see at all times, Medium will allow
you to see the hint once you type Hint or hint during the game. Hard provides no hint 
at all. If you choose the two player option, a person can both choose the word 
for you as well as if they want to give you a hint or even no hint at all >:D. 

Press enter to go back to the Main Menu.

Enjoy!!! 787482
                    """)
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

            # usage_message()
        # ---------------------------------------END-OF-MAIN-MENU-----------------------------------
        # ------------------------------------------GAME-BEGINS-------------------------------------
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

            # PRINTING THE HIDDEN WORD AND THE AVAILABLE LETTERS LEFT TO USE
            if not GAME_BEGINS:
                UNDERSCORE_WORD = "_" * len(ANSWER)
                GAME_BEGINS = True
            print(UNDERSCORE_WORD + "     Guesses left: " + str(6 - GUESSES))
            print("\nAvailable Letters:")
            for letter in AVAILABLE_LETTERS:
                print(letter.upper(), end=" ")



            print(ANSWER)  # TODO: remove before finishing

                            #get char from the user
            guessed_char = input(
                "\nPlease enter your choice from Available Letters: "
            ).lower()
            exit_check(guessed_char)
            if len(guessed_char) > 1:
                usage_message()
                continue

                        # checking to see if the char is available
            if guessed_char not in AVAILABLE_LETTERS:
                print("You have already guessed that letter. Please try again.")
                time.sleep(1.5)
                continue


                        # removing the char from the available letters
            for i, char in enumerate(AVAILABLE_LETTERS):
                if guessed_char == char:
                    AVAILABLE_LETTERS[i] = "_"
                    break


            if guessed_char in ANSWER:
                new_word = ""
                for i, char in enumerate(ANSWER):
                    if guessed_char == char:
                        new_word += guessed_char
                    else:
                        new_word += UNDERSCORE_WORD[i]
                UNDERSCORE_WORD = new_word
                if UNDERSCORE_WORD == ANSWER:
                    you_win_screen()
                    GAME_WIN = True
                    break
                continue



            elif guessed_char not in ANSWER:
                GUESSES += 1
                if 0 < GUESSES < 6:
                    print("That is not correct. Plase try again.")
                    time.sleep(1.5)
                elif GUESSES == 6:
                    print("Oops, you're all out of guesses.")
                    time.sleep(1.5)
                    break
                continue
            elif GUESSES:
                pass


        while GAME_OVER or GAME_WIN:
            # TODO: placeholder for asking if the player would like to play again, this is not working right now
            user_answer = input("Would you like to play again? ( Y)es or N)o ): ")
            exit_check(user_answer)
            # TODO: reset flags and variables to their previous state if the user wants to play again, use
            # ONE_PLAYER and TWO_PLAYER flags
            match user_answer:
                case "y" | "yes":
                    if ONE_PLAYER:
                        ONE_PLAYER_SCREEN_DONE = False
                        ONE_PLAYER = False
                        ONE_PLAYER_GIVE_HINT = False
                        ONE_PLAYER_OPTIONAL_HINT = False
                        DIFFICULTY_CHOICE = ""
                    if TWO_PLAYER:
                        TWO_PLAYER_SCREEN_DONE = False
                        TWO_PLAYER = False
                    PLAYER_HINT = ""
                    MAIN_MENU_DONE = False
                    ANSWER = ""
                    GAME_BEGINS = False
                    UNDERSCORE_WORD = ""
                    GUESSES = 0
                    GAME_WIN = False
                    GAME_OVER = False
                    AVAILABLE_LETTERS = BASE_LETTERS.copy()
                case "n" | "no":
                    print("Thank you for playing, have a wonderful day!")
                    sys.exit()
                case _:
                    usage_message()


if __name__ == "__main__":
    main()

    # TODO: remove before finishing
    # AVAILABLE_LETTERS = [
    #     "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    #     "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    #     ]     this is for when black makes the list super long height wise, just copy and paste this instead of manually fixing

# TODO: need to make a copy of AVAILABLE_LETTERS that can be changed on when the player is playing
# and if the user chooses to play again, the copy can be taken off of the stack and a new copy can
# be made for the new game, also need to work on giving the player hints


# TODO: CONTINUE WORKING ON THE PLAYER BEING ABLE TO RESTART THE GAME IF THEY CHOOSE TO PLAY AGAIN
