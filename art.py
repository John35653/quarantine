"""For now this is where all of the basic art will be stored for the hangman game"""

# pylint: disable=anomalous-backslash-in-string


def beginning() -> None:  # pylint: disable=missing-function-docstring
    print("""
_______
   |   
   |   
   |   
   |   
¯¯¯¯¯¯¯
""")


def first_wrong() -> None:  # pylint: disable=missing-function-docstring
    print("""
_______
   |  O
   |   
   |   
   |   
¯¯¯¯¯¯¯
""")


def second_wrong() -> None:  # pylint: disable=missing-function-docstring
    print("""
_______
   |  O
   |  |
   |   
   |   
¯¯¯¯¯¯¯
""")


def third_wrong() -> None:  # pylint: disable=missing-function-docstring
    print("""
_______
   |  O
   | \\|
   |   
   |   
¯¯¯¯¯¯¯
""")


def fourth_wrong() -> None:  # pylint: disable=missing-function-docstring
    print("""
_______
   |  O
   | \\|/
   |   
   |   
¯¯¯¯¯¯¯
""")


def fifth_wrong() -> None:  # pylint: disable=missing-function-docstring
    print("""
_______
   |  O
   | \\|/
   |   \\
   |   
¯¯¯¯¯¯¯
""")


def final_wrong() -> None:  # pylint: disable=missing-function-docstring
    print("""\033[91m
_______
   |  O
   | \\|/
   | / \\
   |   
¯¯¯¯¯¯¯\033[0m
""")


def main_menu_screen() -> None:  # pylint: disable=missing-function-docstring
    print("""\033[91m
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      \033[0m                


At any point in time if you want to \033[1;93mquit the game\033[0m, type \033[1;93mExit\033[0m or \033[1;93mexit\033[0m

Please make your selection from the options below by typing the letter
on the left side of the ')':

O)ne Player - Ready to challenge yourself?
T)wo Player - In case you want to challenge a friend
\033[93mH)elp - Rundown on how the game works\033[0m
\033[31mE)xit\033[0m

""")


def one_player_screen() -> None:  # pylint: disable=missing-function-docstring
    print("""\033[91m
 _____             ______ _                       
|  _  |            | ___ \ |                      
| | | |_ __   ___  | |_/ / | __ _ _   _  ___ _ __ 
| | | | '_ \ / _ \ |  __/| |/ _` | | | |/ _ \ '__|
\ \_/ / | | |  __/ | |   | | (_| | |_| |  __/ |   
 \___/|_| |_|\___| \_|   |_|\__,_|\__, |\___|_|   
                                   __/ |          
                                  |___/         \033[0m  


\033[92mE)asy - Hints to what the word is.\033[0m
\033[93mM)edium - Optional hints to what the word is.\033[0m
\033[91mH)ard - No hints to the word whatsoever.\033[0m
B)ack - Takes you back to the main menu.

""")


def two_player_screen() -> None:  # pylint: disable=missing-function-docstring
    print("""\033[91m
 _____              ______ _                       
|_   _|             | ___ \ |                      
  | |_      _____   | |_/ / | __ _ _   _  ___ _ __ 
  | \ \ /\ / / _ \  |  __/| |/ _` | | | |/ _ \ '__|
  | |\ V  V / (_) | | |   | | (_| | |_| |  __/ |   
  \_/ \_/\_/ \___/  \_|   |_|\__,_|\__, |\___|_|   
                                    __/ |          
                                   |___/           \033[0m


B)ack - Takes you back to the main menu.

""")


def you_win_screen() -> None:  # pylint: disable=missing-function-docstring
    print("""\033[92m
__   __            _    _ _         _ _ 
\ \ / /           | |  | (_)       | | |
 \ V /___  _   _  | |  | |_ _ __   | | |
  \ // _ \| | | | | |/\| | | '_ \  | | |
  | | (_) | |_| | \  /\  / | | | | |_|_|
  \_/\___/ \__,_|  \/  \/|_|_| |_| (_|_)   \033[0m
                                      
                                      
""")


def game_over_screen() -> None:  # pylint: disable=missing-function-docstring
    print("""\033[91m
 _____                        _____                        __
|  __ \                      |  _  |                  _   / /
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __   (_) | | 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|      | | 
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |      _  | | 
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|     (_) | | 
                                                          \_\  \033[0m
                                                          

""")
