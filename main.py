import save
import time
import signal
from Mancala import Mancala
from Mancala_Tree import Node , Tree

current_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
LEVELS = [1, 4, 7, 10]

#load = int(input("do you want to load game ? (yes = press 1, no = press 0)  \n"))
load = 0
stealing = 1
turn = ""
level = 1
interrupt_mode = 0
if load == 1:
    current_state, stealing, level, interrupt_mode = save.load()
    turn = 'min'
'''else:
    stealing = int(
        input("do you want stealing mode ? (yes = press 1, no = press 0)  \n"))
    turn = input(
        "do you want to start ? (yes = enter 'min', no = enter 'max')  \n")
    level = int(
        input("choose level: 1 - 2 - 3 - 4  \n"))-1
    interrupt_mode = int(
        input("force play method: 0- let the kid take his time\n1-CTRL+C\n2- 30s time limit   \n"))
'''
stealing = 1
turn = 'min'
level = 4
interrupt_mode = 2
Game = Mancala(is_Stealing = stealing, turn = turn)
Tree = Tree()

while True:
    ended, who_win = Game.is_end()
    if ended == 1:
        print('game ended\n and the result is -->', who_win)
        break
    print(Game.turn)
    if Game.turn == 'min':
        user_move = int(
            input('it is your turn Enter a number from 1 to 6 or 0 to save and exit\n'))+6
        if user_move == 6:
            save.save(current_state, stealing, level, interrupt_mode)
            break

        Game = Game.move(user_move)
        while Game.valid_move == False:
            user_move = int(
                input('this is not a valid move try again,  Enter a number from 1 to 6\n'))+6
            if user_move == 6:
                save.save(current_state, stealing, level, interrupt_mode)
                break
            Game = Game.move(user_move)
        print('this is your play')
        Game.print()
        print("--------------------")
    else:
        print('this is my move')

        #t1 = time.time()
        suggested_move = Tree.get_move(Game,7)
        #print("time: ", time.time()-t1)
        Game = Game.move(suggested_move)
        Game.print()
        print("--------------------")
