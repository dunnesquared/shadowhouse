# Shadow House 👻

A supernatural mini text adventure!

![alt text][snapshot]

## How to play from the source code
After cloning or downloading the repo, you can play in one of two ways:

### 1. Run shadowhouse.py.
Navigate to the `shadowhouse` directory and run

```sh
python3 shadowhouse.py
```

OR

### 2. Run the Bash shell script.
This option alters the shell's look and feel, giving it a more 'retro'
aesthetic.

Navigate to `bin` directory and change the permissions of the shell script
to make it executable.

```sh
chmod +x shadowhouse.sh
```

Then run the script by typing the following on the command-line:

```sh
./shadowhouse.sh.
```

## How to play using Docker
Assuming you have Docker installed on your machine, you can start playing without cloning the repo using the following command: 

```sh
docker container run -it --rm --name shadowhouse dunnesquared/shadowhouse
```

## How to see the scoreboard
All winners' scores are written as human-readable text to file
`shadowhouse/scores.dat`. Use your favourite editor or shell utility
to view your final score!

## A note about copyright and licensing
I've let the code fall under the `MIT` license, but retain full rights on
the game's 'creative content' (i.e. narrative, scene descriptions, characters,
etc.). Learn and play with the code as you like, but no copying or altering
of the story text or structure, please.

## Apologies and thanks
Apologies to David Foster Wallace and David Lynch for using their big ideas
for my very small ones.
Thanks to Zed Shaw for providing the impetus and the basics that made
this game possible.
Special thanks to LK for additional dialogue concepts ;-).


[snapshot]: snapshot.jpeg
