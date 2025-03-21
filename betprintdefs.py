import time  # Library for selecting speed to print characters
import sys  # Library for clearing stdout buffer
from colorama import Fore, Back, Style, init  # Library for coloring strings

init()  # Initialize colorama

# Function to print string with selected speed
def print_str_sellect_spead(string, speed):
    for i in range(len(string)):
        print(string[i], end="")
        sys.stdout.flush()  # Clear stdout buffer to print immediately
        time.sleep(speed)  # Pause for the specified time

# Function to print colored string with selected speed
def print_color_str_sellect_spead(string, color, speed):
    for i in range(len(string)):
        print(color + string[i] + Style.RESET_ALL, end="")
        sys.stdout.flush()  # Clear stdout buffer to print immediately
        time.sleep(speed)  # Pause for the specified time

# Function to print colored string
def print_color_str(string, color):
    print(color + string + Style.RESET_ALL)

def print_str_with_end_select_speed(string, speed, startchar, endchar):
    print(startchar, end="")  # Print the start character without a newline
    for i in range(len(string)):
        print(string[i], end="")  # Print each character of the string without a newline
        sys.stdout.flush()  # Clear stdout buffer to print immediately
        time.sleep(speed)  # Pause for the specified speed (in seconds) before printing the next character
    print(endchar, end="")  # Print the end character without a newline