# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pyfiglet

global fish
fish = 'no'

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
    print('he is wearing black robes and has glowing red eyes')
    print("He looks at you and says 'you are too late'")
    print("'I am the Deamon King!'")
    print("'Your sister is mine now. Im taking her back to the Deamon Realm'")
    print("'and there is nothing you can do to stop me'")
    print('In a flash of light he sends a sphere of light towards you')
    print('There is no time to dodge it... it hits you square in the chest and knocks you unconcious')
    print('When you wake up the room is dark and your sister and the Deamon King are gone')
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
            break
        else:
            print('Incorrect answer type yes or no \n')
            continue

def deamon_realm():
    """Continues story in the Deamon Realm and intoroduces 3 doors to go through"""
    print('You find yourself in a strange house')
    print('out of the window you can see a dark and strange land')
    print('you are definately no longer on earth')
    print('You look arround the room you are in')
    print('the room is almost completely bare')
    print('there is a table in the corner with a piece of paper on it')
    print('it is a note that reads...')
    print('If you are reading this you found the travel orb i dropped')
    print('You are either very brave or very stupid')
    print('good luck in the Deamon Realm! you will need it!')
    print('there are 3 doors')
    print('to your right the door leads to a lake')
    print('To your left the door leads to a field')
    print('in front of you the door leads to a dark mountain')
    while True:
        doors = input('Which way will go you? (left/right/front) \n')
        if doors == 'left':
            lake()
            break
        elif doors == 'right':
            field()
            break
        elif doors == 'front':
            mountain()
            break
        else:
            print('incorrect answer you must enter left right or front')
            continue

def lake():
    """ takes you to the lake and asks you player if they want to go fishing"""
    print('you take the left door...')
    print('You walk down a winding path and find yourself at a large lake')
    print('the water is black and it is surrounded by dark purple sand')
    print('and strange eerie trees that have blood red leaves')
    print('at the edge of the late there is a small wooden pier')
    print('at the end of the pier there is a fishing rod set up')
    print('It speems a little strange but ...')
    while True:
        fishing = input('would you like to go fishing? (yes/no) \n ')
        if fishing == 'yes':
            lets_fish()
            break
        elif fishing == 'no':
            print("There is no time to fish. You've got a sister to save!")
            stay_at_lake()
            break
        else:
            print('Incorrect answer type yes or no')
            continue  

def lets_fish():
    """ Fishing choice, asks player if they would like to go fishing and keep the fish"""
    print()
    print('You walk down the little pier and pick up the fishing rod') 
    print('You cast the line into the water and take a seat in the little chair') 
    print('thant is next to the pole')      
    print('after a few minutes you feel a sharp tug at the line..')
    print('you quickly reel the line in')
    print("you can't believe it")
    print('you have actcually caught a fish....')
    while True:
        global fish
        fish = input('Would you like to keep the fish (yes/no) \n')
        if fish == 'yes':
            print('this fish might come in handy for something.')
            print("It looks a bit gross but if i'm hungry enough maybe I could eat it myself")
            print('you wrap it in some of the weird red leaves from the trees and take it with you')
            stay_at_lake()
            break
        elif fish == 'no':
            print("I don't want to kill the fish and it's a bit gross")
            print('you throw the fish back in the pond')
            stay_at_lake()
            break
        else:
            print('Incorrect answer type yes or no.')
            




def play_again():
    """ Called each time the player wins or loses.  
    askes the player if they would like to play again and
    takes them to the start screen if the do or thanks them for 
    playing"""
    while True:
        play = input('Would you like to play again? (yes/no\n')
        if play == 'yes':
            open_image()
            break
        elif play == 'no':
            print('Thank you for playing! Hope to see you again soon!')
            break
        else:
            print('Incorrect answer please type yes or no')





open_image()    