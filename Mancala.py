class Mancala():
    """docstring for Mancala"""
    def __init__(self, Initial_State = None,is_Stealing = True, turn = 'max'):
        super(Mancala, self).__init__()
        self.state = []
        if Initial_State is None:
            self.state = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]
        else:
            self.state = Initial_State

        self.Stealing = is_Stealing
        self.turn = turn
        self.valid_move = True
        self.previous_move = -1
        self.cost = self.cost_Function()

    def cost_Function(self):
        cost = -1*sum([x1 - x2 for (x1, x2) in zip(self.state[0:5], self.state[7:12])])
        return cost

    def is_end(self):
        sum_max = sum(self.state[0:6])
        sum_min = sum(self.state[7:13])
        who_win = 'computer winned'

        if sum_max == 0:
            ended = 1
            who_win = 'computer winned' if self.state[6] > 24 else 'player winned'
        elif sum_min == 0:
            ended = 1
            who_win = 'computer winned' if self.state[13] > 24 else 'player winned'
        else:
            ended = 0
        return ended, who_win

    def print(self):
        temp = self.state[7:13]
        temp.reverse()
        print('player -->', ' ', self.state[13], temp)
        print('computer --> ', '', self.state[0:6], self.state[6])

    def move(self,selected_place):
        num_of_stones = self.state[selected_place]
        if num_of_stones==0 or selected_place not in range(0,13) :
            self.valid_move = False
        else:
            self.valid_move = True

        if selected_place in range(0, 6):
            self.turn = 'min'
        elif selected_place in range(7, 13):
            self.turn = 'max'
        next_state = self.state.copy()
        next_state[selected_place] = 0
        place_to_add_stone = selected_place + 1
        
        Capture_pit = 13 if self.turn == 'max' else 6
        Other_Capture_pit = 6 if self.turn == 'max' else 13
        while True:
            if num_of_stones == 0 :
                break
            
            if num_of_stones == 1 :

                if self.Stealing == True and next_state[place_to_add_stone] == 0 and self.state[12-place_to_add_stone] != 0 :                    
                    next_state[Capture_pit] += next_state[12 - place_to_add_stone] + 1
                    next_state[12 - place_to_add_stone] = 0
                    break
                
                if place_to_add_stone == Capture_pit :
                    self.turn = 'min' if self.turn == 'max' else 'max'
            
            if place_to_add_stone != Other_Capture_pit:
                next_state[place_to_add_stone] += 1
                num_of_stones -= 1


            place_to_add_stone = (place_to_add_stone + 1) % 14

        returned_state = Mancala(next_state, self.Stealing, self.turn)
        returned_state.previous_move = selected_place
        return returned_state

if __name__ == '__main__':
    
    q = Mancala(turn = 'min')
    q.print()
    print(q.turn)
    l = q.move(7)
    l.print()
    print(l.turn)
    q = l.move(4)
    q.print()
    print(q.turn)
