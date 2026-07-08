from art import *
import subprocess
from hang import UNDERSCORE_WORD, GAME_BEGINS, AVAILABLE_LETTERS

subprocess.call(["cls"],shell=True)

help_screen_menu()
one_player_screen()
two_player_screen()
main_menu_screen()
game_over_screen()
you_win_screen()