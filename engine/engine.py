from colorama import Fore, init as init_colorama
from engine.attributes import PlayerAttributes
from engine.color import bright,colored
from time import sleep
import pandas as pd


class Game:
    """The main code for runing the game"""

    def __init__(self) -> None:
        self.introduction = "Welcome to the game"
        init_colorama()

    def play(self):
        """Run the game"""
        print(bright(self.introduction))
        sleep(0.5)

    def start_attributes(self,points):
        cp, luck, diplomacy, desert_survival = 0, 0, 0, 0
        save = points

        for j in ['Combat Power', 'Luck', 'Diplomacy', 'Desert Survival']:
            print(f'You have {points} points left')
            while True:  # Keep asking until valid input is provided
                try:
                    print(f'How many points would you like to put in {j}:')
                    a = int(input('Input: '))
                    if 0 <= a <= points:
                        points -= a
                        if j == 'Combat Power':
                            cp += a
                        elif j == 'Luck':
                            luck += a
                        elif j == 'Diplomacy':
                            diplomacy += a
                        elif j == 'Desert Survival':
                            desert_survival += a
                        break  # Break out of the loop if input is valid
                    else:
                        print('You do not have enough points')
                except ValueError:
                    print('Invalid input')

        print(f'You have {cp} points in Combat Power, {luck} points in Luck, {diplomacy} points in Diplomacy, and {desert_survival} points in Desert Survival')
        a = input('Are you happy with your choices? (y/n):')
        if a.lower() in ['yes', 'y']:
            return cp, luck, diplomacy, desert_survival
        else:
            return self.start_attributes(save)   
        
    def choice(self, choices: list[str], message: str) -> str:
        """Get the player's choice"""
        print(colored(Fore.LIGHTWHITE_EX, message))
        colnamee = ['id', 'choices','description','impacct']
        df = pd.read_csv('choices.csv', names = colnamee)

        df = df.loc[df['id'].isin(choices)]
        pd.options.display.max_colwidth = 150
        for i in range(len(choices)):
            print(f'{colored(Fore.GREEN ,str(i+1))}. {df.iloc[i,1]} ')
        while True:
            try:
                choice = int(input('Enter the number of your choice: '))
                if 0 < int(choice) <= len(  choices):
                    return df.iloc[choice - 1,0]
                elif choice == 99:
                    for i,j in enumerate( df['description']):
                        print(f'{colored(Fore.GREEN ,str(i + 1))}. {j} ')
                elif choice == 98:
                    pd.options.display.max_colwidth = 400
                    for i,j in enumerate( df['impacct']):
                        print(f'{colored(Fore.GREEN ,str(i + 1))}. {j} \n')
                else:
                    print(colored(Fore.LIGHTRED_EX, 'Invalid choice.'))
            except ValueError:
                print(colored(Fore.LIGHTRED_EX, 'Invalid adadasdchoice.'))
        
            
