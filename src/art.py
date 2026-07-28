"""For now this is where all of the basic art will be stored for the hangman game"""
# pyright: reportInvalidStringEscapeSequence=false
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

def help_screen_menu() -> None: # pylint: disable=missing-function-docstring
    print("""\033[1;93m
 _   _      _        
| | | |    | |       
| |_| | ___| |_ __   
|  _  |/ _ \ | '_ \  
| | | |  __/ | |_) | 
\_| |_/\___|_| .__/  
             | |     
             |_|     \033[0m


At any given time, you can type \033[1;93mExit\033[0m or \033[1;93mexit\033[0m to quit the program.
At the Main Menu however you can just type \033[1;93mExit/exit/E/e\033[0m to quit the program.
In fact, for a majority of menu options you can also just spell out the whole word. Ex: O)ne can 
be selected by either typing 'o' or "one", T)wo being either 't' or "two", etc.
If you choose just one player, you can choose between \033[1;93mEasy, Medium, or Hard\033[0m.

-\033[92mEasy\033[0m will give you a \033[95mhint\033[0m that you can see at all times.
-\033[93mMedium\033[0m will allow you to see the \033[95mhint\033[0m once you type \033[1;95mHint\033[0m or \033[1;95mhint\033[0m during the game. 
-\033[91mHard\033[0m provides no \033[95mhint\033[0m at all. 

If you choose the two player option, a person can both choose the word 
for you as well as if they want to give you a hint or even no hint at all >:D. 

Enjoy!!! 787482

Press enter to go back to the Main Menu.
""")


def one_player_screen() -> None:  # pylint: disable=missing-function-docstring
    print("""\033[1;91m
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
    print("""\033[1;91m
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
    print("""\033[1;92m
__   __            _    _ _         _ _ 
\ \ / /           | |  | (_)       | | |
 \ V /___  _   _  | |  | |_ _ __   | | |
  \ // _ \| | | | | |/\| | | '_ \  | | |
  | | (_) | |_| | \  /\  / | | | | |_|_|
  \_/\___/ \__,_|  \/  \/|_|_| |_| (_|_)   \033[0m
                                      
                                      
""")


def game_over_screen() -> None:  # pylint: disable=missing-function-docstring
    print("""\033[1;91m
 _____                        _____                        __
|  __ \                      |  _  |                  _   / /
| |  \/ __ _ _ __ ___   ___  | | | |_   _____ _ __   (_) | | 
| | __ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|      | | 
| |_\ \ (_| | | | | | |  __/ \ \_/ /\ V /  __/ |      _  | | 
 \____/\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|     (_) | | 
                                                          \_\  \033[0m
                                                          

""")

def hangman_saved() -> None: # pylint: disable = missing-function-docstring
    print("""\033[1;92m
                0
               \\|/     YAY!!! I'M SAVED
               / \\     \033[0m
          
""")
