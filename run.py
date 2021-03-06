import os
import time
import pyfiglet

global fish
fish = 'no'

global flower
flower = 'ignore'

global beat_bear
beat_bear = 'run'


def open_image():
    """ Shows name of game and gets player name. runs if else statement to
    ensure name is input, links to game intro function"""
    print(pyfiglet.figlet_format('DEMON', justify='center'))
    print(pyfiglet.figlet_format('QUEST', justify='center'))
    while True:
        name = input('If you wish to play please enter your name\n')
        if name == "":
            print('Incorrect input.  Please enter your name')
            continue
        else:
            print()
            time.sleep(2)
            print(f'Welcome {name}')
            break
    intro()
    time.sleep(3)


def intro():
    """ Sets the scene for the game using print statements.
    links to start_game function"""
    print()
    print('It is a normal boring Saturday night. \n')
    time.sleep(2)
    print('Your parents have gone out for the evening leaving you in charge.')
    print()
    time.sleep(2)
    print('Your baby sister is sleeping upstairs in her bedroom. \n')
    time.sleep(2)
    print('Suddenly you hear a strange noise coming' +
          ' from your sisters bedroom...')
    time.sleep(2)
    print('You go upstairs to investigate... \n')
    time.sleep(2)
    print('As you approach the door, you hear a strange chanting sound')
    print('coming from her room... \n')
    time.sleep(2)
    print('Full of fear you slowly open the door.... \n')
    time.sleep(2)
    print('Standing over your sisters cot is what looks like a man. \n')
    time.sleep(2)
    print('He is wearing black robes and has glowing red eyes. \n')
    time.sleep(2)
    print('He looks at you and says "you are too late" \n')
    time.sleep(2)
    print('"I am the Demon King!" \n')
    time.sleep(2)
    print('"Your sister is mine now. Im taking her back to the Demon Realm')
    time.sleep(1)
    print('and there is nothing you can do to stop me".\n')
    time.sleep(2)
    print('In a flash of light he sends a sphere of light towards you. \n')
    time.sleep(2)
    print('There is no time to dodge it...')
    print('It hits you square in the chest and knocks you unconcious. \n')
    time.sleep(3)
    print('When you wake up the room is dark and your sister and')
    print('the Demon King are gone \n')
    time.sleep(3)
    print('You sit and cry for a moment .... \n')
    time.sleep(3)
    print('Then you notice a small glowing orb underneath the cot \n')
    time.sleep(2)
    print('It must have been dropped by the Demon King \n')
    time.sleep(2)
    start_game()


def start_game():
    """ starts the game, asks the player if they wish to touch the sphere. Uses if,
    elif, else statement. 'yes' links to demon_realm function. 'no' links to
    game_over function. Uses while loop to ensure correct input word is
    entered"""
    while True:
        touch_orb = input('Do you touch the orb?  (yes/no) \n')
        if touch_orb == 'no':
            print()
            time.sleep(2)
            print('How terribly brave of you! \n')
            print('Just leave your sister to her fate \n')
            time.sleep(2)
            print('Go and have a cup of tea and forget all about it! \n')
            time.sleep(6)
            game_over()
            break
        elif touch_orb == 'yes':
            demon_realm()
            break
        else:
            print('Incorrect answer please type yes or no \n')
            continue


def demon_realm():
    """Continues story in the Demon Realm and introduces
    3 doors to go through. The player can choose left, right or front.
    using an if else statement and while loop. 'left' connects to lake function
    'right' connects to field function and 'front' connects to mountain
    function"""
    print()
    time.sleep(2)
    print('You find yourself in a strange house.')
    time.sleep(2)
    print('Out of the window you can see a dark and strange land. \n')
    time.sleep(2)
    print('You are definately no longer on earth! \n')
    time.sleep(2)
    print('You look around the room you are in')
    time.sleep(2)
    print('it is almost completely bare. \n')
    time.sleep(2)
    print('There is a table in the corner with a piece of paper on it. \n')
    time.sleep(2)
    print('It is a note that reads... \n')
    time.sleep(2)
    print('If you are reading this you found the travel orb I dropped')
    print('You are either very brave or very stupid!')
    print('Good luck in the Demon Realm! \nYou will need it! \n')
    time.sleep(3)
    print('You look back around the room\n')
    time.sleep(2)
    print('There are 3 doors. \n')
    print('To your left, the door leads to a lake. \n')
    time.sleep(2)
    print('To your right, the door leads to a field. \n')
    time.sleep(2)
    print('In front of you, the door leads to a dark mountain')
    time.sleep(2)
    print("and the Demon King's Castle. \n")
    time.sleep(2)
    while True:
        doors = input('Which way will you go?  (left/right/front) \n')
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
    """ Goes to the lake and asks the player if they want to go fishing,
    uses if, else statement. 'yes' links to lets_fish function, 'no'
    links to stay_at_lake function """
    print()
    print('You take the left door... \n')
    time.sleep(2)
    print('You walk down a winding path and find yourself at a large lake.\n')
    time.sleep(2)
    print('The water is black and it is surrounded by dark purple sand')
    time.sleep(2)
    print('and strange eerie trees that have blood red leaves. \n')
    time.sleep(2)
    print('At the edge of the lake, there is a small wooden pier... \n')
    time.sleep(2)
    print('At the end of the pier, there is a fishing rod set up... \n')
    time.sleep(2)
    print('It seems a little strange but ... \n')
    time.sleep(2)
    while True:
        fishing = input('Would you like to go fishing?  (yes/no) \n ')
        if fishing == 'yes':
            lets_fish()
            break
        elif fishing == 'no':
            print()
            time.sleep(2)
            print("There is no time to fish. You've got a sister to save!")
            time.sleep(2)
            stay_at_lake()
            break
        else:
            print('Incorrect answer please type (yes or no)')
            continue


def lets_fish():
    """ follows the story and the player goes fishing, if else
    stament asks if the player would like to keep the fish.  both yes
    and no options link to stay_at_lake function"""
    print()
    time.sleep(2)
    print('You walk down the little pier and pick up the fishing rod')
    time.sleep(2)
    print('You cast the line into the water')
    print('and take a seat in the little chair. \n')
    time.sleep(2)
    print('After a few minutes you feel a sharp tug at the line.. \n')
    time.sleep(2)
    print('You quickly reel the line in... \n')
    time.sleep(2)
    print("You can't quite believe it... \n")
    time.sleep(2)
    print('You have actually caught a fish!....\n')
    while True:
        global fish
        fish = input('Would you like to keep the fish?  (yes/no) \n')
        if fish == 'yes':
            time.sleep(2)
            print('This fish might come in handy for something. \n')
            time.sleep(2)
            print("It looks a bit gross but if I'm hungry enough")
            print("maybe I could eat it myself \n")
            time.sleep(2)
            print('You wrap it in some of the weird red leaves from the trees')
            print('and take it with you \n')
            time.sleep(2)
            stay_at_lake()
            break
        elif fish == 'no':
            print("I don't want to kill the fish and it's a bit gross. \n")
            time.sleep(2)
            print('You throw the fish back in the lake \n')
            time.sleep(2)
            stay_at_lake()
            break
        else:
            print('Incorrect answer please type (yes or no).')
            continue


def stay_at_lake():
    """ If else statement, asks player if they would like to navigate to the
    mountain, field or stay at the lake. 'mountain' option links to mountain
    function. 'field' links to field function
    and 'stay' leads to game_over function"""
    while True:
        stay = input('Would you like to stay at the lake, go to the,' +
                     'mountain \nor go to the field? (stay/mountain/field) \n')
        if stay == 'stay':
            print('This lake is really peaceful \n')
            time.sleep(2)
            print('You decide to stay for a while \n')
            time.sleep(2)
            print('The purple sand surrounding the lake ' +
                  'looks really interesting...\n')
            time.sleep(2)
            print('You walk down to the edge of the water... \n')
            time.sleep(2)
            print('You reach down and take a handfull of sand... \n')
            time.sleep(2)
            print('The moment your skin touches ' +
                  'the sand it starts to move....\n')
            time.sleep(3)
            print('The sand is actally millions of tiny bugs... \n')
            time.sleep(3)
            print('You scream in pain as the bugs ' +
                  'consume your entire body... \n')
            time.sleep(3)
            print('Moments later there is just ' +
                  'a pile of bones by the water \n')
            time.sleep(3)
            print('What a way to go!')
            time.sleep(6)
            game_over()
            break
        elif stay == 'mountain':
            mountain()
            break
        elif stay == 'field':
            field()
            break
        else:
            print('Incorrect answer please type (stay, mountain or field)')
            continue


def field():
    """ plays when the payler chooses to go to the field, here you find the
    dragon can choose befriend the dragon or run. befriend leads to the
    befriend_dragon function, run leads to the run_from_dragon function"""

    print('You set off along the path \n')
    time.sleep(2)
    print('and find yourself in an enormous field ' +
          'full of green and red flowers. \n')
    time.sleep(2)
    print('There seems to be a big hill in the middle of it... \n')
    time.sleep(2)
    print('You head towards the hill to see ' +
          'if you can see anything from the top \n')
    time.sleep(2)
    print('as you get close to the hill you realise it is moving.... \n')
    time.sleep(2)
    print('The hill unfolds and looks straight at you....\n')
    time.sleep(3)
    print('It is not a hill.....\n')
    time.sleep(3)
    print('It is a DRAGON......\n')
    time.sleep(2)
    while True:
        dragon = input('Do you run, or try to ' +
                       'befriend the dragon?  (run/befriend)\n')
        if dragon == 'run':
            run_from_dragon()
            break
        elif dragon == 'befriend':
            befriend_dragon()
            break
        else:
            print('Incorrect answer please type (run or befriend)')
            continue


def befriend_dragon():
    """gives the player the opportunity to befriend the dragon.  This will
    only work if the player has got the fish from the lake,  uses a global
    variable of fish. fish input links to new_dragon_friend function. Run
    leads to run_from_dragon function and pet input leads to game_over
    function.  Uses dragon_input variable to give player the correct
    options in the input statements"""
    print()
    print('This dragon looks friendly enough you think to yourself \n')
    time.sleep(2)
    print("I'm sure I can win it over \n")
    time.sleep(2)
    print('You start to walk slowly towards the dragon...\n')
    time.sleep(3)
    print('But as you step closer the dragon starts ' +
          'to make a low growling sound..... \n')
    time.sleep(3)
    print("you're starting to wonder if you've made the correct decision...\n")
    time.sleep(2)
    print('What do you do?\n')
    time.sleep(2)
    print('Put your hand out to try and pet the dragon? \n')
    time.sleep(2)
    print("Change you're mind and run?\n")
    time.sleep(2)
    global fish
    if fish == 'yes':
        print('Give the Dragon the fish from the lake?\n')
    if fish == 'yes':
        dragon_input = ('Pet the dragon, Run or give the' +
                        ' dragon the fish (pet/run/fish)')
    else:
        dragon_input = ('Pet the dragon or Run (pet/run)')
    while True:
        dragon_taming = input(f'Do you {dragon_input} \n')
        if dragon_taming == 'fish':
            new_dragon_friend()
        elif dragon_taming == 'pet':
            print('You tentitively stretch out your hand' +
                  ' towards the dragons nose \n')
            time.sleep(2)
            print('The dragon gives you a sniff.....\n')
            time.sleep(2)
            print('But something is wrong... \n')
            time.sleep(2)
            print('The dragon likes the smell of you' +
                  ' for all the wrong reasons... \n')
            time.sleep(2)
            print('Before you can blink the dragon pounces...\n')
            time.sleep(2)
            print('AND SWALLOWS YOU WHOLE!!!')
            time.sleep(6)
            game_over()
            break
        elif dragon_taming == 'run':
            run_from_dragon()
            break
        else:
            print(f'Incorrect answer you must input: {dragon_input}')


def run_from_dragon():
    """ defining what happens when the player runs from the dragon.
    connects to game_over function"""
    print('The dragon is looking at you....\n')
    time.sleep(2)
    print('You sieze your moment and run ' +
          'as fast as you can away from the dragon.\n')
    time.sleep(2)
    print('The dragon leaps into the air and grabs you with its claws.\n')
    time.sleep(2)
    print('It takes you flying high into the air. \n')
    time.sleep(2)
    print('The dragon takes you high up into the mountain')
    time.sleep(2)
    print('and drops you into a nest....\n')
    time.sleep(2)
    print('Waiting in the nest are four hungry baby dragons.....\n')
    time.sleep(2)
    print('who devour you instantly\n')
    time.sleep(6)
    game_over()


def new_dragon_friend():
    """ The player has the dragon on side and next must decide whether to go to the
    Demon Castle or take a Joyride on the dragon. The castle option links to
    the demon_castle_dragon option and joyride links to the game_over
    function"""
    print()
    print('Thank goodness you kept that fish \n')
    time.sleep(2)
    print('You throw the fish to the dragon \n')
    time.sleep(2)
    print('The Dragon really seems to like it ....\n')
    time.sleep(2)
    print("It makes a happy chirping noise")
    print("and pushes you with it's nose \n")
    time.sleep(2)
    print("This Dragon isn't so bad after all! \n")
    time.sleep(2)
    print("You decide to climb on the Dragon's back. \n")
    time.sleep(2)
    print("Do you take the dragon for a joyride around the Demon Realm?\n")
    time.sleep(2)
    print("or, do you fly directly to the " +
          "Demon King's castle in the mountain?\n")
    time.sleep(2)
    while True:
        fly = input('(joyride/castle)')
        if fly == 'joyride':
            print('You climb onto the Dragons back\n')
            time.sleep(2)
            print('The Dragon takes off flying high up in the sky\n')
            time.sleep(2)
            print('The Dragon flys high towards the sun....\n')
            time.sleep(2)
            print("It's scales heat up making it too hot to hold onto \n")
            time.sleep(2)
            print("Then the dragon swoops down close to the sea \n")
            time.sleep(2)
            print("You fall into the sea because you can't hold on\n")
            time.sleep(2)
            print('The water is freezing and you are unable to swim\n')
            time.sleep(2)
            print('You sink to the bottom and drown\n')
            time.sleep(6)
            game_over()
            break
        elif fly == 'castle':
            demon_castle_dragon()
            break
        else:
            print('Incorrect answer please input (joyride or castle)')


def mountain():
    """Plays when the player picks mountain path.  It gives the option
    to collect an exploding flower. The 'pick' and 'ignore' options link to
    bear function 'smell' links to game_over function"""
    print()
    print('You climb the rocky mountain path \n')
    time.sleep(2)
    print('Growing along the sides are the most')
    print('beautiful pink flowers\n')
    time.sleep(2)
    print('Do you stop to smell the flowers?\n')
    time.sleep(2)
    print('Do you pick a flower to take with you? \n')
    time.sleep(2)
    print('Or ignore the flowers completely \n')
    time.sleep(2)
    while True:
        global flower
        flower = input('(smell/pick/ignore)')
        if flower == 'smell':
            print('You stop and smell the flowers \n')
            time.sleep(2)
            print('They smell beautiful \n')
            time.sleep(2)
            print('But they make youre nose tickle...\n')
            time.sleep(2)
            print('These are no ordinary flowers...\n')
            time.sleep(3)
            print('The pollen has explosive qualities...\n')
            time.sleep(3)
            print('Unfortunately you have a large quantity')
            print('of pollen up your nose.\n')
            time.sleep(3)
            print('You try to hold in the sneeze..\n')
            time.sleep(3)
            print("But you can't!....\n")
            time.sleep(3)
            print('You sneeze.....\n')
            time.sleep(3)
            print('Your head EXPLODES! \n')
            time.sleep(6)
            game_over()
            break
        elif flower == 'pick':
            print('These flowers may come in handy later \n')
            time.sleep(2)
            print('You carefully wrap one up and put it in your pocket \n')
            time.sleep(2)
            bear()
            break
        elif flower == 'ignore':
            print('There is no time to stop for flowers \n')
            time.sleep(2)
            print("I've got to save my sister. \n")
            time.sleep(2)
            bear()
            break
        else:
            print('Incorrect answer please enter (smell, pick or ignore)')
            continue


def bear():
    """ Player continues up the mountain and has to pass a bear.  Uses global
    variables fish and flower.  fish and flower inputs lead to the
    demon_castle_mountain function run and fight inputs lead to the game_over
    function.  Uses bear_input variable to give player correct options"""
    print()
    print('You continue up the mountain path \n')
    time.sleep(2)
    print('It is getting steep')
    print('and dense with undergrowth \n')
    time.sleep(2)
    print('You hear movement up ahead \n')
    time.sleep(2)
    print('You turn the corner and you see.... \n')
    time.sleep(3)
    print('A BEAR!!! \n')
    time.sleep(2)
    print("Oh no, how are you going to get past a bear!! \n")
    time.sleep(2)
    print('Do you run? \n')
    time.sleep(2)
    print('Do you fight it with your bare hands? \n')
    time.sleep(2)
    global fish
    global flower
    global beat_bear
    if fish == 'yes':
        print('Do you give it the fish? \n')
        time.sleep(2)
    if flower == 'pick':
        print('Do you throw the flower at it \n')
        time.sleep(2)
    if fish == 'yes' and flower == 'pick':
        bear_input = ('(run/fight/flower/fish)')
    if fish == 'yes' and flower == 'ignore':
        bear_input = ('(run/fight/fish)')
    if fish == 'no' and flower == 'pick':
        bear_input = ('(run/fight/flower)')
    if fish == 'no' and flower == 'ignore':
        bear_input = ('(run/fight)')
    while True:
        beat_bear = input(f'Do you {bear_input}?\n')
        if beat_bear == 'run':
            time.sleep(2)
            print('You try to run but you trip and fall \n')
            time.sleep(2)
            print('Into a patch of those pink flowers \n')
            time.sleep(3)
            print('Both you and the bear explode into a million pieces \n')
            time.sleep(6)
            game_over()
            break
        elif beat_bear == 'fight':
            print('There is no other option. \n')
            time.sleep(2)
            print('You decide to take on the bear yourself. \n')
            time.sleep(2)
            print("But you're an idiot! \n")
            time.sleep(2)
            print("Of course you can't beat a bear \n")
            time.sleep(2)
            print("It's a friggin BEAR!!! \n")
            time.sleep(2)
            print('It rips you limb from limb \n')
            time.sleep(6)
            game_over()
            break
        elif beat_bear == 'fish' and fish == 'yes':
            print()
            print('Thank goodness you kept that fish \n')
            time.sleep(2)
            print('You wave the fish in front of the bear\n')
            time.sleep(2)
            print('and then throw it into the unergrowth. \n')
            time.sleep(2)
            print('The bear goes running after it. \n')
            time.sleep(2)
            print('You take your chance ')
            print('and leg it up the rest of the mountain \n')
            time.sleep(2)
            demon_castle_mountain()
            break
        elif beat_bear == 'flower' and flower == 'pick':
            print()
            print('You remember the flower in your pocket \n')
            time.sleep(2)
            print('You throw it at the bear \n')
            time.sleep(2)
            print('It explodes killing the bear instantly. \n')
            time.sleep(2)
            print('You breathee a sigh of relief')
            print('and continue up the mountain\n')
            time.sleep(2)
            demon_castle_mountain()
            break
        else:
            print(f'incorrect answer please input {bear_input}')
            continue


def demon_castle_dragon():
    """ Final stage for the dragon path through the game, the player can
    choose to fight the demon or save their sister.The demon input links to
    game_over function, sister leads to winner function"""
    print()
    print('You fly on the dragons back \n')
    time.sleep(2)
    print('Straight to the Demon Kings castle. \n ')
    time.sleep(2)
    print('Through the creepy halls of the castle')
    print('until you find him..... \n')
    time.sleep(3)
    print('THE DEMON KING \n')
    time.sleep(2)
    print('You see your sister in a cot at the side of the room')
    time.sleep(2)
    print('"Touch her and I will kill you both"')
    print('Says the Demon King')
    time.sleep(2)
    print('The atmosphere is tense \n')
    time.sleep(2)
    print('You so badly want to go and hold your sister \n')
    time.sleep(2)
    print('You stare at the Demon King \n')
    time.sleep(2)
    print('You wonder what to do...')
    time.sleep(2)
    print('The dragon shifts restlessly next to you \n')
    time.sleep(2)
    print('Do you run towards the Demon King? \n')
    time.sleep(2)
    print('Or do you run towards your sister?')
    while True:
        defeat = input('(demon/sister)')
        if defeat == 'demon':
            print('You rush towards the Demon King \n')
            time.sleep(2)
            print('You are completely unarmed')
            print('so this feels a little foolish \n')
            time.sleep(2)
            print('The Demon King starts laughing \n')
            time.sleep(2)
            print('You launch yourself at the Demon King \n')
            time.sleep(3)
            print('The Demon King catches you by the throat \n')
            time.sleep(2)
            print('In a bid to help')
            print('the dragon lets out a stream of fire... \n')
            time.sleep(2)
            print('Which unfortunately hits you both')
            time.sleep(2)
            print('You were so close.....')
            time.sleep(6)
            game_over()
            break
        elif defeat == 'sister':
            print('You look at the dragon\n')
            time.sleep(2)
            print('You pray he does the right thing \n')
            time.sleep(2)
            print('You launch yourself towards you sister \n')
            time.sleep(2)
            print('The Demon King raises his arm ' +
                  'to send a fireball your way\n')
            time.sleep(3)
            print('The dragon is startled by the sudden movement \n')
            time.sleep(2)
            print('You grab your sister ....\n')
            time.sleep(2)
            print('You turn just in time')
            print('to see the dragon breathe a streem of fire\n')
            time.sleep(2)
            print('It hits the Demon King!... \n')
            time.sleep(2)
            print('He screems in pain and terror...\n')
            time.sleep(3)
            print('There is a flash of light that knocks you over... \n')
            time.sleep(3)
            print(' When you open you eyes \n')
            time.sleep(2)
            print('You are on your sofa in your living room. \n')
            time.sleep(2)
            print('You race upstairs to your sisters bedroom')
            time.sleep(2)
            print('She is safely in her cot')
            time.sleep(2)
            print('You breathe a huge sigh if relief')
            time.sleep(2)
            print('It must have been an awful nightmare..')
            time.sleep(2)
            print('Then you hear a noise from the back garden')
            time.sleep(2)
            print('You look out of the window...')
            time.sleep(2)
            print('and see the DRAGON sitting in your paddling pool......\n')
            time.sleep(3)
            print('But that is an adventure for another day!')
            time.sleep(6)
            winner()
            play_again()
        else:
            print('Incorrect answer, please input (sister or demon)')
            continue


def demon_castle_mountain():
    """ Final stage for the mountain pathway through the game, if the player
    still has the flower and iputs flower links to winner function, if the
    player inputs run or fight it links to the game_over function """
    print()
    print('You make your way into the Demon Kings Castle \n')
    time.sleep(2)
    print("It's a dark and scary building")
    print('with long and winding hallways\n')
    time.sleep(2)
    print('You find your way to the room the Demon King is in\n')
    time.sleep(2)
    print('As you enter, he looks at you and laughs\n')
    time.sleep(2)
    print("I've been expecting you, although I'm surprised you made it! \n")
    time.sleep(2)
    print('You see your sister in a cot at the side of the room.\n')
    time.sleep(2)
    print('You say "Give me my sister"\n')
    time.sleep(2)
    print('He laughs again \n')
    time.sleep(2)
    print('"How exactly are you going to make me do that"\n')
    time.sleep(2)
    print('you say" ahha... I will show you" \n')
    time.sleep(3)
    print('You have no idea how to beat him \n')
    time.sleep(2)
    print('Do you try and fight him? \n')
    time.sleep(2)
    print('Do you try and grab your sister and leg it? \n')
    time.sleep(2)
    global flower
    global beat_bear
    global fish
    choice = ""
    if flower == 'pick' and beat_bear == 'fish':
        print('Then you You remember the flower in your pocket \n')
        time.sleep(2)
        print('Do you throw it at the Demon? \n')
        time.sleep(2)
        choice = 1
        end_game = ('(flower/fight/run)')
    elif fish == 'yes' and beat_bear == 'flower':
        print("All you've got is a fish")
        print('what on earth can you do with a fish?')
        choice = 2
        end_game = ('(fish/fight/run)')
    else:
        end_game = ('(fight/run)')
    while True:
        demon_attack = input(f'Do you {end_game} \n')
        if demon_attack == 'flower' and choice == 1:
            print('You carefully and discreetly')
            print('pull the flower from your pocket \n')
            time.sleep(2)
            print('The demon has his guard down \n')
            time.sleep(2)
            print('He thinks there is nothing you can do \n')
            time.sleep(2)
            print('You throw the flower as hard as you can towards him \n')
            time.sleep(2)
            print('A look of shock and horror appears on his face....\n')
            time.sleep(3)
            print('Seconds before the flower explodes in front of him \n')
            time.sleep(3)
            print('You grab your sister....\n')
            time.sleep(3)
            print('There is a flash of light that knocks you over \n')
            time.sleep(3)
            print('When you open you eyes \n')
            time.sleep(2)
            home_from_mountain()
            break
        elif demon_attack == 'fight':
            print("You can't quite believe you got here completely unarmed \n")
            time.sleep(2)
            print('what on earth were you thinking!\n')
            time.sleep(2)
            print('You take a deap breath and run at the Demon King \n')
            time.sleep(2)
            print("You don't even get close\n")
            time.sleep(2)
            print('The last thing you hear is his evil' +
                  'cackle as he vapourises you\n')
            time.sleep(6)
            game_over()
            break
        elif demon_attack == 'run':
            print('You make a dash for your sister\n')
            time.sleep(2)
            print("But you don't even get close\n")
            time.sleep(2)
            print('He sends a fireball at you\n')
            time.sleep(2)
            print('You were so close...')
            time.sleep(6)
            game_over()
            break
        elif demon_attack == 'fish' and choice == 2:
            print('"ok" you say to yourelf\n')
            time.sleep(2)
            print('"Think bold with that fish" \n')
            time.sleep(2)
            print('You walk straight up to that Demon ...\n')
            time.sleep(3)
            print('and fish slap him round the face!\n')
            time.sleep(3)
            print('He looks at you in shock and horror\n')
            time.sleep(2)
            print("You can't believe it\n")
            time.sleep(2)
            print('His face is starting to melt...\n')
            time.sleep(2)
            print("He's allergic to fish\n")
            time.sleep(2)
            print('What a stroke of luck!\n')
            time.sleep(2)
            print('You run and grab your sister\n')
            time.sleep(2)
            print('The Demon King drops to the floor\n')
            time.sleep(2)
            print('As you run for the exit')
            print('The world around you melts away\n')
            time.sleep(2)
            print('The next thing you know\n')
            home_from_mountain()
        else:
            print(f'Incorrect answer please type {end_game}')
            continue


def home_from_mountain():
    """ Print statents describe end of game for winning the mountain section
    of the game.  links to the winner function.  I put this in because there
    are two winning options in the mountain section and it saves code being
    repeated twice"""
    print('You are on your sofa in your living room \n')
    time.sleep(2)
    print('You race upstairs to your sisters bedroom \n')
    time.sleep(2)
    print('She is safely in her cot\n')
    time.sleep(2)
    print('You breathe a huge sigh of relief\n')
    time.sleep(2)
    print('It must have been an awful nightmare.. \n')
    time.sleep(2)
    print('You sink to your knees')
    time.sleep(2)
    print('and notice the glowing orb is still there\n')
    time.sleep(2)
    print('You decide not to touch it this time\n')
    time.sleep(2)
    print("You've had quite enough adventure for one day\n")
    time.sleep(6)
    winner()


def game_over():
    """ runs game over text through a loop using os inport make the letters
    appear one at at a time. uses pyfiglet to make the letters
    decorative and time.sleep to delay the loop timelinks to
    play_again function"""

    lose = 'GAME \nOVER!'
    y = 0
    while y <= len(lose):
        os.system('clear')
        print(pyfiglet.figlet_format(lose[:y], justify='center'))
        time.sleep(0.3)
        y = y+1
    play_again()


def winner():
    """ runs winner text through a loop using os inport make the letters
    appear one at at a time. uses pyfiglet to make the letters
    decorative and time.sleep to delay the loop time links to
    play_again function"""
    win = 'WINNER!'
    y = 0
    while y <= len(win):
        os.system('clear')
        print(pyfiglet.figlet_format(win[:y], justify='center'))
        time.sleep(0.3)
        y = y+1
    play_again()


def play_again():
    """ Called each time the player wins or loses.
    askes the player if they would like to play again and
    takes them to the start screen if the do or thanks them for playing
    and exits the game"""
    while True:
        play = input('Would you like to play again? (yes/no) \n')
        if play == 'yes':
            open_image()
            break
        elif play == 'no':
            print('Thank you for playing! Hope to see you again soon!')
            exit()
        else:
            print('Incorrect answer please type (yes or no)')


open_image()
