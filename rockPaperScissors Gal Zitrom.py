# Rock Paper Scissors
# A code file structure:
# A line that starts with "#"  is a comment line (it will not be interpreted)
"""
If you ant to comment multiple lines, start and finish with three (3) double quotes (")
As you can see, this line is also a comment.

"""

# ----------------------------------------------------------------------------------------------------------------------
# Here you include all of your package imports (like random and time packages wev'e discussed about)
# ----------------------------------------------------------------------------------------------------------------------
import random

# ----------------------------------------------------------------------------------------------------------------------
# Here you will write all of the functions (for later stages of the course
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Here you write code :)
# ----------------------------------------------------------------------------------------------------------------------
"""
I'll give you the text inputs for this program, to make your lives a little easier.
In addition, and to make it simple to you, the input from the user will be an integer:
1 for ROCK
2 for PAPER
3 for SCISSORS
A text input describing the operation is unacceptable and will cost you with points.

A quick reminder of the rules:

ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins
SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win
PAPER(2) vs ROCK(1)      --> PAPER(2) wins

DO NOT ADD EXTRA OPTIONS (No lizard, no Spock.)
"""

# print the instructions for the user to see:
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")

# The game will run in a WHILE loop.
# The loop is infinite, and only the user has the power to stop it (when they say they don't want to play anymore)
while True:
    Rock = 1
    Paper = 2
    Scissors = 3
    play = 'would you like to start? y/n\n'
    start = input(play)
    if str(start.lower()) == 'y':
        pick = (int(input("hi please type your pick here \n choose '1' ,'2' or '3'")))
        choices = [1, 2, 3]
        pc = random.choice(choices)

        if pick == pc:
            print('Its a tie!\n')
        elif pick == Rock and pc == Paper:
            print('you lost he chose Paper\n')
        elif pick == Rock and pc == Scissors:
            print('you won he chose Scissors\n')
        elif pick == Paper and pc == Scissors:
            print('you lost he chose Scissors\n')
        elif pick == Paper and pc == Rock:
            print('you won he chose Rock\n')
        elif pick == Scissors and pc == Rock:
            print('You lost he chose Rock\n')
        else:
            print('You won he chose Paper')

    elif start.lower() == 'n':
        break
    else:
        input("Please press y/n\npress any key to restart\n")
