import random
import sys
import os
import time

def random_typing_delay(command):
    for char in command:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0, 0.2))
    sys.stdout.write('\n')

def ghost_command(command):
    if random.random() < 0.1:  # 10% chance to mess with the command
        command = command + random.choice(['x', 'y', 'z'])
    os.system(command)

def change_text_color():
    colors = ["\033[95m", "\033[94m", "\033[92m", "\033[93m", "\033[91m"]
    sys.stdout.write(random.choice(colors))

def surprise_message():
    messages = ["Beware the CLI Devil!", "Did you mean to do that?", "Oops!"]
    sys.stdout.write(random.choice(messages) + '\n')

while True:
    try:
        change_text_color()
        command = input("$ ")
        if random.random() < 0.1:
            random_typing_delay(command)
        elif random.random() < 0.1:
            ghost_command(command)
        elif random.random() < 0.1:
            surprise_message()
        else:
            os.system(command)
    except KeyboardInterrupt:
        sys.stdout.write("\nExiting...\n")
        break
