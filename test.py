from art import *
import subprocess
from hang import UNDERSCORE_WORD, GAME_BEGINS, AVAILABLE_LETTERS

subprocess.call(["cls"],shell=True)

hello = ["h","e","l","l","o"]
helloCopy = hello.copy()
print(helloCopy)
helloCopy[2] = "x"
print(hello)
print(helloCopy)
helloCopy = hello.copy()
print(helloCopy)