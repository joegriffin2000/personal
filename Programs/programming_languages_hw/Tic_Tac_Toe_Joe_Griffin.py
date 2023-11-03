#
# tic tac toe
#

import random

class Game():
    def __init__(self):
        self.num_moves = 0
        self.board = []
        self.current_player= " X "
        self.size = 0
        self.X_score = [0,0,0]
        self.O_score = [0,0,0]
        
    def legal_move(x,y):
        pass
    def make_move(x,y):
        pass
    def game_over():
        pass
    def play_game():
        pass
    def reset_game():
        pass
    def __repr__():
        pass

class TicTacToe(Game):
    def __init__(self,size):
        super().__init__()
        try:
            self.size = int(size)
        except:
            print("Illegal size entered, setting size to 3")
            self.size = 3
        
        if (self.size < 3) or (self.size > 9):
            print("Illegal size entered, setting size to 3")
            self.size = 3
            
        self.board = []*self.size
        
        for i in range(0,self.size):
            temp=[]
            for j in range(0,self.size):
                temp.append("({},{})".format(i,j))
            self.board.append(temp)
            
        
    def reset_game():
        self.board = []*self.size
        
        for i in range(0,self.size):
            temp=[]
            for j in range(0,self.size):
                temp.append("({},{})".format(i,j))
            self.board.append(temp)

    def legal_move():
        pass
    
    def play_game():
        pass
    
    def random_play_game():
        pass
    
    def game_over():
        pass
    
    def __repr__():
        pass

class TicTacToeTwo(TicTacToe):
    def __init__(self):
            pass

def main():
    pass

if __name__ == "__main__":
    TicTacToe(3)
    main()