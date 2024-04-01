from engine.engine import Game
from dataclasses import dataclass, field
import engine.color as color
from engine.attributes import PlayerAttributes
import events as ev
import sys
import os

player = PlayerAttributes()

class Test(Game):
    def __init__(self):
        super(Test, self).__init__()

    def game_over(self):
        print(color.colored('red', """
          ____                                            _ 
         / ___| __ _ _ __ ___   ___    _____   _____ _ __| |
        | |  _ / _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__| |
        | |_| | (_| | | | | | |  __/ | (_) \ V /  __/ |  |_|
         \____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|  (_)
        """))

        print('\nWould you like to play again?')
        a = input('y/n: ')
        if a.lower() in ['yes', 'y']:
            self.play()
        else:
            print('Goodbye')
            sys.exit()


    def main(self, paths):
        # Choice of path
        path = Game.choice(self, paths, 'What path do you choose?')

        if path == 'p1':
            print(color.bright('You chose path of Desert'))
            print("As Paul surveyed new territories on his thopter, the vast desert stretched below like a sea of sand dunes.")
            print("Without warning, a critical node malfunctioned, sending the craft into a spiraling descent.")
            print("Paul grappled with the controls, trying to regain stability, but it was too late.")
            print("The thopter plummeted towards the desert, slamming into the sand with a deafening crash, kicking up a cloud of dust and debris.\n\n")

            if ev.survival_challenge(10,10): # water, distance_to_safety 
                choice = Game.choice(self, ['d1','d2'], 'What would you like to do?')
                if choice == 'd2':
                    print('You have chosen to save yourself.')
                    player.change_attributes('Allegiance', -30)
                print("\n\nYou've chosen the burdens of the people over your own. Now, it's just a matter of reaching your own.")
                print('But The path ahead is treacherous.')

                if player.return_attributes()['Desert Survival'] >= 2 and player.return_attributes()['Luck'] >= 2:
                    print('You have the skills to survive.')

                    print("Paul sees a small settlement of Fremen in the distance, ahead of him lies a choice.")
                    choice = Game.choice(self, ['d3','d4'], 'What path do you choose?')
                    if choice == 'd3':
                        print("Upon arriving at the Fremen settlement, Paul is greeted cautiously by the inhabitants.")
                        print("The leader of the Fremen steps forward, his demeanor stern yet curious.")
                        print("'Welcome, stranger,' he begins. 'We have heard of your arrival and wish to ascertain your intentions.'")
                        print("Paul meets the leader's gaze with a steady one of his own.")
                        print("'I am Paul Atreides,' he replies. 'My family's home has been taken from us, and I seek refuge and allies.'")
                        print("The Fremen leader nods. 'Very well, Paul Atreides,' he says. 'But words alone are not enough to earn our trust.'")
                        print("With that, the Fremen begin to pose a series of questions to Paul.")

                        score = ev.quizz('questions.txt')    

                        if score == 4 and player.return_attributes()['Allegiance'] >= 70:
                        
                            print("As the questioning comes to an end, the Fremen leader nods approvingly.")
                            print("You have shown yourself to be a man of honor and integrity, Paul Atreides,' he says.")
                            print("You are welcome among us. But remember, our trust is not easily earned, and it can be just as easily lost. Do not betray it.")  
                            print("With that, Paul is welcomed into the fold of the Fremen, his journey taking on new purpose and meaning as he joins them in their struggle against their common enemies.")
                            player.change_attributes('Allegiance', 30)
                        else:
                            print("Upon realizing that Paul had not answered all the questions correctly, the Fremen leaders deliberated among themselves.")
                            print("They also recognized the potential benefits of aligning themselves with someone of Paul's background and influence.")
                            print("In a show of goodwill and pragmatism, the Fremen decided to extend their assistance to Paul.")
                            print("They provided him with supplies, guidance, and safe passage through their territory.")
                            print("As Paul continued his journey, he reflected on the unexpected kindness of the Fremen.")
                            print("He vowed to repay their generosity by standing with them in their struggles and offering his aid whenever needed.")
                            player.change_attributes('Allegiance', -15)

                    
                    else:
                        print("Upon arriving at the Fremen settlement, Paul attempts to leverage his high status and influence to persuade them to accept him into their ranks.")
                        print("He addresses the gathered crowd with confidence and conviction, but his words fail to resonate with the inhabitants.")
                        print("The leader of the Fremen, sensing Paul's attempt to manipulate them with his status, sternly rejects his overtures and calls for sincerity and humility before the people.")
                        print("Realizing his plan has backfired, Paul is faced with the bitter realization of his misguided actions.")
                        print("With a heavy heart, he leaves the Fremen settlement, acknowledging that his pride and ambition have only worsened his situation.")
                        print("Alone in the desert once more, Paul is stripped of both his high status and the support of the Fremen.")
                        player.change_attributes('Allegiance', -30)

                else:
                    print('You do not have the skills to survive.')
                    self.game_over()

                paths.remove('p1')
                self.main(paths=paths)
            else: self.game_over()
        elif path == 'p3':
            print('                 __')
            print('                /  \\')
            print('               /    \\')
            print('              /      \\')
            print('             /        \\')
            print('            /__________\\')
            print('           /____________\\')
            print('          /_____/  \\_____\\')
            print('         /      /    \\    \\')
            print('        /      /______\\    \\')
            print('       /      /        \\    \\')
            print('      /______/__________\\____\\')
            print('You chose path of ')
            print("The day had been challenging, and Paul needed to rest for at least a couple of hours to regain his strength.")
            print("As he settled down to rest, Paul began to drift into sleep.")
            print("\nWhile resting, Paul started to experience strange visions.")
            print("His mind was filled with images and sensations that seemed to blur the lines between reality and dreams.")

            vision = ev.VisionGame()
            if vision.play():
                player.change_attributes('Happiness', 10)
            print("As the visions faded, Paul found himself back in the harsh reality of the desert.")
            print("The experience had left him feeling disoriented and drained, but he knew he had to press on.")
            print('Interpretation of Visions:')
            choice = Game.choice(self, ['v1','v2'], 'What do you choose?')
            if choice == 'v1':
                print("Paul decided to interpret the visions as a sign of his destiny and the path he must follow.")
                print("He resolved to embrace the unknown and forge his own destiny, trusting in the guidance of the visions.")
                player.change_attributes('Allegiance', 10)
            else:
                print("Despite the unsettling nature of the vision, Paul chooses to dismiss it as mere speculation and carry on with his usual duties. He rationalizes that indulging in cryptic visions would only distract him from the pressing matters at hand.")
                print("Doubt gnaws at his resolve, and he finds himself second-guessing his choice. Despite his efforts to suppress it, the vision lingers in the back of his mind, casting a shadow over his decisions and actions.")
                print("As events unfold, Paul begins to notice unsettling parallels between the vision and the unfolding reality. He realizes, too late, that his dismissal of the vision was a grave mistake. The signs he ignored manifest in unexpected ways, posing a grave threat to his family and kingdom.")
                print("Caught off guard by the unfolding crisis, Paul scrambles to rally his forces and mitigate the damage. However, his delayed response and lack of preparation leave them vulnerable to the machinations of their enemies. The kingdom faces chaos and upheaval as Paul grapples with the consequences of his decision to dismiss the vision.")
                self.game_over()
            
            paths.remove('p3')
            self.main(paths=paths)
            
        #Endings
        end_attributes = player.return_attributes()
        if end_attributes['Allegiance'] >= 90 and end_attributes['Happiness'] >= 80  and end_attributes['Needs'] >= 70:
            print("     __         __")
            print("    /  \\      /  \\")
            print("  /      \\  /      \\")
            print(" /   \\  /\\/  \\/\\/\\   ")
            print("/_______\\/_/\\/\\_\\_\\")
            print("/________________________\\")
            print("\nDespite facing numerous challenges, including political intrigue and external threats, your unwavering commitment to your people pays off.")
            print("Through shrewd diplomacy and benevolent leadership, you foster a strong sense of unity among the freemen.")
            print("Your dedication to their well-being earns you their undying loyalty and respect.\n")
            print("As a result, the alliance of freemen becomes a formidable force, capable of withstanding any adversary.")
            print("Together, you successfully navigate the treacherous political landscape of Dune, securing peace and prosperity for your people.")
            print("Your legacy as a wise and compassionate leader endures for generations to come, ensuring a bright future for the freemen and their descendants.")

        elif end_attributes['Allegiance'] >= 60 and end_attributes['Happiness'] >= 50  and end_attributes['Needs'] >= 40:
            print("    .--.")
            print("   |o_o |")
            print("   |:_/ |")
            print("  //   \ \ ")
            print(" (|     | )")
            print("/'\_   _/`\ ")
            print("\___)=(___/") 

            print("\nDespite your best efforts, maintaining cohesion among the freemen proves to be a daunting task.")
            print("Internal divisions and external pressures threaten to tear the alliance apart.")
            print("While you manage to stave off complete collapse, the freemen struggle to overcome the myriad challenges they face.")
            print("As resources dwindle and tensions escalate, the alliance teeters on the brink of collapse.")
            print("Although you manage to eke out some semblance of stability, it comes at a great cost.")
            print("The freemen endure hardship and suffering, their hopes for a better future fading with each passing day.")
            print("Your leadership is marked by resilience in the face of adversity, but the road ahead remains uncertain and fraught with peril.")

        else:
            print("\nYour rule over the freemen descends into chaos and despair.")
            print("Internal strife and external threats erode the alliance, leaving it fractured and vulnerable.")
            print("Your inability to address the needs and grievances of your people leads to widespread disillusionment and unrest.")
            print("As dissent simmers and tensions reach a boiling point, violence erupts across Dune.")
            print("The alliance collapses under the weight of its own divisions, plunging the freemen into a state of chaos and anarchy.")
            print("Your legacy is one of failure and despair, as the dreams of a united front against tyranny are dashed on the rocks of bitter infighting and betrayal.")
            self.game_over()

    def play(self):
        # Clearing the Screen
        Game.clear_screen(self)

        # introduction
        print(color.bright('Welcome to Dune: The Desert Planet'))
        print('In this game, you will embark on a journey through the harsh desert landscape of the planet Dune.')
        print('Your choices will determine the fate of your people and the future of your people.\n')

        # skill selection
        points = 10 # total points
        print(color.bright(f'Select your skills, you have {points} points to spend, choose wisely:'))

        # Adding to the player's attributes
        cp, luck, diplomacy, desert_survival =  Game.start_attributes(self,points)
        player.add_attributes({'Combat Power': cp, 'Luck': luck, 'Diplomacy': diplomacy, 'Desert Survival': desert_survival})
        player.add_attributes({'Allegiance': 70, 'Happiness': 50, 'Needs': 70})
        
        # Choice and start of the game
        print(player.return_attributes())
        self.main(paths= ['p1','p2','p3']) #see the paths in the choices.csv file


if __name__ == '__main__':
    game = Test()
    game.play()
