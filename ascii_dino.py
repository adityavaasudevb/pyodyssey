try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    use_color = True
except ImportError:
    use_color = False

import random

def greet():
    dino_art = r"""
                      __
                     / _)
           _.----._/ /
         /         /
      __/ (  |  (  |
     /__.-'|_|--|_|
    """
    greetings = [
        ">>> Welcome to Pyodyssey 🦖",
        ">>> Explore. Code. Repeat.",
        ">>> Logic, chaos, dinosaurs 🧠🔥",
        ">>> Keep your bugs friendly 💻",
        ">>> This repo bites...in a good way 🧪🦕"
    ]

    print(Fore.MAGENTA + Style.BRIGHT + dino_art if use_color else dino_art)
    print(Fore.GREEN + Style.BRIGHT + random.choice(greetings) if use_color else random.choice(greetings))

if __name__ == "__main__":
    greet()


