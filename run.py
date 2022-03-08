# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pyfiglet



def open_image():
    """ Shows name of game and gets player name"""
    print(pyfiglet.figlet_format('DEAMON', justify='center'))
    print(pyfiglet.figlet_format('QUEST', justify='center'))

    name = input('If you wish to play please enter your name ')

    print(f'Welcome {name}')
    intro()    

def intro():
    """ Sets the scene for the game using the players name and asks them if they wish to proceed to the next section"""
    print()
    print('It is a normal boring Saturday night.')
    print('Your parents have gone out for the evening leaving you in charge')
    print('your baby sister is sleeping upstairs in her bedroom')
    print()
    print('Suddenly you hear a strange noise coming from your sisters bedroom')
    print('so you go upstairs to investigate')
    print('As you approach the door you hear a strange chantinf sound coming from the room')
    print('Full of fear you slowly open the door....')
    print('Standing over your sisters cot is what looks like a man')
    print('he is wearing black robes ans glowing red eyes')
    print(f"He looks at you and says you're too late")
    print("Your sister is mine now. I'm taking her back to the Deamon Rehealm")
    print('and there is nothing you can do to stop me')
    print('In a flash of light he sends a sphere of light towards you')
    print('There is no time to dodge it and it hits you square in the chest and knocks you unconcious')
    print('When you wake up the room is dark and your sister and the Deamon are gone')
    print('You sit and cry for a moment ....')
    print('Then you notice a small glowing orb underneath the cot')
    print('It must have been dropped by the Deamon King')
    start_game()


def start_game():
    """ starts game, asks player if they wish to touch sphere if else yes not statememt"""
    while True:
        touch_orb = input('Do you touch the orb?  (yes/no) \n')
        if touch_orb == 'no':
            print('How terribly brave of you! Just leave your sister to her fate')
            print('Go and have a cup of tea and forget all about it')
            print('GAME OVER!')
            play_again()
            break
        elif touch_orb == 'yes':
            deamon_realm()
        else:
            print('Incorrect answer type yes or no')
            continue

        




open_image()    