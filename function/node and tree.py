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


