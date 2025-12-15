import random
import Bot
import time
from Paused_games import pausedGames
#-----------------------------------Functions-------------------------------------#
def Print(st, dur=0.05):
    '''This function creates the typing effect'''
    for ch in st:
        time.sleep(dur)
        print(ch, end='', flush=True)

def sprt(st):
    '''This function seperates all the numbers from a string.'''
    nums = []
    i = 0
    while i < len(st) :
        if st[i].isdigit() :
            scan = st[i]
            while i < len(st)-1 :
                i += 1
                scan += st[i]
                if not scan.isdigit() :
                    nums += [int(scan[:-1])]
                    break
            else :
                nums += [int(scan)]
        i += 1
    return nums

def check(st,cards):
    '''This function checks wether the statement is vlaid or not'''
    if eval(st) and ('//' not in st) and ('!=' not in st) : # if statement is not valid it returns false.
        nums = sprt(st)
        if sorted(cards) == sorted(nums) :
            return int(eval(st.split('==')[1]))  # if statement is valid it returns the value of the statement , eg : (2**3==8) it returns 8.
        else :
            return False
    else :
        return False
    
def play(name,cards=None):
    num = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13] # Total cards
    if not cards :
        cards = []
        for i in range(3):
            cards += [num.pop(random.randrange(len(num)))] # generating 3 random cards such that none of the card is repeated.
    Print('\nTurn : '+name+'\nyour cards : '+str(cards)+'\n')
    while True :
        Print('Enter Statement (\'//\' not allowed)\nOr press \'+\' to add 1 new card(-2 points)\nOr press \'0\' to skip\n : ', .01)
        statement = input()
        if statement == '+' and len(num) > 42: # user can take upto 7 additional cards.
            cards += [num.pop(random.randrange(len(num)))] # drawing a new card.
            Print('New set : '+str(cards)+'\n')
        elif statement == '0' :
            players[name] += [0-(len(cards)-3)*2] # user's final points.
            Print('\n'+player+' : + ( '+str(0-(len(cards)-3)*2)+' )\n')
            break
        else:
            p = check(statement, cards) 
            if p :
                players[name] += [int(abs(p))-(len(cards)-3)*2] # user's final points.
                Print('\n'+player+' : + ( '+str(abs(p)-(len(cards)-3)*2)+' )\n')
                break
            else :
                Print('wrong statment, Try again\n')
                print()

def newGame():
    '''This function initializes a new game'''
    Print('play with Ishan(0)/play with freinds(1) : ')
    mode = int(input())
    players = {}
    if mode :
        Print('mode : multi player\n')
        while True :
            Print('Enter player\'s name\nOr press \'Enter\' if you are done : ')
            player = input()
            if player:                # adds player's name in the 'players' dictionary. 
                players[player] = []
            else :                    # breaks the loop when '' is enterd.
                break
    else:
        Print('mode : single player\n')
        Print('Enter your name : ')
        players[input()] = []      # adds's player in the 'players' dictionary.
        players['Ishan'] = []      # add bot in the 'players' dictionary.
    return players
#-----------------------------------Main program--------------------------------------#
Print('How to play : Try to create a mathematical statement with given numbers\nEg:- with[2,3,5] you can say 2+3==5 or with[9,2,3] you can say 3**2==9\n\n', .03)
game = 0                          # game's default value is 0(a new game)   
if pausedGames :                  # True when there is atleast 1 game pending.
    Print('Start a new game(0)/Resume an old game(1) : ')
    game = int(input())           # pending game's index number
    if game:
        while True:
            Print('Which game would you want to continue '+str(pausedGames.keys())[10:-1]+' : ')
            game = int(input())
            if game in pausedGames:     # it checks wether the entered game index is present or not in the pending game's file.
                break
            Print('game does not exist\n\n')
        players = {}
        Print('Recap\n')
        for player in pausedGames[game]:
            players[player] = pausedGames[game][player]
            Print(str(player)+' : '+str(pausedGames[game][player])+'\n')
    else:
        players = newGame()
else :
    players = newGame()
spnFdng = 0
if not list(players.values())[0] :
    spnFdng = 2
spnFdng_user = [[2, 3, 8], [5, 8, 13], [3, 2, 9], [5, 2, 10], [6, 2, 12], [3, 3, 9], [13, 1, 12], [3, 4, 12]]
spnFdng_bot = [[1, 2, 3], [3, 5, 13], [13, 5, 2], [1, 10, 3], [2, 2, 4], [2, 1, 2], [3, 3, 5], [1, 1, 1]]
#------------------------------------Game begins----------------------------------------#
diff_optns = {1 : 'Easy', 2 : 'Medium' , 3 : 'Hard'}
difficulty = 1
while True :
    if 'Ishan' in players:
        Print(f'\nEnter [Play(1)/Save(s)/Exit(0)/Change difficulty(cd) (Current difficulty : {diff_optns[difficulty]})] : ', .03)
    else:
        Print('\nEnter [Play(1)/Save(s)/Exit(0)] : ')
    permission = input()
    
    if permission == 'cd' and 'Ishan' in players:
        Print('Set difficulty [Easy(1)/Medium(2)/Hard(3)] : ')
        while True:
            try:
                difficulty = int(input())
                break
            except:
                Print('Invalid input...\n')
    
    elif permission == '1':
        for player in players :
            if player == 'Ishan': # Bot's turn
                num = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12,13,13,13,13]
                if spnFdng <= 0 :            
                    cards = []
                    for i in range(3):
                        cards += [num.pop(random.randrange(len(num)))]
                else :
                    cards = spnFdng_bot[random.randrange(len(spnFdng_bot))]
                Print('\nTurn : Ishan\nIshan\'s cards : '+str(cards)+'\n')
                Print('Enter Statement (\'//\' not allowed)\nOr press \'+\' to add 1 new card(-2 points)\nOr press \'0\' to skip\n : ', .01)
                
                for i in range(difficulty-1):            
                    time.sleep(.5)
                    print('+')
                    cards += [num.pop(random.randrange(len(num)))]
                    time.sleep(.3)
                    Print('New set : '+str(cards)+'\n')
                    Print('Enter Statement (\'//\' not allowed)\nOr press \'+\' to add 1 new card(-2 points)\nOr press \'0\' to skip\n : ', .01)
                
                s = Bot.statement(cards) # s is a list containing all the possible combinations.
                st = Bot.choose(s)       # st is a list with 2 members [max points, statement with max points]
                if st:
                     Print(st[1])
                     p = int(st[0])
                     players['Ishan'] += [abs(p)-(len(cards)-3)*2]
                     Print('\n\nIshan : + ( '+str(abs(p)-(len(cards)-3)*2)+' )\n')
                else : # if st is still null.
                     time.sleep(.5)
                     print('0')
                     players['Ishan'] += [0-(len(cards)-3)*2]
                     Print('\n\nIshan : + ( '+str(0-(len(cards)-3)*2)+' )\n')
            else :   # player's turn
                if spnFdng <= 0 :
                     play(player)
                else :
                     play(player,spnFdng_user[random.randrange(len(spnFdng_user))])

    elif permission == 's' or permission == 'S' :
        # Saving current game in the game file.
        if game:
            pausedGames[game] = players
        elif pausedGames :
            pausedGames[max(pausedGames.keys())+1] = players
        else :
            pausedGames[1] = players
        file = open('Paused_games.py','w')
        file.write('pausedGames = '+str(pausedGames))
        file.close()
        Print('game has been Saved successfully')
        time.sleep(1)
        break

    else : # if permission is denied.
        max = 0
        winner = []
        for player in players :
            if sum(players[player]) > max :
                max = sum(players[player])
                winner = [player]
            elif sum(players[player]) == max:
                winner += [player]
            Print('\n'+player+' : '+str(players[player])+'\nTotal : '+str(sum(players[player]))+'\n')
        Print('\nWinner : '+str(winner))
        if game :
            # removing current game from the file.
            del pausedGames[game]
            file = open('Paused_games.py','w')
            file.write('pausedGames = '+str(pausedGames))
            file.close()
        feedBack = input('\n\nHow was the game : ')
        break
    spnFdng -= 1
