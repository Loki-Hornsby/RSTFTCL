import time
import string
import random
import os
import pathlib

file = "Tracker.txt"
lineclr = 25

# Lazy functions
def get_current_file():
    return str(os.path.abspath(os.getcwd())) + "\\" + file

def clearline():
    return " " * lineclr

def sleep(t):
    time.sleep(t)

def newline():
    print("\n", end="\b")

def play_fancy_animation(animation, t, end):
    if (end == -1):
        end = len(animation)
    
    i = 0

    while i < end:
        print(animation[i % len(animation)], end="\r")
        time.sleep(t)
        i += 1

def id_generator(size, chars = string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def apply_encryption_effect(s, t=0.01, end=10):
    animation = []
        
    for i in range(end):
        animation.append(id_generator(len(s)))
            
    animation.append(clearline())
    animation.append(s)
        
    play_fancy_animation(animation, t, -1)

    newline()

def write_to_file(s):
    f = open(file, "a")
    f.write(s + "\n\n")
    f.close()

def get_format_from_data(s):
    output = time.strftime("==== [%H:%M] [%Y.%m.%d] ====") + "\n"

    if (s == None or s == ""):
        s = "I inputted nothing into the tracker 2000 and it gave me sass!";
    
    try:
        for line in s.split("~"):
            output += "- " + line + "\n"
    except:
        output += "- " + s + "\n"
        
    return output

def ask_for_input():
    store = input(">> ").lower()

    if (store == "x"):
        quit()

    return store

def ask_for_data():
    # Input
    apply_encryption_effect("> Current file is located at " + get_current_file())
    apply_encryption_effect("> Write what you have done here")
    apply_encryption_effect("> Seperate multiple items with a tilde (~)")
    apply_encryption_effect("> Type 'x' to cancel")

    return ask_for_input()

def spam():
    s = """
  _______ _    _ ______   _______ _____            _____ _  ________ _____    ___   ___   ___   ___  
 |__   __| |  | |  ____| |__   __|  __ \     /\   / ____| |/ /  ____|  __ \  |__ \ / _ \ / _ \ / _ \ 
    | |  | |__| | |__       | |  | |__) |   /  \ | |    | ' /| |__  | |__) |    ) | | | | | | | | | |
    | |  |  __  |  __|      | |  |  _  /   / /\ \| |    |  < |  __| |  _  /    / /| | | | | | | | | |
    | |  | |  | | |____     | |  | | \ \  / ____ \ |____| . \| |____| | \ \   / /_| |_| | |_| | |_| |
    |_|  |_|  |_|______|    |_|  |_|  \_\/_/    \_\_____|_|\_\______|_|  \_\ |____|\___/ \___/ \___/ 
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    """                                                                                                                                              

    for i in range(100):
        print(" " * lineclr)

    print(s)

def Startup():
    # Change console size and color
    os.system('mode 125,' + str(lineclr))
    os.system('color 5E')

    # Show logo
    spam()
    
    # Animations
    bar = [
        clearline(),
        "Loading.        ",
        " Loading..      ",
        "  Loading...    ",
        "   Loading....  ",
        "  Loading...    ",
        " Loading..      ",
        "Loading.        "
    ]

    tracker = [
        clearline(),
        "T",
        clearline(),
        "TH",
        clearline(),
        "THE",
        clearline(),
        "THE ",
        clearline(),
        "THE T",
        clearline(),
        "THE TR",
        clearline(),
        "THE TRA",
        clearline(),
        "THE TRAC",
        clearline(),
        "THE TRACK",
        clearline(),
        "THE TRACKE",
        clearline(),
        "THE TRACKER",
        clearline(),
        "THE TRACKER ",
        clearline(),
        "THE TRACKER 2",
        clearline(),
        "THE TRACKER 20",
        clearline(),
        "THE TRACKER 200",
        clearline(),
        "THE TRACKER 2000",
        clearline(),
        "THE TRACKER 2000",
        clearline(),
        "THE TRACKER 2000",
    ]

    # Fancy Startup
    play_fancy_animation(bar, 0.1, 25)
    play_fancy_animation(tracker, 0.05, -1)

# Start program
Startup()

# First Confirmation
inp = None

while inp != "x":
    # Input
    inp = ask_for_data()
    
    # Preview output
    print("\n" + "> Output will be: ")
    v = get_format_from_data(inp)
    print(v)

    # Second confirmation
    print("> Are you sure? y/n")

    y = ask_for_input()

    if y == "y":
        write_to_file(v)
        print("Wrote to file! closing...")
        sleep(5)

        inp = "x"
    else: # Add space
        spam()
                    
# Exit
quit()
