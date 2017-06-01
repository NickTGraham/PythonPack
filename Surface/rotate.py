import sys
import os
import subprocess
import re

status = subprocess.check_output(["xrandr", "-q"])

lines = status.split("\n")
stat = ""

for line in lines:
    if "eDP-1" in line:
        stat = line

orientation = stat.split(" ")[4]

if len(sys.argv) < 2:
    exit()
elif (sys.argv[1] == "-l"):
    if (orientation == "left"):
        subprocess.call(["xrandr", "--output", "eDP-1", "--rotate", "inverted"])
    elif (orientation == "inverted"):
        subprocess.call(["xrandr", "--output", "eDP-1", "--rotate", "right"])
    elif (orientation == "right"):
        subprocess.call(["xrandr", "--output", "eDP-1", "--rotate", "normal"])
    else:
        subprocess.call(["xrandr", "--output", "eDP-1", "--rotate", "left"])
else:
    if (orientation == "left"):
        subprocess.call(["xrandr", "--output", "eDP-1", "--rotate", "normal"])
    elif (orientation == "inverted"):
        subprocess.call(["xrandr", "--output", "eDP-1", "--rotate", "left"])
    elif (orientation == "right"):
        subprocess.call(["xrandr", "--output", "eDP-1", "--rotate", "inverted"])
    else:
        subprocess.call(["xrandr", "--output", "eDP-1", "--rotate", "right"])
