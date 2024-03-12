import random
import time
from colorama import Fore, Style

simbols = ["*", "$", "@", "#", "%"," ", " ", " ", " ", " "]
color = Fore.GREEN
timewait = 0.0001
while True:
    simbol = random.choice(simbols)
    print(color + simbol + Style.RESET_ALL, end='', flush=True)
    time.sleep(timewait)
