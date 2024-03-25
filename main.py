from engine.engine import Game
from dataclasses import dataclass, field
from engine.attributes import PlayerAttributes as ea
import events as ev
import sys


player = ea()

class Test(Game):
    def __init__(self):
        super(Test, self).__init__()

    def game_over(self):
        print('Game Over')
        print('Would you like to play again?')
        a = input('y/n: ')
        if a.lower() in ['yes', 'y']:
            self.play()
        else:
            print('Goodbye')
            sys.exit()


    def main(self, paths):
        print(1)
        path = Game.choice(self, paths, 'What path do you choose?')
        if path == 'p1':
            print('You chose path of Desert')
            print("As Paul surveyed new territories on his thopter,")
            print("the vast desert stretched below like a sea of sand dunes.")
            print("Without warning, a critical node malfunctioned,")
            print("sending the craft into a spiraling descent.")
            print("Paul grappled with the controls, trying to regain stability,")
            print("but it was too late. The thopter plummeted towards the desert,")
            print("slamming into the sand with a deafening crash,")
            print("kicking up a cloud of dust and debris.")
            if ev.survival_challenge(10,10): # water, distance_to_safety - need to change them
                choice = Game.choice(self, ['d1','d2'], 'What would you like to do?')
                if choice == 'd2':
                    print('You have chosen to save yourself.')
                    player.change_attributes('Allegiance', -30)
                print("You've chosen the burdens of the people over your own. Now, it's just a matter of reaching your own.")
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
                        print(score, player.return_attributes()['Allegiance'])
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
        elif path == 'p2':
            print('You chose path of Politics')
        elif path == 'p3':
            print('You chose path of ')
            print("The day had been challenging, and Paul needed to rest for at least a couple of hours to regain his strength.")
            print("As he settled down to rest, Paul began to drift into sleep.")
            print("\nWhile resting, Paul started to experience strange visions.")
            print("His mind was filled with images and sensations that seemed to blur the lines between reality and dreams.")

            vision = ev.VisionGame()
            vision.play()

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


    def play(self):
        # skill select

        points = 10
        print(f'Select your skills, you have {points} points to spend, choose wisely!:')
             
        cp, luck, diplomacy, desert_survival =  Game.start_attributes(self,points)
        player.add_attributes({'Combat Power': cp, 'Luck': luck, 'Diplomacy': diplomacy, 'Desert Survival': desert_survival})
        player.add_attributes({'Allegiance': 71, 'Happiness': 50, 'Needs': '70'})
        # Choice

        print(player.return_attributes())
        self.main(paths= ['p1', 'p2', 'p3'])


if __name__ == '__main__':
    game = Test()
    game.play()
