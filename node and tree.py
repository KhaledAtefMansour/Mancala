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


