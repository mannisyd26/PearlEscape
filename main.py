import time
import random

GAME_OVER = '''
 ____  ____  _  _  ____  ____        ____  ____
|    ||    || \/ ||___  |    ||    ||___  |____|
|  ___|____||    ||     |    ||    ||     |   \     
|____||    ||    ||____ |____| \__/ |____ |    \
'''
MAIN_ROOM = '''
 \                                                       /
  \                                                     / 
   \                                                   /
    |__________                             __________|
    |          |\                         /|          |
    |          | \ _____________________ / |          |
    |          |  |                     |  |          |
    |          |  |                     |  |          |
    |          |  |                     |  |          |
    | <---     |  |                     |  |    --->  |
    |          |  |                     |  |          |  
    |          |  |_____________________|  |          |  
    |          | /                       \ |          |
    |__________|/                         \|__________|
    |                                 ___             |
   /                                 /~~/___            \
  /                                 /__//  /             \
 /                                     /__/               \ 




'''

NOTES_1 = '''
  ________  _______   ___
 /        \/       \_/   \
/                        /
\  its been like this.. /
 \  as long as i can   /
  \ remember           |
   |  every day...     |
  /  every night...    \
  \                     |
 / this darkness..       \   
|     when will it end?   \
 \                         \ 
 |____________/\___/\____/\/ '''

NOTES_2 = '''
  ___   _______  ________
 /   \_/       \/        \
 \                         \
  \                        /
   \  explore the rooms   |
    |pick the right items /
    |    pay attention   /
    |  follow the clues |
   / find the pearls     \
  |                       \
 /        ESCAPE          |                  
/                         / 
\/\____/\___/\___________| '''

ORIGNIALNOTE = '''
  ___   _______  ________
 /   \_/       \/        \
 \                         \
  \                        /
   \  explore the rooms   |
    |pick the right items /
    | kill the monsters  |
   / find the 3 pearls     \
  |                       \
  /      and escape        |
 /                          |
/      SURIVE             / 
\/\____/\___/\____________| '''

# KITCHEN VISUALS
KITCHEN = '''                                 ___ ______
 \                                           /   |      |   
  \                                         /    |      |
   \                                       /     |      |
    |__________                           /  _   |      |
    |          |\                        /  |_|1 |      |
    |          | \ _____________________/        |      |
    |          |   |                    | ____ _  |      |
    |          |   |      ________       /     |  |      |
    |     ____ |   |      |      |      /      |  |      |
    |    /     |\  |      |  5   |    /        |  |      |
    |   |      ||  |      |      |   |  ___    |  |      |  
    |   |      ||  |______|      |__|  | 2 |   |  |      |  
    6   |      || /  __             |  |   |   |  |      |
    |___|______||/  |__|4           |__|___|___|__|______|
    |                                                |   ___
   /                                                  \ |___|
  /                                                    \|___|
 /                                                      \___|3  

 '''

# note with bad book number in 2
# key for chest at 5 is in drawer at 3
# poison apple in drawer
# 4 has code for closet
# 6 goes to library
# chest has pearl
# 1 door that sayd dpont open, itll be bad for you, are you sure you want to do this (can either give game over or extra life
KITCHENDRAWER = '''
   _______________________
  /|                       |\
 / |          ___          | \
|  |         |_1_|         |  |
|  |                       |  |
|  |_______________________|  |
|  |                       |  |
|  |                       |  |
|  |          ___          |  |
|  |         |   |         |  |
|  |         |_2_|         |  |
|  |                       |  |
|  |_______________________|  |
|  |                       |  |
|  |          ___          |  |
|  |         |_3_|         |  |
 \ |                       | /
  \|_______________________|/

  '''

KITCHEN_DRAWER_1 = '''
 _______________________________
|\                              /|
| \                            / |
|  \ ________________________ /  |
|   |                        |   |
|   |                        |   |
 \__|________________________|__/
 '''

KITCHEN_DRAWER_2 = '''
  _______________________________
|\          ___|___             /|
| \        |       |           / |
|  \ _______\_____/__________ /  |
|   |                        |   |
|   |                        |   |
 \__|________________________|__/ '''

KITCHEN_DRAWER_3 = '''
 ________________________________
|\                              /|
| \            /\____          / |
|  \ _________|___O__|_______ /  |
|   |                        |   |
|   |                        |   |
 \__|________________________|__/ '''

PAPERWITHBADBOOK = '''

   /\/\/\/ \
  / BOOK# 2 \ 
  \_______/\/ 

 '''

CHEST_UNOPENED = '''
                   :
  _____________________________                           
 \                              \
|\       ::              ::      :
| \      ::      _____   ::      :
|  \ ____::____:__0__:___::_____ :
|   :    ::    :  :  :   ::      :
 \  :    ::    :_____:   ::      :
  \ :    ::              ::      :
   \:____::______________::______:  '''

CHEST_OPENED = '''
      ___________________________
     /    ::               ::    :
    /     ::    _____      ::     :
   / :____::___:  0  :_____::_____ :                   :
  / /                             /
 / /                            /
 :/___________________________/
|\                            \
| \                            \
|  \ ___________________________\
|   :    ::    :  :  :   ::      :
 \  :    ::    :_____:   ::      :
  \ :    ::              ::      :
   \:____::______________::______:

   '''

CHEST1 = CHEST_UNOPENED
CHEST2 = CHEST_UNOPENED
CHEST3 = CHEST_UNOPENED

# Add clocks with variations of the code
CLOCK = '''
  _________________
 /                 \
|  __  __    _  __  |
| |__ |  | o | |  | | 
| |__| _/_ o | |__| |
|                   |
 \_________________/

 '''

# DINING TABLE ITEMS
DINING_ROOM = '''                                 
 \                                               /
  \                                             / 
   \                                           /
    |                               __________|
    |_                            /|          |
    | \_________________________ / |          |
    |  |   *                    |  |          |
    |  | C* A R  E F U L *    * |  |          |
    |  |       *   ____     *   |  |  *       |
    |  |    *     |    |  *     |  |        * |
   _____    ___   |    |    *   |  |          |  
  /     \ __|4|___| 5  |________|  |    *     |  
 |   _   |      _______    __|\  \ |*         |
 |  / \  |     / |_| 1 \  |\__|   \|__________|
 |  | |  |    /_________\  |  |               |
 |__|_|__|3   |         |              <*>     \
  /           |         |               |       \
 /          6                          \_/ 2     \    

 '''

LOCKEDCABINET = '''

  ________________________
 /            |           \
|            /             |
|      .     \      .      |
|       .     |            |
|             |            | 
|      _      |   __       |
|     |_|   . |  {  }    , |
|             |   ||       |
|   .      .  |   |>       |
|             |            |
|     .        \     .     |
|    .         /  .    .   |
|_____________|____________| '''

UNLOCKEDCABINET = '''
  ________________________
 /            |           \
|            /             |
|      .     \     __ .    |
|       .     |   /  |     |
|             |__|___|_____| 
|      _      |            |
|     |_|   . |        _   |
|             |       / \  |
|   .      .  |______|___|_|
|             |            |
|     .        \           |
|    .         /           |
|_____________|____________| '''

FLOWER = '''

   _
 _( )_
(_)@(_) 
  (_)|/
    \|
     |//
   \ |/  
 _\\\|//*\__
(           )
 \         /
  \_______/

'''

TABLE = '''
   _________________
  /      ___        \
 /      |___|        \
/-____-_-________-____\
|                     |
|                     |
'''

# note with bad door
CLOSET = '''

|\_                            _/ |
|  \_                        _/   |
|    \_                    _/     |
|      \___ ___________ __/       |
|          |           |    __    |        
|__________|           |___|3_|___|
|          |___________|          |    
|  _/\_    |    ___    |          | 
|_|__1_|___|   |___|   |_O<>______|
|          |           |          |
|          |___________|          |
|__________|   |   |   |___002____|
|   __   __|_4_|_5_|_6_|__        |
|  |  |_/                 \_      |
|  |*_/                     \_    |
| _/                          \_  |
 /_____________7  ______________\


'''

BOX = '''
         _________
 _______/         \_______
|                         |
|     _______________     |
|    |               |    |
|    |____o----<_____|    |
|_________________________| '''

NUMBER_LOCK = '''
  ___________________
 /                   \  
|  __   __   __   __  |
| |##| |##| |##| |##| |
| |__| |__| |__| |__| |
|                     |
| |0| |1| |2| |3| |4| |
|                     |
| |5| |6| |7| |8| |9| |
 \___________________/

'''

PEARL_LOCK = '''
   ___________________
  /                   \
 /  ___    ___    ___  \
|  /   \  /   \  /   \  |
| |  O  ||  O  ||  O  | |
|  \___/  \___/  \___/  |
 \                     /
  \___________________/

'''

LETTER_LOCK = '''
    _________________________________
   /                                 \
  / ___   ___   ___   ___   ___   ___ \
 / |   | |   | |   | |   | |   | |   | \
|  |___| |___| |___| |___| |___| |___|  |
|                                       |
|                                       |
|   A B C D E F G H       _____         |
|   I J K L M N O P      /     \        |
|   Q R S T U V W X     |   O   |       |
|         Y Z            \_____/        |
 \                                     /
  \___________________________________/


'''

LIBRARY = '''


\_                         _/
  \_                     _/
    \ ___-_-_-_____---__/
      |         |     
      |  _____  | ___ _   1    
      | |  _  | | |__| | _ |\
      | | |_| | | ||_|||_|/||| |__
      | |_____| |  _   ___
      |         | (_}__| |---__
      |   ___   |_||_|||_|__|__|_
  4   |  /   \  | ____
 / |  | | 3   | | |  |__|\  _
| @|  | |  /\ | |_|_||__|_|(_)__
| @|  | |/\  || |        
|@@  _/_||__/_|_|-__-_-_
|@@|/                _  \_
|_/                 |2|   \_
/___________5 ______________\                 

'''

# one book has key to chest in basement

BOOK_SHELF = '''
  __________________________  __________________________
||  _     __                ||        ____         ____ ||
|| | |   |  |_ _ _      ___ ||   ||  |    |___    |    |||
|| | |___|  | | | |____|   |||  .  . |____|   |___| 4  |||
|| | | 1 |  | | | |    |   ||| ;    :|    |   |   |    |||
||_|_|_+_|__|_|_|_|____|___|||__*__*_|____|___|___|____|||
||--------------------------||--------------------------||
||  ___                     ||                    _     ||
||_|   |____     {o}    _ _ ||         __   _____\ \    ||
|| |   |\   \   __|__  | | ||| .---.   )(  (_____|\ \   ||
|| |   | \   \ (  3  ) | | |||( X X ) /  \ (_____| \ \  ||
||_|___|__\___\_\|||/__|_|_|||_|_V_|_(____)(_____|__\_\_||
||--------------------------||--------------------------||
||                       *  ||  *__*                ^   ||
||  (w) [o]              |  ||  |  |    ____       / \  ||
|| __|___|_  _ __ __ __ _ \ || .    .  |    |___  / ^ \ ||
|| \  5   / | |  |5 |  | | |||:      : | 2  |   |(( o ))||
||__\_**_/__|_|__|__|__|_|/_||_*____*__|____|___| \___/_||
||--------------------------||--------------------------||
'''
# 1 P
# 2 bad book
# 3 H
# 4 pay attention, be careful
# 5 Dont eat apple

BOOKWITHKEY = '''      

                     .,^
                  ,/    :
                .'        :
              .'            :
      _,.---'';              :
 ,._''         \               :
<               :   \^/          :
 :               \   |           ,.
  :               ;  |>       .,' 
   :               :       ,'
    :                ;  ,'
     :             __.\_'
      :       ,_.''
       :  .,_'
        :/

'''

# key for opening chest in basement
DOUBLE_DOORS = '''

C  H  O  O  S  E
 _ __--=__  ____________    _ __   =---______--__
| |  ____-\/__________ |  | |  _\_/___________  |
| | |                | |  | | |                | |
| | |                | |  | | |                |/
| | |________________| |  | | |________________|\
| |                    |  | |                    |
| |                   /   | |                    |
| |             __    \   | |             __    (
| |            |__|    |  | |            |__|    |
| |                    /  | |                    |
| |                   |   | |                    |
| |                    \  | |                    |
| | DOOR 1             |  | | DOOR 2            /
|_|_______-_--=-/\__--_|  |_|__---_______/\_____\ 

                         C  A  R  E  F  U  L  L  Y
'''

# BEDROOM
BEDROOM = '''


 _                                            _
| \_                                        _/ |
|   \_                                    _/   |
|     \__________________________________/     |
|      |       .                        |      |
|      |                                |      |
|      |        B     .   .             |      |
|      |           E                    |      |
|      |  .                             |      |
|      |    .              .            |      |
|      |      .      A          .       |      |
|      |    _____   . W  A R            |      |
|      |   |     |            E   .     |      |
|      |   |  2  |            .   . ..  |      |
|      |   |   * |      ___ .           |      |
|      |___|_____|______|4|_____________|      |
|     / __________               ____    \     |
|    / /_________()             /_*__\    \    |
|  _/   |     3  |              | 1  |     \_  |
|_/_____________________5   _________________\_|

 '''

DOOR2 = '''
 _ __--=__  ____________  
| |  ____-\/__________ | 
| | |                | |  
| | |                | | 
| | |________________| |
| |                    |  
| |                   /  
| |             __    \  
| |            |__|    | 
| |                    /  
| |                   |   
| |                    \ 
| | DOOR 1             |
|_|_______-_--=-/\__--_|

'''

BED = '''

  ______--______---_____-____-
|\
|  \ 
|  | \ 
|  |   \ 
|  |     \ 
|  |       \-______---__________  
|  |        |  |            
|  |        |  |   ___
|__|        |  |  |   \
            |  |  |___/
            |__|


'''

BEDROOMTABLE = '''
   _________________
  /      ___        \
 /      |___|        \
/-____-_-________-____\
|                     |
|                     | '''


def ENDING1():
    answer = 'yes'
    time.sleep(1)
    print('You find that there is no hope')
    time.sleep(1)
    print('You feel years of work and worry leave you')
    time.sleep(1)
    print("There is no purpose for you here")
    time.sleep(1)
    print('You feel whispers of dread')
    time.sleep(1)
    print("But you easily will them away")
    time.sleep(1)
    print('You lie on the floor and wait... (enter to continue)')
    input()
    print("You wait for anyone to take you away from this horrid place (enter to continue)")
    input()
    print('...')
    time.sleep(1)
    print('You hear shuffling')
    time.sleep(1)
    print("You can't open your eyes")
    time.sleep(1)
    print('You feel something pick you up by your feet')
    time.sleep(1)
    print('You find that you can\'t scream')
    time.sleep(2)
    print('\'You have failed,\' you hear something say')
    time.sleep(1)
    print("\'We must get a replacement,\' says another voice.")
    time.sleep(1)
    print('Your head hits something as it drags you away')
    time.sleep(1)
    print('Perhaps there was another way, you think')
    time.sleep(1)
    print("Perhaps you could have made better decisions")
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(GAME_OVER)


def INTRO():
    print('Your eyes suddenly open')
    time.sleep(2)
    print('The ground feels unfamiliar')
    time.sleep(2)
    print('Everything around you is pitch black')
    time.sleep(2)
    print('You don\'t know you you got here')
    time.sleep(2)
    print('Your last memory comes crashing at you')
    time.sleep(2)
    print('an eerie scream')
    time.sleep(2)
    print('You feel around to get an idea of your surroundings (enter to continue)')
    input()
    print('There is a door behind you')
    time.sleep(1)
    print('The door is locked')
    time.sleep(1)
    print("It would be too hard to break it down")
    time.sleep(1)
    answer = input(('Give up? (yes or no)'))
    if answer.startswith('y'):
        ENDING1()
        return answer
    else:
        time.sleep(2)
        print('You calm your nerves, and take a deep breath')
        time.sleep(2)
        print('You search the room with your hands')
        time.sleep(2)
        print('You find a flashlight')
        time.sleep(2)
        answer = ''
        i = 0
        while answer != 'yes':
            print('Turn on flashlight? (type yes)')
            answer = input().lower()
            i = i + 1
            if i >= 3:
                print('You decide to turn on the flashlight with no other option.')
                break
        time.sleep(1)
        print(MAIN_ROOM)
        time.sleep(2)
        print('You find yourself in a large room')
        time.sleep(1)
        print('With many pathways leading out')
        time.sleep(1)
        print('After walking around for a bit')
        time.sleep(1)
        print('You find a note')
        time.sleep(1)
        answer = ''
        i = 0
        while answer != 'yes':
            print('Read note? (type yes)')
            answer = input().lower()
            i = i + 1
            if i >= 3:
                print('You decide to read the note with no other option.')
                break
        time.sleep(1)
        print(NOTES_1)
        time.sleep(1)
        print('Click enter to continue')
        input()
        print(NOTES_2)
        time.sleep(1)
        print('Click enter to continue')
        input()
        print('When you finish reading')
        time.sleep(1)
        print('You hear a voice in your head tell you that you must escape')
        time.sleep(2)
        print('After further thought, you find that this note seems familar')
        time.sleep(2)
        print('This unsettles you, and you put the note back where you found it')
        time.sleep(1)
        print('...')
        time.sleep(2)
        print('You want to move far away from the note')
        time.sleep(2)
        answer = 'no'
        return answer


def MAINROOM():
    print(MAIN_ROOM)
    print('In front of you there are two pathways')
    time.sleep(1)
    print('One to the right, and one to the left')
    time.sleep(2)
    direction = ''
    while direction != 'right' and direction != 'left':
        print('Which do you choose? (right or left). (You can always come back to this room)')
        direction = input().lower()
        if direction == 'right':
            TO_KITCHEN()
        if direction == 'left':
            TO_DINING_ROOM()


# KITCHEN FUNCTIONS
def CHEST(CHESTNUM, COLOR, PEARLNUM):
    if CHESTNUM == CHEST_UNOPENED:
        print('You decide to look at the box in the room')
        time.sleep(2)
        print('At a closer glance, it looks like a chest')
        time.sleep(2)
        print(CHESTNUM)
        time.sleep(2)
        print('The chest and its lock are ' + COLOR + '.')
        time.sleep(2)
        print('Why would there be a chest here?')
        time.sleep(2)
        print('You try the lock')
        time.sleep(2)
        print('The lock doesn\'t budge')
        time.sleep(2)
        print('Where could you find a key?')
    if CHESTNUM == CHEST_OPENED:
        if PEARLNUM not in items:
            print("You open the chest with the " + COLOR + " key")
            time.sleep(2)
            print('And you find...')
            time.sleep(2)
            print('A pearl!')
            items.append(PEARLNUM)
        if PEARLNUM in items:
            print('Nothing to do here')


def ENDING2():
    print("You feel hunger settle in")
    time.sleep(1)
    print('The apple beckons you')
    time.sleep(2)
    print('You have a great desire to sink your teeth')
    time.sleep(1)
    print('Into this juicy fruit that lies in front of you (enter to continue)')
    input()
    print('You don\'t even think')
    time.sleep(2)
    print('You grab the apple')
    time.sleep(1)
    print('And take a big bite')
    time.sleep(2)
    print('You instantly feel satisfaction and happiness')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print("Soon, however, doubt and guilt settles in")
    time.sleep(1)
    print('You only realize you have made a grave mistake')
    time.sleep(1)
    print('As you begin to crumble away')
    time.sleep(1)
    print(GAME_OVER)


def TO_KITCHEN():
    # treasure chest with key
    print('You open the right door and find a kitchen on the other side')
    time.sleep(2)
    print('The room is dark, but the flashlight illumates just about everything')
    time.sleep(2)
    print('You take a quick scan of the room')
    time.sleep(1)
    KITCHENCHOICES()


def KITCHEN_DRAWER():
    print(KITCHENDRAWER)
    print('Which drawer do you want to open? or type \'back\' to go back to the kitchen')
    drawer = input()
    while drawer != '1' and drawer != '2' and drawer != '3' and drawer != 'back':
        print("What do you want to do? (1, 2, 3, back)")
    if drawer == 'back':
        print('You decide to go back')
        KITCHENCHOICES()
    if drawer == '1':
        print(KITCHEN_DRAWER_1)
        time.sleep(1)
        print('There is nothing in this drawer')
        print('(Click enter to go back)')
        input()
        KITCHEN_DRAWER()
    if drawer == '2':
        print(KITCHEN_DRAWER_2)
        time.sleep(1)
        print('Inside this drawer, you find an apple')
        time.sleep(2)
        print('You instints tell you that you shouldn\'t eat it')
        time.sleep(1)
        print('Much less even touch it')
        time.sleep(1)
        print('Do you want to eat it? (yes or no)')
        answer = input()
        if answer.startswith('y'):
            ENDING2()
            result = 'bad'
            return result
        else:
            print("You decide to leave the apple be")
            print("(Click enter to go back)")
            input()
            KITCHEN_DRAWER()
    if drawer == '3':
        print(KITCHEN_DRAWER_3)
        time.sleep(1)
        print('Inside this drawer, you find a note')
        time.sleep(1)
        print('The letter O is written on it')
        time.sleep(2)
        print('You ponder what this might mean')
        time.sleep(1)
        print("(Click enter to go back)")
        input()
        KITCHEN_DRAWER()


def KITCHENCHOICES():
    print(KITCHEN)
    print("What do you want to do? (1, 2, 3...)")
    choice = int(input())
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
        print("What do you want to do? (1, 2, 3...)")
        choice = input()
    if choice == 1:
        print('You find a clock in the back of the kitchen')
        print(CLOCK)
        time.sleep(1)
        print("The time is 62:10. How is that even possible?")
        print("(if done, click enter)")
        response = input()
        print('What next?')
        KITCHENCHOICES()
    elif choice == 2:
        print('You find a cabinet in the side of the room')
        time.sleep(1)
        print(PAPERWITHBADBOOK)
        time.sleep(1)
        print('Inside, you find a ripped piece of paper')
        time.sleep(1)
        print("On the paper there is a note")
        time.sleep(2)
        print("\'Book#2\'")
        time.sleep(1)
        print('The first half of the note seems to be ripped')
        time.sleep(1)
        print("(if done, click enter)")
        input()
        print('What next?')
        KITCHENCHOICES()
    elif choice == 3:
        print('You walk towards the drawers')
        time.sleep(2)
        KITCHEN_DRAWER()
        time.sleep(1)
        result = KITCHEN_DRAWER()
        if result == 'bad':
            returm
        else:
            print("(if done, click enter)")
            input()
            print('What next?')
            KITCHENCHOICES()
    elif choice == 4:
        CHEST(CHEST1, 'golden', 'PEARL1')
        print("(if done, click enter)")
        input()
        print('What next?')
        KITCHENCHOICES()
    elif choice == 5:
        print('You decide to go to the library')
        time.sleep(1)
        TO_LIBRARY()
    else:
        print('You decide to return to the mainroom')
        time.sleep(1)
        MAINROOM()


def TO_DINING_ROOM():
    print('You decide to take the left door')
    time.sleep(1)
    print(DINING_ROOM)
    time.sleep(1)
    print('And find yourself in a dining room setting')
    time.sleep(1)
    print('You see a message on the opposite side of the room')
    time.sleep(1)
    print('You shudder, and ponder giving up (enter to continue)')
    input()
    print('Now is not the time however.')
    time.sleep(1)
    print('A voice in your head tells you to keep going')
    time.sleep(1)
    DININGROOMCHOICES()


def DININGROOMCHOICES():
    print(DINING_ROOM)
    choice = int(input(('What do you want to do? (1, 2, 3...)')))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 and choice != 6:
        print('Type a number (1, 2, 3...)')
        choice = int(input(print('What do you want to do?')))
    if choice == 1:
        print(TABLE)
        print("You walk to the table in the middle of the room")
        time.sleep(1)
        print("On the table, you find a box")
        time.sleep(1)
        print('Luckily, the box is unlocked')
        time.sleep(1)
        print('Inside, you find a note with a single letter')
        time.sleep(1)
        print('\'T\'')
        time.sleep(1)
        print('(Click enter to continue)')
        input()
        DININGROOMCHOICES()
    if choice == 2:
        print('You walk towards the innocent flower pot in the room')
        time.sleep(1)
        print(FLOWER)
        time.sleep(1)
        print('You search inside the pot with your hand')
        time.sleep(1)
        if CHEST2 == CHEST_OPENED:
            print('You find nothing')
            time.sleep(1)
            print('There is nothing to do here')
            time.sleep(1)
        if CHEST2 == CHEST_UNOPENED:
            print('Your hand touches something that does not feel like soil')
            time.sleep(1)
            print('You pull it out')
            time.sleep(2)
            print('Looks like you found a key')
            time.sleep(1)
            print('The key is silver and has an eerie glow to it')
            time.sleep(1)
            CHEST2 = CHEST_OPENED
            print('You tuck the key into your pocket')
            time.sleep(1)
        print('(Click enter if done)')
        input()
        DININGROOMCHOICES()
    if choice == 3:
        print('You decide to look at the drawer at the left of the room')
        if CABINET == CABINETLOCKED:
            print(CABINET)
            time.sleep(1)
            print("You try the door of the cabinet")
            time.sleep(1)
            print('It won\'t budge')
            time.sleep(1)
            print('You then notice a key hole')
            time.sleep(1)
            print('Where could you find a key?')
            time.sleep(1)
            print('(Click enter to continue)')
            input()
            DININGROOMCHOICES()
        if CABINET == CABINETUNLOCKED:
            print(CABINET)
            time.sleep(2)
            print('You use the cabinet key and open the cabinet')
            time.sleep(2)
            print('Inside, you find two scraps of paper')
            time.sleep(2)
            print('On one, there is a picture of a clock')
            time.sleep(2)
            print('ON the other, there is a short note')
            time.sleep(1)
            print('\'Door # ' + gooddoor + '\'')
            time.sleep(2)
            print('You wonder what these may mean')
            time.sleep(1)
            print('(click enter to continue)')
            input()
            DININGROOMCHOICES()
    if choice == 4:
        CHEST(CHEST3, 'bronze', 'PEARL3')
        print("(if done, click enter)")
        input()
        print('What next?')
        DININGROOMCHOICES()
    if choice == 5:
        print('You decide to go the next room')
        time.sleep(1)
        TO_BEDROOM()
    if choice == 6:
        print('You decide to return to the main room')
        time.sleep(1)
        MAINROOM()


def TO_LIBRARY():
    time.sleep(1)
    print(LIBRARY)
    time.sleep(2)
    print('You find yourself in the library')
    time.sleep(2)
    print('Books line up the entire left side of the room')
    time.sleep(2)
    print('Multiple doors lead out of this room')
    LIBRARY_CHOICES()


def LIBRARY_CHOICES():
    print(LIBRARY)
    choice = int(input(('What do you want to do? (1, 2, 3...)')))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5:
        print('Type a number (1, 2, 3...)')
        choice = int(input(print('What do you want to do?')))
    if choice == 1:
        print('You decide to look at the books')
        time.sleep(1)
        BOOKSHELF()
        outcome = BOOKSHELF()
        if outcome == 'bad':
            return
        else:
            print('(click enter to go back')
            input()
            LIBRARY_CHOICES()
    if choice == 2:
        print('You decide to look at the object on the ground')
        time.sleep(2)
        print('It looks like a book')
        time.sleep(1)
        print('WHen you open the book...')
        time.sleep(1)
        if CHEST1 == CHEST_OPENED:
            print('And there is nothing inside')
            time.sleep(1)
            print('There is nothing to do here')
            time.sleep(1)
        if CHEST1 == CHEST_UNOPENED:
            print('You find a golden key')
            time.sleep(2)
            print('It seems to have a strange glow to it')
            time.sleep(2)
            print('You stuff it into your pocket')
            time.sleep(2)
            print('You wonder what this will open')
            time.sleep(2)
            CHEST1 = CHEST_OPENED
        print('(click enter to go back)')
        input()
        LIBRARY_CHOICES()
    if choice == 3:
        print('You walk towards the fireplace')
        time.sleep(2)
        print('You don\'t understand why a fire would be placed so close to these books')
        time.sleep(1)
        print('You look around the fire place')
        time.sleep(2)
        print('And find a small charred piece of paper')
        time.sleep(1)
        print('it says \'don\'t read\'')
        time.sleep(2)
        print('The rest is cut off')
        time.sleep(2)
        print('(click enter to go back)')
        LIBRARY_CHOICES()
    if choice == 4:
        print('You decide to take a look at the side of the room')
        time.sleep(1)
        result = DOUBLEDOORS()
        if result == 'death':
            return
        if result != 'death':
            print('(click enter to go back')
            input()
            LIBRARY_CHOICES()
    if choice == 5:
        print('You decide to return to the kitchen')
        time.sleep(1)
        KITCHENCHOICES()


def DOUBLEDOORS():
    print(DOUBLE_DOORS)
    time.sleep(1)
    print('In front of you there are two doors')
    time.sleep(2)
    print('They seem to lead somewhere important')
    time.sleep(1)
    print('You see the message on the wall')
    time.sleep(2)
    print('It seems like you should be careful')
    time.sleep(2)
    print('Which door do you choose? (1 or 2 or type \'back\' to go back)')
    door = input()
    if door.lower() == 'back':
        LIBRARYCHOICES()
    else:
        if door == '1':
            doorword = 'first'
        if door == '2':
            doorword = 'second'
        print('You open the ' + doorword + ' door')
        if int(door) == gooddoor:
            print('You open the door')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('And it seems like you made the right choice')
            TO_CLOSET()
        else:
            print('You open the door')
            time.sleep(2)
            print('...')
            time.sleep(2)
            print('At first you see nothing')
            time.sleep(2)
            print('...')
            time.sleep(1)
            print('You hear a creak')
            time.sleep(1)
            print('You look up')
            time.sleep(2)
            print('And see a boulder fall on your head')
            time.sleep(2)
            print('Maybe there was a clue you could have looked for?')
            time.sleep(1)
            print(GAME_OVER)
            result = 'death'
            return result


def BOOKSHELF():
    print(BOOK_SHELF)
    time.sleep(1)
    print('What do you want to look at? (1, 2, 3...) (or type back to return to the library)')
    book_choice = input()
    while book_choice != '1' and book_choice != '2' and book_choice != '3' and book_choice != '4' and book_choice != '5' and book_choice != 'back':
        print('What do want to look at? (1, 2, 3...)')
    if book_choice == 'back':
        print('You decide to go back')
        LIBRARYCHOICES()
    if book_choice == '1':
        print('You decide to look at the first book')
        time.sleep(1)
        print('As you skim through the pages...')
        time.sleep(1)
        print('You find that every page has the letter \'P\' written on it')
        time.sleep(1)
        print("That might not be important")
        time.sleep(1)
        print('(click enter to go back)')
        input()
        BOOKSHELF()
    if book_choice == '2':
        print('You decide to look at the second book')
        time.sleep(1)
        print('As you read through the pages')
        time.sleep(1)
        print('you begin to feel queasy and drowsy')
        time.sleep(2)
        print("Even then, you feel a great urge to continue")
        time.sleep(2)
        print('You quickly read through the book')
        time.sleep(1)
        print('Eating up every word as if your life depends on it')
        time.sleep(2)
        print('...')
        time.sleep(2)
        print('When you finaly finish')
        time.sleep(2)
        print('You feel a chill move down your back')
        time.sleep(2)
        print('You hear breathing')
        time.sleep(2)
        print("Just as you are about to turn around")
        time.sleep(2)
        print('The floor sucks you in')
        time.sleep(1)
        print('The last thing you see being fire')
        time.sleep(1)
        print('...')
        time.sleep(2)
        print("Maybe there was a clue you could have looked for?")
        time.sleep(1)
        print(GAME_OVER)
        outcome = 'bad'
        return outcome
    if book_choice == '3':
        print('You decied to take a look at the vase')
        time.sleep(1)
        print('Inside, you find a note')
        time.sleep(1)
        print('On the note, there is a tongue twister')
        time.sleep(1)
        print('\'Hairy Harry Hid His Hammer under a Hill of Honey colored Hay\'')
        time.sleep(1)
        print('Click enter to continue')
        input()
        print("You don't understand how this may be important")
        time.sleep
        print('Though each \'h\' is in bold')
        time.sleep(1)
        print('(click enter to go back)')
        input()
        BOOKSHELF()
    if book_choice == '4':
        print('You decide to read the 4th book')
        time.sleep(1)
        print('Inside, you find only two sentences')
        time.sleep(2)
        print('\'Pay attention\'')
        time.sleep(1)
        print('\'Be Careful\'')
        time.sleep(1)
        print('The rest of the pages are blank')
        time.sleep(1)
        print('(Click enter to go back)')
        input()
        BOOKSHELF()
    if book_choice == '5':
        print('You decide to look at the vase holding two flowers')
        time.sleep(2)
        print('Between the flowers, you find a small strip of paper')
        time.sleep(1)
        print('\'Beware of the apple\'')
        time.sleep(1)
        print('Strange')
        time.sleep(1)
        print('(Click enter to go back)')
        input()
        BOOKSHELF()


# 1 P
# 2 bad book
# 3 H
# 4 pay attention, be careful
# 5 Dont eat apple

def TO_BEDROOM():
    print(BEDROOM)
    print('From the dining room you enter the bedroom')
    time.sleep(1)
    print('Nothing in this house seems to make sense')
    time.sleep(1)
    print('The words in fron of you leave a sinking feeling in your gut')
    time.sleep(1)
    print('You remember you goal')
    time.sleep(1)
    print('You must escape')
    time.sleep(1)
    BEDROOMCHOICES()


def BEDROOMCHOICES():
    print(BEDROOM)
    time.sleep(1)
    print('What do you want to look at? (1, 2, 3...) ')
    number = int(input())
    while number != 1 and number != 2 and number != 3 and number != 4 and number != 5:
        print('What do want to look at? (1, 2, 3...)')
    if number == 1:
        print('You decide to take a look at the table')
        print(BEDROOMTABLE)
        print("There is a box on this table")
        if CABINET == UNLOCKEDCABINET:
            print('The box is empty')
            time.sleep(1)
            print('There is nothing to do here')
            time.sleep(1)
        if CABINET == LOCKEDCABINET:
            print('Luckily, the box is unlocked')
            time.sleep(2)
            print('Inside the box, there is a key')
            time.sleep(1)
            print('The key is metal, but seems fairly ordinary')
            time.sleep(2)
            print("A \'C\' is carved into its edge")
            time.sleep(1)
            print("What might this open?")
            time.sleep(1)
            CABINET == UNLOCKEDCABINET
        print('(Click enter to go back)')
        input()
        BEDROOMCHOICES()
    if number == 2:
        print('You decide to look at the door in the front of the room')
        time.sleep(2)
        print('As you near the door, you feel a sense of urgency')
        print(DOOR)
        time.sleep(2)
        print('Once you reach the door, you start to reach for the handle')
        time.sleep(2)
        print('You pause, and wonder if this is truly the right decision')
        time.sleep(2)
        print('Opening this door could be the choice between life and death')
        time.sleep(2)
        print('You feel like beyond this door lies something important')
        time.sleep(2)
        print('You take a deep breath and reach for the handle')
        time.sleep(1)
        print('You begin to sweat as your hand inches closer and closer')
        time.sleep(1)
        print('You turn your head away, feel a need to scream')
        time.sleep(2)
        print('You twist the handle')
        time.sleep(2)
        print('...')
        print('The door is locked')
        time.sleep(2)
        print('...')
        time.sleep(2)
        print('In frustration, you kick the door open')
        time.sleep(1)
        print('The door easily breaks down')
        time.sleep(2)
        print('...')
        time.sleep(2)
        print('...')
        time.sleep(2)
        print("There is nothing inside")
        time.sleep(1)
        print('(Click enter to go back)')
        input()
        BEDROOMCHOICES()
    if number == 3:
        print('You decide to take a look at the bed')
        time.sleep(1)
        print('After some searching...')
        time.sleep(1)
        print(BED)
        print('You find a piece of paper under the bed')
        time.sleep(2)
        print('The single letter \'y\' is written on it')
        time.sleep(1)
        print('(Click enter to go back)')
        input()
        BEDROOMCHOICES()
    if number == 4:
        CHEST(CHEST2, 'silver', 'PEARL2')
        print("(if done, click enter)")
        input()
        BEDROOMCHOICES()
    if number == 5:
        print('You decide to return to the dining room')
        time.sleep(1)
        DININGROOMCHOICES()


def TO_CLOSET():
    print('You feel relieved after choosing the right door')
    time.sleep(1)
    print('This room has a sense of finality')
    time.sleep(1)
    print('NOTE: You can still go to other rooms, enter the closet through the same door as before')
    CLOSETCHOICES()


def CLOSETCHOICES():
    print('What do you want to look at? (1, 2, 3...) ')
    number = int(input())
    while number != 1 and number != 2 and number != 3 and number != 4 and number != 5 and number != 6 and number != 7:
        print('What do want to look at? (1, 2, 3...)')
    if number == 1:
        print('You decide to look at the box at the side of the room')
        print(BOX)
        print('You open the box...')
        if CHEST3 == CHEST_OPENED:
            print('and find nothing')
            time.sleep(2)
            print('The box is only full of dust')
            time.sleep(1)
            print('There is nothing to do here')
            time.sleep(1)
            print('click enter to go back')
            input()
            CLOSETCHOICES()
        if CHEST3 == CHEST_UNOPENED:
            print('and find an object')
            time.sleep(1)
            print('When you take the object out of the box, you find that it is a key')
            time.sleep(2)
            print('The key is bronze, and has a lively glow')
            time.sleep(1)
            print('click enter to go back')
            input()
            CLOSETCHOICES()
    if number == 2:
        print('You decide to look at some containers on the right')
        time.sleep(1)
        print('As you look around, you are greated with a lot of dust')
        time.sleep(1)
        print('Inside one of the containers, you find a crumpled piece of worn paper')
        time.sleep(1)
        print('You are barely able to make out what is written')
        time.sleep(1)
        print('It seems to be the letter \'n\'')
        time.sleep(2)
        print('(click enter to go back)')
        input()
        CLOSETCHOICES()
    if number == 3:
        print('You decide to look at the box on the right shelf')
        time.sleep(1)
        print('You open the box')
        time.sleep(1)
        print('It is full of dust...')
        time.sleep(1)
        print('But not much else')
        time.sleep(2)
        print('(click enter to go back)')
        input()
        CLOSETCHOICES()
    if number == 4:
        print(NUMBER_LOCK)
        print('You walk towards the number lock')
        print('Try a combination? (or type back to go back)')
        print('NOTE: type numbers in the format (0000). Use clues to find combo')
        num_guess = input()
        while num_guess != '6210':
            if num_guess == 'back':
                CLOSETCHOICES()
            else:
                print('Incorrect, try again? (or type back to go back)')
                num_guess = input()
        print('You got the correct combination')
        print('Try another lock')
        locks.append('NUMBER')
        if 'LETTER' and 'PEARL' and 'NUMBER' in locks:
            WINGAME()
        else:
            print('(click enter to go back)')
            input()
            CLOSETCHOICES()
    if number == 5:
        print(PEARL_LOCK)
        time.sleep(1)
        print('You walk towards the pearl lock')
        time.sleep(1)
        if 'PEARL1' and 'PEARL2' and 'PEARL3' not in items:
            print('You still have more pearls to find')
            time.sleep(1)
        else:
            print('You have found all the pearls')
            time.sleep(1)
            locks.append('PEARL')
        if 'LETTER' and 'PEARL' and 'NUMBER' in locks:
            WINGAME()
        else:
            print('(click enter to go back)')
            input()
            CLOSETCHOICES()
    if nubmer == 6:
        print(LETTER_LOCK)
        print('You walk towards the letter lock')
        time.sleep(1)
        print("Try a combination? (or type back to go back)")
        time.sleep(1)
        print('NOTE: Type letters in the format AAAAAA. Use clues to find combo')
        time.sleep(1)
        letter_guess = input()
        while letter_guess.upper() != 'PYTHON':
            if letter_guess == 'back':
                CLOSETCHOICES()
            else:
                print('Incorrect, try again? (or type back to go back)')
                letter_guess = input()
        print('You got the correct combination')
        time.sleep(1)
        locks.append('LETTER')
        if 'LETTER' and 'PEARL' and 'NUMBER' in locks:
            WINGAME()
        else:
            print('(click enter to continue)')
            input()
            CLOSETCHOICES()
    if number == 7:
        print("You decide to return to the library")
        time.sleep(1)
        print('Note: To reenter closet, go through the same door as before')
        time.sleep(1)
        LIBRARY_CHOICES()


def WINGAME():
    print('You open all the locks')
    time.sleep(2)
    print('A sense of euphoria overcomes you')
    time.sleep(2)
    print('A door opens in front of you')
    time.sleep(2)
    print('You take a step outside')
    time.sleep(2)
    print('and take a breath of fresh air')
    time.sleep(2)
    print('it feels as if you haven\'t taken a breath in years')
    time.sleep(2)
    print('The sky is dark, but you feel more alive than ever')
    time.sleep(2)
    print('As you look outside however')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('You notice that the stars don\'t seem right')
    time.sleep(2)
    print('The sky is far too black')
    time.sleep(2)
    print('Even the ground seems pixilated')
    time.sleep(2)
    print('an eerie sensation forms in your mind')
    time.sleep(2)
    print('You notice a light in the edge of your vision')
    time.sleep(2)
    print('As you turn to see the light, you hear a sound')
    time.sleep(2)
    print('Something hits you')
    time.sleep(2)
    print('and you fall to the floor')
    time.sleep(2)
    print('Your vision clouds over')
    time.sleep(2)
    print('And you begin fall into a deep')
    time.sleep(2)
    print('deep')
    time.sleep(2)
    print('deep')
    time.sleep(2)
    print('sleep')
    time.sleep(2)
    print('Your last memory')
    time.sleep(2)
    print('being the feeling of victory')
    time.sleep(3)
    print('and the screech of a monster')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('Your eyes suddenly open')
    time.sleep(3)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(2)
    print('Thank you for playing')


CABINET = LOCKEDCABINET
locks = []
all_locks = ['NUMBER', 'PEARL', 'LETTER']
pearllist = ['PEARL1', 'PEARL2', 'PEARL3']
gooddoor = random.randint(1, 2)
items = []
answer = INTRO()
if answer.startswith('n'):
    MAINROOM()
