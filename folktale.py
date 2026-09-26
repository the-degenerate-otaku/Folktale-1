import random 
import math
import time


def type_print(text1, delay=0.05):
    for char in text1:
     print(char, end='', flush=True)
     time.sleep(delay)
print()

text1=(
    """
    Hello Adventurer How do you do? Welcome to Avegard, A World filled with Monsters, Dragon, Magic and More 
    Firstly, Would you mind Telling me your name?
    """
)

type_print(text1)


name = str(input("Please enter your name:"))

# wait i can just ddirectly upload to