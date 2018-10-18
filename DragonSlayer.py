import sys # for exiting when player has lost
import time # for slow_type
import random # for slow_type

# Global Scope
response = []
responseChoices = []

# Creates new profile if player does not have
# a file. Returns file name.
def boot():
    print("Welcome to DragonSlayer!\n")
    goodAns = False
    while not goodAns: #player can only move on if the answer is either Y or N
        ans = raw_input("Have you played before?(Y/N): ")
        if(ans == "N"):
            goodAns = True
            print("Making new profile now.\n")
            name = raw_input("What is your name?: ")
            profile = open((name + "DragonSlayer.txt"), 'w+')
            profile.write('NAME: ' + name + '\n')
            profile.write('LEVEL: 1\n')
            profile.write('INVENTORY: \n')
            profile.write('MOVES: \n')
            profile.close()
            return (name + "DragonSlayer.txt")
        elif(ans == "Y"):
            goodAns = True
            name = raw_input("What is your profile name?: ")
            return (name + "DragonSlayer.txt")
        else:
            print("Please input either Y or N")
#END OF BOOT()

# Takes a string and a typing speed (wpm) and
# prints to the terminal slowly as if someone
# is typing the string
# ~Found on StackOverFlow while looking for a
# way to slow down printing--modified slightly~
def slow_print(str, typing_speed):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ''

# Takes fileName and opens profile
# Gets player name from profile
def getName(fileName):
    profile = open(fileName, 'r')
    lines = profile.readlines()
    name = lines[0].rstrip()
    profile.close()
    return name[6:]
# END OF GETNAME()

# Takes fileName and opens profile
# Gets player level from profile
def getLevel(fileName):
    profile = open(fileName, 'r')
    lines = profile.readlines()
    level = lines[1].rstrip()
    profile.close()
    return level[7:]
# END OF GETLEVEL()

# Takes fileName and opens profile
# Gets inventory from profile
def getInventory(fileName):
    profile = open(fileName, 'r')
    lines = profile.readlines()
    profile.close()
    return lines[2]
# END OF GETINVENTORY()

# Takes fileName and opens profile
# Gets moves from profile
def getMoves(fileName):
    profile = open(fileName, 'r')
    lines = profile.readlines()
    profile.close()
    return lines[3]
# END OF GETMOVES()

# Takes a list and pops all values
# inside the list, clearing it
def clearList(list):
    i = 0
    while 0 < len(list):
        list.pop()
        i = i + 1
# END OF CLEARLIST()

# Records the progress of the player at the time
# this is called. Overwrites everything.
def recordProfile(fileName, name, level, inventory, moves):
    profile = open(fileName, 'w')
    profile.write('NAME: ' + name + '\n')
    profile.write('LEVEL: ' + str(level) + '\n')
    profile.write('INVENTORY: ')
    profile.write(inventory)
    profile.write('MOVES: ')
    profile.write(moves)
    profile.close()
# END OF RECORDPROFILE()

# First level: King establishes story, minimal interaction, reponses only
def levelOne(name):
    slow_print("Long ago there was a powerful kingdom. This kingdom was known throughout the land for its rich culture, lavish lifestyle, and, above all, its happy people.\n", 100)
    slow_print("For years the people from this kingdom enjoyed the great riches provided by the kingdom.\n", 100)
    slow_print("Until one day...\n", 30)
    slow_print("Drawn by the wealth this great kingdom held, a great dragon decended on the kingdom.\n", 100)
    slow_print("The dragon terrorized the small kingdom, demanding gifts of gold.\n", 100)
    slow_print("The king, helpless to save his kingdom, aquiesed to the great dragon.\n", 100)
    slow_print("Each day, the king vowed to bring gold to the dragon to keep his kingdom and his life.\n", 100)
    slow_print("Quickly, the kingdom slipped into poverty.\n", 100)
    slow_print("The king, with no gold of his own left, turned to his subjects for gold.\n", 100)
    slow_print("The once kind-hearted king turned sour, ransacking villages and subjects for gold.\n", 100)
    slow_print("The subjects begged the king to find a different way to rid the dragon, but the cowardly king would not listen.\n", 100)
    slow_print("Your village is out of gold.\n", 100)
    slow_print("You have been elected to confront the king.\n", 100)
    print("\n")
    slow_print("You stand in the center of a modest stone throne room.", 100)
    slow_print("The king sits on a raised platform in front of you.\n", 100)
    slow_print("KING: " + name + ", I have heard that you carry no gold for me.\n", 50)
    # Adding player's possible responses
    response.append('*nod*')
    responseChoices.append('1')
    response.append('My village has run dry.')
    responseChoices.append('2')
    response.append('Stop taking our money!')
    responseChoices.append('3')
    goodAns = False
    while not goodAns:
        print(response)
        print("\nAnswer: ")
        print(responseChoices)
        ans = input("\n>")
        if(ans == 1):
            goodAns = True
            slow_print("KING: There is only one way you can redeem yourself.\n", 50)
        elif(ans == 2):
            slow_print("KING: This is no excuse.\n", 50)
            slow_print("KING: You brought me no gold?\n", 30)
            response.remove('My village has run dry.')
            responseChoices.remove('2')
        elif(ans == 3):
            goodAns = True
            slow_print("KING: DO YOU WISH TO ENDURE THE DRAGON'S WRATH?!\n", 50)
            slow_print("KING: Guards, rid me of this peasant.\n", 50)
            slow_print("Two guards come from both sides of the throne and drag you out of the castle.\n", 100)
            slow_print("You live out the rest of your days in poverty and fear, toiling the fields.\n", 100)
            slow_print("Your adventure ends here.\n", 100)
            sys.exit(0)
        else:
            slow_print("KING: If you mumble again I am throwing you out!\n", 50)
    # Refresh lists
    clearList(response)
    clearList(responseChoices)
    slow_print("KING: Defeat the dragon and I will have no need to take your money.\n", 50)
    slow_print("KING: What do you say to this, " + name + "?\n", 50)
    response.append('Yes')
    responseChoices.append('1')
    response.append('Me...?')
    responseChoices.append('2')
    response.append('No')
    responseChoices.append('3')
    goodAns = False
    while not goodAns:
        print(response)
        print("\nAnswer: ")
        print(responseChoices)
        ans = input("\n>")
        if(ans == 2):
            slow_print("KING: Either this or I begin taking your people. I have no other option.\n", 50)
            slow_print("KING: This is my final offer.\n", 50)
            response.remove('Me...?')
            responseChoices.remove('2')
        elif(ans == 3):
            goodAns = True
            slow_print("KING: Very well then. You may leave.\n", 50)
            slow_print("You gather the last of your dignity and leave the stone castle for the last time.\n", 100)
            slow_print("When you return you find that the king has already taken some of your people away.\n", 100)
            slow_print("You live out the rest of your days in poverty and fear, toiling the fields, watching your neighbors disappear.\n", 100)
            slow_print("Your adventure ends here.\n", 100)
            sys.exit(0)
        elif(ans == 1):
            goodAns = True
            slow_print("KING: This is your only chance.\n", 50)
        else:
            slow_print("KING: If you mumble again I am throwing you out!\n", 50)
    # Refresh lists
    clearList(response)
    clearList(responseChoices)
    slow_print("KING: Very well. If you return with a dragon scale I will let my kingdom live in peace once more.\n", 50)
    slow_print("KING: Now BEGONE\n", 40)
    slow_print("Two guards move from the sides of the throne towards you and begin to escort you out of the castle.\n", 100)
    slow_print("GUARD1: *ahem*\n", 50)
    slow_print("GUARD1: If I were you, I'd start preparing to fight this dragon.\n", 80)
    slow_print("GUARD1: I heard some chatter around the inn that there might be a magical way to defeat this dragon. I would check it out.\n", 80)
    slow_print("GUARD1: Also get yourself a sword and shield at the blacksmith.\n", 80)
    slow_print("The guards lead you to the fifteen foot high wooden door you entered the castle through and two more guards start to crank the doors open.\n", 80)
    slow_print("GUARD1: I wish you the best of luck.\n", 80)
    slow_print("You walk out the fully raised wooden doors and hear the door guards begin to crank it shut again behind you.\n", 100)
    print("END OF LEVEL 1\n")
    print("Would you like to continue?\n")
    ans = raw_input("(Y/N) > ")
    while not goodAns:
        if(ans == 'Y'):
            goodAns = True
            print("Level 2 coming soon...\n")
            print("Thank you for playing.\n")
        elif(ans == 'N'):
            goodAns = True
            print("Your progress has been recorded.\n")
            print("Thank you for playing.\n")
        else:
            print("Please respond with either Y or N\n")
    #END OF LEVELONE

#MAIN
if __name__ == "__main__":
    # run boot() to make or access profile
    fileName = boot()

    # establish variables from profile
    name = getName(fileName)
    level = getLevel(fileName)
    inventory = getInventory(fileName)
    moves = getMoves(fileName)

    # run level one
    levelOne(name)
    level = 2
    recordProfile(fileName, name, level, inventory, moves)
