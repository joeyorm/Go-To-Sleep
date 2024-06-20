import random
import sys, time

##################### color functions and vars ##############################
class colors:
    g = '\033[32m'  # GREEN
    y = '\033[33m'  # YELLOW
    r = '\033[31m'  # RED
    b = '\033[34m'  # BLUE
    RE = '\033[0m'  # RESET COLOR

def green(x):
    x = str(x)
    return colors.g + x + colors.RE

def red(x):
    x = str(x)
    return colors.r + x + colors.RE

def blue(x):
    return colors.b + x + colors.RE

def yellow(x):
    return colors.y + x + colors.RE

def help_iterator(x):
    for i in range(len(x)):
        print(x[i])

##############################################################################

def Project2():
    CMD_BED = 'b'
    CMD_CLOSE = 'c'
    CMD_EAST = 'e'
    CMD_FEED = 'f'
    CMD_GET = 'g'
    CMD_LOCK = 'l'
    CMD_NORTH = 'n'
    CMD_OPEN = 'o'
    CMD_PUT = 'p'
    CMD_QUIT = 'q'
    CMD_SOUTH = 's'
    CMD_TV = 't'
    CMD_UNLOCK = 'u'
    CMD_WEST = 'w'
    CMD_PASSWORD1 = "21"
    CMD_PASSWORD2 = "64"
    CMD_PASSWORD3 = "32"
    CMD_INV = "i"
    CMD_HELP = "h"

    ROOM_FRONT = 0
    ROOM_LIVING = 1
    ROOM_KITCHEN = 2
    ROOM_OFFICE = 3
    ROOM_BED = 4
    
    times_gone_into_bedroom = 0
    flag_me_awake = True
    flag_tv_on = False
    safe_is_open = False
    trevor_been_fed = False
    extra_treats_had = None
    pantry_open = False
    pantry_locked = True
    spam_in_pantry = False
    out_of_treats = False

    room = 0
    turns = 0
    fail_counter = 0
     
    
################################### LISTS ##########################################
    ROOM_NAMES = ("Front Door", "Living Room", "Kitchen", "Office", "Bedroom")

    Dog_Tricks = ["Trevor gives you a lick on the cheek", "Trevor barks merrily at your command",
                  "Trevor gives you a paw", "Trevor runs outside and brings his favorite ball", "Trevor rolls over",
                  "Trevor flops over and lies still on his belly, he plays dead", "Trevor spins around happily",
                  "Trevor stands on his hind legs", "Trevor sits down and wags his tail",
                  "Trevor jumps at you and gives you a hug",
                  "Trevor eats a Super Treat, grows wings, and flies around the house!",
                  "Trevor eats a Super Treat and decimates the neighbor's cat's house!"]
    Help = [
    f"Sleep in bed:      {green('b')}", 
    f"Close:             {green('c')}",
    f"Move East:         {green('e')}", 
    f"Move North:        {green('n')}", 
    f"Move West:         {green('w')}",
    f"Move South:        {green('s')}",
    f"Feed:              {green('f')}",
    f"Get item:          {green('g')}",
    f"Lock:              {green('l')}",
    f"Open:              {green('o')}",
    f"Quit Game:         {green('q')}",
    f"Toggle Tv:         {green('t')}",
    f"Unlock:            {green('u')}", 
    f"Open Inventory:    {green('i')}",
    f"Open Map:          {green('m')}",
    f"See achievements:  {green('a')}",
    "\n"]
    
    INVENTORY = []

    ACHIEVEMENTS = []

    start = time.time()
    print('''
        )
       (  (              .^.
        \) )           .'.^.'.
         (/          .'.'---'.'.
        _\)_       .'.'-------'.'.
       (__)()    .'.'-,=======.-'.'.
       (_)__)  .'.'---|   |   |---'.'.
       (__)_),'.'-----|   |   |-----'.'.
       ()__.'.'-------|___|___|-------'.'.
       (_.'.'---------------------------'.'.
       .'.'-------------------------------'.'.
       """"|====..====.=======.====..====|"""""
       ()_)|    ||    |.-----.|    ||    |
       (_)_|    ||    ||     ||    ||    |
       (...|____||____||_____||____||____|
      (_)_(|----------| _____o|----------|
      (_)(_|----------||     ||----------|
      (__)(|----------||_____||----------|
      (_)(_|---------|""""""""|----------|
      ()()(|--------|""""""""""|_--------|
    wWUwwuw|wwWWwuu|"""""""""""""|uwuwuuW|wuwwuuwu
      ''')
    print("Today really has been a long and tedious day. You arrive at the front of your house with a feeling of relief, but immediately remember your work is far from over...\n")
    print("CIIC 3015 Autumn 2021 Project 2: Time For Go-To-Bed\n")
    print("Remember if you need help, you can use the 'h' word for help in commands")

    ####################### FRONT DOOR AND ROOM INDEXER ####################################

    while flag_me_awake:
        print(f"Location:  {green(ROOM_NAMES[room])} \n")
        cmd = input("> ")
        turns += 1

        if cmd == CMD_QUIT:
            return False

        if cmd == CMD_INV:
            print(red(INVENTORY))

        if cmd == CMD_HELP:        
             liscmd = "Commands List:"
             print(f"{liscmd.center(20, ' ')}")
             help_iterator(Help)  

        if room == ROOM_FRONT:
            if cmd == CMD_EAST:
                print(f"You open the front door and enter your house.")
                room = ROOM_LIVING
                if flag_tv_on:
                    print(f"The TV is currently {blue('on')}")
                else:
                    print(f"The TV is currently {blue('off')}")
                continue

        #####
        ################################ LIVINGROOM  ####################################

        if room == ROOM_LIVING:
            if cmd == CMD_TV:
                if flag_tv_on:
                    print(f"You turned the tv {blue('off.')}")
                    flag_tv_on = False
                else:
                    print(f"You turned the tv {blue('on.')}")
                    flag_tv_on = True
                continue

            
            ################################### Locational commands #################################

            if cmd == CMD_NORTH and trevor_been_fed:
                if times_gone_into_bedroom == 0:
                    print("Your dog Trevor no longer blocks your path. You open the door and walk inside.")
                    if not spam_in_pantry:
                        print(
                            f"The {red('can of spam')} is not where it should be, you feel compelled to put it back in its place before you go to sleep\n")
                        room = ROOM_BED
                        times_gone_into_bedroom += 1
                        continue
                    else:
                        room = ROOM_BED
                        print("You enter your bedroom")
                        continue
                else:
                    if not spam_in_pantry:
                        print(
                            f"The {red('can of spam')} is not where it should be, you feel compelled to put it back in its place before you go to sleep\n")
                        room = ROOM_BED
                        print("You enter your bedroom")
                        continue
                    else:
                        room = ROOM_BED
                        print("You enter your bedroom")
                        continue


            elif cmd == CMD_NORTH and trevor_been_fed == False:
                print(
                    "Your dog Trevor stands blocking the door. He looks uneasy, you should probably feed him so he moves out the way")

            if cmd == CMD_WEST:
                print("Lets be real, in your current state you know you wouldnt last another second outside. Lets just stay inside...")
                continue

            if cmd == CMD_EAST:
                print("You enter the office")
                if safe_is_open == False:
                    print(f"The office safe is {blue('closed')}")
                if safe_is_open:
                    print(f"The office safe is {blue('open')}... I should close it")
                room = ROOM_OFFICE
                continue

            if cmd == CMD_SOUTH:
                print("You enter the kitchen.")
                if pantry_locked == False:
                    print(f"The pantry is {red('unlocked')}")
                else:
                    print(f"The pantry is {red('locked')}")
                room = ROOM_KITCHEN
                continue
            

            ######################## "FEED" commands, variants and failsafes ####################

        if cmd == CMD_FEED and "bag of dog treats" in INVENTORY and flag_tv_on == False:
            print(
                'You open the bag of dog treats while Trevor stares blankly at the television. Much to your dismay, he seems to refuse to eat until the TV is turned on for some reason...')
            continue

        if cmd == CMD_FEED and "bag of dog treats" in INVENTORY and flag_tv_on and extra_treats_had == None:
            print(
                'While Trevor is distracted looking at the TV, you open the bag of treats and plop them on the floor for him. He quickly darts over and begins eating')
            trevor_been_fed = True
            extra_treats_had = 1
            continue

        if cmd == CMD_FEED and "bag of dog treats" in INVENTORY and extra_treats_had >= 0 and not out_of_treats:
            if extra_treats_had <= 10:
                print(Dog_Tricks[random.randint(0, len(Dog_Tricks) - 1)])
                extra_treats_had += 1
                if extra_treats_had == 5:
                    #print(f"{green('ACHIEVEMENT:')} Half-full or half_empty? ")
                    ACHIEVEMENTS.append("Half-full or half_empty? (Feed Trevor atleast 5 extra treats)")
                continue

            else:
                print("Welp, there goes the entire bag, he sure has one hell of an appetite...")
                INVENTORY.remove('bag of dog treats')
                out_of_treats = True
                continue

        if cmd == CMD_FEED and out_of_treats:
            print('There are no more dog treats, youll need to remember to buy some tomorrow.')
            continue

        #########################################################################################
        ######################################## KITCHEN ########################################
        #########################################################################################

        if room == ROOM_KITCHEN:
            if cmd == CMD_NORTH:
                print("You enter the living room.")
                room = ROOM_LIVING
                if flag_tv_on:
                    print(f"The TV is currently {blue('on')}")
                else:
                    print(f"The TV is currently {blue('off')}")
                continue

            ######################### "Unlock" and "open" failsafes and conditions ###################

            if cmd == CMD_UNLOCK and "pantry key" in INVENTORY and pantry_locked:
                print(f"You use the {red('pantry key')} to unlock the pantry doors")
                pantry_locked = False
                continue

            if cmd == CMD_UNLOCK and "pantry key" in INVENTORY and pantry_locked == False:
                print(f"The pantry is already {blue('unlocked')}")
                continue

            if cmd == CMD_OPEN and pantry_open == False and pantry_locked == False:
                print(
                    f"You opened the pantry. Inside you see the {red('bag of dog treats')} and enough space to fit virtually anything else in there")
                pantry_open = True
                continue

            if cmd == CMD_OPEN and pantry_open:
                print(f"The kitchen pantry is already {blue('open')}")
                continue

            if cmd == CMD_OPEN and pantry_locked:
                print(f"You cant open the pantry without {blue('unlocking')} it")
                continue

            if cmd == CMD_LOCK and "pantry key" not in INVENTORY:
                print(f"You cant do that, you must get the {red('pantry key')} from the office safe first...")
                continue

            if cmd == CMD_UNLOCK and "pantry key" not in INVENTORY:
                print(f"You cant do that, you must get the {red('pantry key')} from the office safe first...")
                continue

            ######################### Kitchen "Get" and "Put" failsafes and conditions ###################

            if cmd == CMD_GET and "bag of dog treats" in INVENTORY and pantry_open and pantry_locked == False and out_of_treats == False:
                print(f'You already took the {red("bag of dog treats")}')
                continue
            elif cmd == CMD_GET and "bag of dog treats" in INVENTORY and pantry_open and pantry_locked == False and out_of_treats == True:
                print('You remember you fed Trevor the entire bag earlier...')
                continue

            if cmd == CMD_GET and pantry_open and pantry_locked == False and out_of_treats == False:
                print(f"You grab the {red('bag of dog treats')}")
                INVENTORY.append("bag of dog treats")
                continue

            if cmd == CMD_GET and pantry_open == False and pantry_locked:
                print(f'Hmmm, seems it is locked, try using the {red("pantry key")} to {blue("unlock")} it then open the doors')
                continue

            if cmd == CMD_GET and pantry_open == False:
                print('You cant grab whatever is in there without opening the doors silly...')
                continue

            if cmd == CMD_PUT and "can of spam" in INVENTORY:
                print(
                    f"The {red('can of spam')} is now safe and sound in the pantry. Now you should close and lock the pantry before going to sleep just in case...")
                spam_in_pantry = True
                INVENTORY.remove("can of spam")
                continue

            ########################## "Lock" and "close" failsafes and conditions ###################

            if cmd == CMD_LOCK and pantry_open == False and pantry_locked and "pantry key" in INVENTORY:
                print(f'The pantry is already {blue("locked")}')
                continue
            elif cmd == CMD_LOCK and pantry_open:
                print(f'You cant lock the pantry while its still {blue("open")}')
                continue

            if cmd == CMD_LOCK and pantry_locked == False and "pantry key" in INVENTORY:
                print(
                    f'You use the {red("pantry key")} to {blue("lock")} the pantry, whoever planned to mess with its contents sure wont be able to do so now!')
                pantry_locked = True
                continue

            if cmd == CMD_CLOSE and pantry_locked:
                print(f"The pantry is {blue('locked')}, so it already is {blue('closed')}")
                continue

            if cmd == CMD_CLOSE and pantry_open:
                print(f"You {blue('close')} the pantry door")
                pantry_open = False
                continue

            if cmd == CMD_CLOSE and pantry_open == False:
                print(f"Pantry door is already {blue('closed')}")
                continue

        ###############################################################################
        ############################## OFFICE #########################################
        ################################################################################

        if room == ROOM_OFFICE:
            if cmd == CMD_WEST:
                room = ROOM_LIVING
                if flag_tv_on:
                    print(f"The TV is currently {blue('on')}")
                else:
                    print(f"The TV is currently {blue('off')}")
                continue

            ################################# OFFICE "get" commands and failsafes ###############

            if cmd == CMD_GET and safe_is_open == False:
                print('You need to open the safe first')
                continue

            if cmd == CMD_GET and safe_is_open and "pantry key" not in INVENTORY:
                print(f"You grab the {red('pantry key')} from the safe")
                INVENTORY.append('pantry key')
                continue

            if cmd == CMD_GET and safe_is_open and "pantry key" in INVENTORY:
                print(f'You already have the {red("pantry key")}')
                continue

            ############################ OFFICE "put" commands and failsafe ################

            if cmd == CMD_PUT and safe_is_open == False:
                print("You need to open the safe first")
                continue

            if cmd == CMD_PUT and safe_is_open and "pantry key" in INVENTORY:
                print(f"You place the {red('pantry key')} back in the safe")
                INVENTORY.remove('pantry key')
                continue

            if cmd == CMD_PUT and safe_is_open and "pantry key" not in INVENTORY:
                print(f"You dont have the {red('pantry key')} yet")
                continue

            ############################## SAFE COMBINATION#################################

            if cmd == CMD_OPEN and safe_is_open == False:
                print(
                    "You remember that in order to open your safe, you have to input your 3 secret numbers... Lets see now...")
                cmd = input("First sequence was?: ")
                if cmd == CMD_PASSWORD1:
                    print("Nice, next up is?")
                    cmd = input("Second sequence?: ")
                    if cmd == CMD_PASSWORD2:
                        print("Spot on")
                        cmd = input("Final sequence?: ")
                        if cmd == CMD_PASSWORD3:
                            print("Great, you have unlocked your safe!\n")
                            safe_is_open = True
                            if fail_counter == 0:
                                ACHIEVEMENTS.append(f'First try baby (Unlock the safe in your first try)')
                                fail_counter == None
                            continue
                        else:
                            print("Oops, thats not right... You should try again")
                            fail_counter += 1
                            continue
                    else:
                        print("Oops, thats not right... You should try again")
                        fail_counter += 1
                        continue
                else:
                    print("Oops, thats not right... You should try again")
                    fail_counter += 1
                    continue

            if cmd == CMD_OPEN and safe_is_open:
                print('The safe is already open')
                continue

            if cmd == CMD_CLOSE and safe_is_open:
                print(
                    "You close the safe and it automatically locks, electronic safes sure are great! Now thats one less thing to worry about")
                safe_is_open = False
                continue

            if cmd == CMD_CLOSE and safe_is_open == False:
                print('The safe is already closed')
                continue

        ############################# BEDROOM ########################################
        ######################################################################################

        if room == ROOM_BED:
            if cmd == CMD_SOUTH:
                room = ROOM_LIVING
                if flag_tv_on:
                    print(f"The TV is currently {blue('on')}")
                else:
                    print(f"The TV is currently {blue('off')}")
                continue

            if cmd == CMD_GET and 'can of spam' in INVENTORY and spam_in_pantry == False:
                print(f"You already took the {red('can of spam')}")
                continue

            if cmd == CMD_GET and 'can of spam' not in INVENTORY and spam_in_pantry == False:
                print(f"You got the {red('can of spam')}, now you should put it in the pantry")
                INVENTORY.append("can of spam")
                continue
            
            if cmd == CMD_GET and 'can of spam' not in INVENTORY and spam_in_pantry == True:
                print("You already took the spam to the pantry, there's nothing left to pick up")

            if cmd == CMD_BED:
                if not safe_is_open:
                    if not flag_tv_on:
                        if not pantry_open:
                            if pantry_locked:
                                if 'pantry key' not in INVENTORY:
                                    if spam_in_pantry:
                                        print(
                                            "You finally lay down on your bed and tuck your pillow before going to sleep. A long day of work has finally been rewarded...\n")
                                        print(f"{turns} turns played\n")
                                        end = time.time()
                                        elapsed_time = end - start
                                        if elapsed_time > 60:
                                            print(f"It took you {round(elapsed_time)/60} minutes to complete the run\n")
                                        else:
                                            print(f"It took you {round(elapsed_time)} seconds to complete the run\n")
                                        if elapsed_time < 120:
                                            ACHIEVEMENTS.append('The fastest man alive! (Finish the game within 2 minutes)')
                                        if turns < 50:
                                            ACHIEVEMENTS.append('GG Well played (Win within 50 turns)')
                                        if ACHIEVEMENTS != []:
                                            print(f"{yellow('Achievements unlocked:')}\n")
                                            for x in ACHIEVEMENTS:
                                                individual_achievement = f"-{x}\n"
                                                print(yellow(individual_achievement))
                                                flag_me_awake = False
                                        else: print('No secret achievements were attained, try playing again to see if you find any!')
                                    else:
                                        print(
                                            "The can of spam in the bedroom gives you a cold stare and says to you 'Put me in the pantry... NOW!'")
                                        continue
                                else:
                                    print("Dangit, seems you forgot to place the pantry key back in the safe")
                                    continue
                            else:
                                print("You forgot to lock the pantry, better hurry up and go do that before your sleep paralysis demon comes and eats your precious spam!")
                                continue
                        else:
                            print("Oops, you left the pantry door open and your OCD wont let you sleep unless you close it")
                            continue
                    else:
                        print("The tv is on and it makes a lot of noise, you cant sleep")
                        continue
                else:
                    print("Your pretty sure you left the safe open...")
                    continue
    return True
