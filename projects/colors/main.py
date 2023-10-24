from termcolor import colored, COLORS
from pyfiglet import figlet_format, COLOR_CODES

text = input('What word do you want to print?: ')

color = input('What color do you want to print?: ')
if color not in COLORS:
    raise TypeError('color not supported')


def print_text(text, color):
    print(colored(figlet_format(text), color=color))


print_text(text, color)
