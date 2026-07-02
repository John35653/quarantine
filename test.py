from art import *
import subprocess
from hang import UNDERSCORE_WORD, GAME_BEGINS

subprocess.call(["cls"],shell=True)

main_menu_screen()
one_player_screen()
two_player_screen()
game_over_screen()