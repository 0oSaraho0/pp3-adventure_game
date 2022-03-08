# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import pyfiglet

def open_image():
    """ Shows name of game and gets player name"""
    print(pyfiglet.figlet_format('DEAMON', justify='center'))
    print(pyfiglet.figlet_format('QUEST', justify='center'))

    print('If you wish to play, please enter your name')
    x = input()
    print('Welcome ' + x)
    intro()    


open_image()    