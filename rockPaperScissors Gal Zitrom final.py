
import random

print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")
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
