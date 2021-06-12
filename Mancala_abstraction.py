class node:
    def __init__(self, state, turn):

        self.is_leaf = 0
        self.cost = 0
        self.min_max = turn
        self.children = []
        self.state = state
        self.pruned = 0
        self.move_made_me = 0

def create_tree(root, depth):

    if depth == 0:
        root.is_leaf = 1
        root.cost = cost_fun(root.state)
        return root
    if root.min_max == 'max':
        places = range(0, 6)
    else:
        places = range(7, 13)

    for place in places:
        valid_move, returned_state, turn = make_move(place, root.state)
        if valid_move == 0:
            continue
        child_Node = node(returned_state, turn)
        child_Node.move_made_me = place
        temp = create_tree(child_Node, depth-1)
        root.children.append(temp)
    return root


def is_end(state):
    s = state.copy()
    sum_max = 0
    sum_min = 0
    who_win = 'computer winned'
    for i in range(0, 6):
        sum_max += s[i]
        sum_min += s[i+7]
    if sum_max == 0:
        ended = 1
        if s[6] > 48-s[6]:
            who_win = 'computer winned'
        elif s[6] < 48-s[6]:
            who_win = 'player winned'
        else:
            who_win = 'Draw'
    elif sum_min == 0:
        ended = 1
        if s[13] > 48-s[13]:
            who_win = 'player winned'
        elif s[13] < 48-s[13]:
            who_win = 'compuuter winned'
        else:
            who_win = 'Draw'
    else:
        ended = 0
    return ended, who_win



def make_move(selected_place,current_state):
    num_of_stones=current_state[selected_place]
    if num_of_stones==0 or selected_place not in range(0,13) :
        valid_move=0
    else:
        valid_move=1
    if selected_place in range(0,6):
        turn = 'min'
    elif selected_place in range(7,13):
        turn = 'max'

    returned_state=current_state.copy()
    returned_state[selected_place]=0
    place_to_add_stone=selected_place+1

    while True:
        if num_of_stones==0:
            break
        if stealing==1 and num_of_stones==1 and selected_place in range(0,6) and place_to_add_stone in range(0,6) and returned_state[place_to_add_stone]==0:
            returned_state[6]+=returned_state[12-place_to_add_stone]+1
            returned_state[12-place_to_add_stone]=0
            break
        if stealing==1 and num_of_stones==1 and selected_place in range(7,13) and place_to_add_stone in range(7,13) and returned_state[place_to_add_stone]==0:
            returned_state[13]+=returned_state[12-place_to_add_stone]+1
            returned_state[12-place_to_add_stone]=0
            break
        if num_of_stones==1 and selected_place in range(0,6) and place_to_add_stone==6:
            turn = 'max'
        if num_of_stones==1 and selected_place in range(7,13) and place_to_add_stone==13:
            turn = 'min'
        if not(((selected_place in range(0,6)) and (place_to_add_stone==13)) or((selected_place in range(7,13)) and (place_to_add_stone==6))):
            returned_state[place_to_add_stone]+=1
            num_of_stones-=1
        place_to_add_stone+=1
        place_to_add_stone=place_to_add_stone%14
    return valid_move, returned_state, turn
        

'''
state=[4,4,4,4,4,400,0,4,4,4,4,4,4,0]
stealing = int(input("do you want stealing mode ? (yes = press 1, no = press 0)  \n"))
make_move(5,state)
x,y,z=make_move(5,state)
'''
