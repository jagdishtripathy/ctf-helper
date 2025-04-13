from pyfiglet import Figlet
from termcolor import colored

def print_banner():
    f = Figlet(font='slant')
    banner_text = f.renderText('CTF Helper')
    print(colored(banner_text, 'cyan'))
    print(colored("Author: Jagadish | Version: 1.0", 'yellow'))
    print(colored("A Swiss Army Knife for CTFs & Cybersecurity Tasks\n", 'green'))
