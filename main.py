import save
import time
import signal

current_state = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
LEVELS = [1, 4, 7, 10]

load = int(input("do you want to load game ? (yes = press 1, no = press 0)  \n"))
stealing = 1
turn = ""
level = 1
interrupt_mode = 0
if load == 1:
    current_state, stealing, level, interrupt_mode = save.load()
    turn = 'min'

else:
    stealing = int(
        input("do you want stealing mode ? (yes = press 1, no = press 0)  \n"))
    turn = input(
        "do you want to start ? (yes = enter 'min', no = enter 'max')  \n")
    level = int(
        input("choose level: 1 - 2 - 3 - 4  \n"))-1

    interrupt_mode = int(
        input("force play method: 0- let the kid take his time\n1-CTRL+C\n2- 30s time limit   \n"))


 
while True :
    ended,who_win = is_end(current_state)
    if ended==1:
        print('game ended\n and the result is -->',who_win)
        break
    if turn=='min':
        print_state(current_state)
        user_move=int(input('it is your turn Enter a number from 1 to 6\n'))+6
        valid_move, returned_state, next_turn=make_move(user_move,current_state)
        while valid_move==0:
            user_move=int(input('this is not a valid move try again,  Enter a number from 1 to 6\n'))+6
            valid_move, returned_state, next_turn=make_move(user_move,current_state)
        state=returned_state
        turn = next_turn
        print('this is the your play')
        print_state(current_state)
    else:
        print('this is my move')
        suggested_move=get_move(current_state)
        valid_move, returned_state, next_turn=make_move(suggested_move,current_state)
        state=returned_state
        turn = next_turn



