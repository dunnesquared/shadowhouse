#!/bin/bash

# Launch Shadow House

# Set size of window: rows columns
resize -s 49 75

#Clear terminal/console window
clear

# Set background of terminal window to black (can't assume user has
# this pre-selected)
tput setab 0

# Set font to bold; set colour. Go to Wikipedia/Google "tput" for more colours
tput bold
tput setaf 7 # white

# Run Python file
python3 ../shadowhouse/shadowhouse.py
