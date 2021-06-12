import numpy as np
import matplotlib as plt
import importlib
from Mancala import Mancala

class Node:
    def __init__(self, current_state):
        super(Node, self).__init__()
        self.future_states = [] 
        self.mancala = current_state
        self.pruned = 0

class Tree:
    
    def createNode(self, state = None , Next_turn = None,previous_move = -1):
        
        mancala_state = Mancala(Initial_State = state, turn = Next_turn)
        mancala_state.previous_move = previous_move
        return Node(mancala_state)

    def createTree(self,root,depth):

        if depth == 0:
            return root
        Valid_moves = range(0,6) if root.mancala.turn == 'min' else range(7,13)
        for move in Valid_moves:
            Next = root.mancala.move(move)
            child_Node = self.createNode(Next.state,Next.turn,move) 
            root.future_states.append(self.createTree(child_Node,depth - 1))
        return root
    def alpha_beta(self,node, alpha, beta):
        if node.future_states == []:
            return node.mancala.cost

        if node.mancala.turn == 'max':
            temp = float('-inf')
            for child in node.future_states:
                child.mancala.cost = self.alpha_beta(child, alpha, beta)
                temp = max(temp, child.mancala.cost)
                alpha = max(alpha, temp)
                if alpha >= beta:
                    node.pruned = 1
                    break  # beta cutoff
            node.mancala.cost = temp
            return temp

        elif node.mancala.turn == 'min':
            temp = float('inf')
            for child in node.future_states:
                child.mancala.cost = self.alpha_beta(child, alpha, beta)
                temp = max(temp, child.mancala.cost)
                beta = min(beta, temp)
                if beta <= alpha:
                    node.pruned = 1
                    break  # alpha cutoff
            node.mancala.cost = temp
            return temp
    def get_move(self,state, depth):
        try:
            root = Node(state)
            root = self.createTree(root, depth)
            self.alpha_beta(root, float('-inf'), float('inf'))
            temp = []
            for child in root.future_states:
                if child.mancala.cost == root.mancala.cost:
                    temp.append(child)
            if len(temp) > 1:
                for i in temp:
                    if i.pruned == 0:
                        return i.mancala.previous_move
            else:
                return temp[0].mancala.previous_move
        except KeyboardInterrupt:
            return -1

    def search(self, node, data):
        """
        Search function will search a node into tree.
        """
        return


    def deleteNode(self,node,data):
        """
        Delete function will delete a node into tree.
        """
        return


    def traverseInorder(self, root):
        """
        traverse function will print all the node in the tree.
        """
        for move in root.future_states:
            if move is not None:
                move.mancala.print()
                self.traverseInorder(move)


if __name__ == "__main__":
    T = Tree()
    m = Mancala()
    N = T.createNode(m.state,m.turn)
    r = T.createTree(N,1)
    q = T.get_move(m.state,7)
    T.traverseInorder(N)
