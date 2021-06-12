def get_move(state):
    s=state.copy()
    root = node(s,'max')
    create_tree(root)
    alpha_beta (root, float('-inf'), float('inf'), 'max')
    for i in range(0,6):
        if root.children[i].cost == root.cost and children[i].pruned==0:
            print('wasalt')
            return i



'''
node attrbutes :
1) leaf --> equals one if the node is leaf , otherwise zero
2) cost --> equals the estimated cost 
3) mini_max --> equals 'max' if the node is maximizer and equals 'min' if the node is minimizer
4) children --> list contains childs of the node
5) state --> list contains state this node represnt 
6) pruned --> equals one if the node is pruned and zero other wise
'''
