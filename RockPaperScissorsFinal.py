import random
yesno = ['y', 'n']
choices = {1: 'Rock', 2: 'paper', 3: 'Scissors'}
print("GAME RULES: \n"
      "ROCK(1) vs SCISSORS(3)   --> ROCK(1) wins\n"
      "SCISSORS(3) vs PAPER(2)  --> SCISSORS(3) win\n"
      "PAPER(2) vs ROCK(1)      --> PAPER(2) wins)\n")
while True:
    pick = (int(input("hi please type your pick here\n choose 1 ,2 or 3 \n")))
    pc = int(random.randrange(1, 4, 1))
    if pick not in choices.keys():
        print("Please enter number between 1 - 3")
        continue
    if pick == pc:
        print('Its a Tie')
        continue
    elif pick == 1 and pc == 2:
        print(f'PC won!!\n you choose {choices[1]}, and pc choose {choices[2]}\n')

    elif pick == 1 and pc == 3:
        print(f'You won!!\n you choose {choices[1]}, and pc choose {choices[3]}\n')

    elif pick == 2 and pc == 3:
        print(f'PC won!!\n you choose {choices[2]}, and pc choose {choices[3]}\n')

    elif 2 and pc == 1:
        print(f'you won!!\n you choose {choices[2]}, and pc choose {choices[1]}\n')

    elif pick == 3 and 1:
        print(f'PC won!! \n you choose {choices[3]}, and pc choose, {choices[1]}\n')

    else:
        print(f'you won!!\n you choose {choices[3]} and pc choose, {choices[2]}\n')

    n = 1
    restart = str(input('Would you like to restart? y/n'))
    while n == 1:
        if restart == 'n' or restart == 'y':
            n = 0
            break
        else:
            print('not a valid answer')
            restart = str(input('Would you like to restart? y/n'))

    if restart == 'y':
        continue
    else:
        break
