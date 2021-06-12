import signal

class TimeoutException(Exception):   # Custom exception class
    pass


def timeout_handler(signum, frame):   # Custom signal handler
    raise TimeoutException


def get_move_irp(current_state):

    if interrupt_mode == 0:
        return get_move(current_state)
    
    elif interrupt_mode == 1:
        i = 2
        move = get_move(current_state, 1)

        while True:
            temp = get_move(current_state, i)
            if temp == -1:
                return move
            move = temp
            i += 1
    else:
        i = 2
        move = get_move(current_state, 1)
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(30)
        try:
            while True:
                temp = get_move(current_state, i)
                move = temp
        except TimeoutException:
            return move

