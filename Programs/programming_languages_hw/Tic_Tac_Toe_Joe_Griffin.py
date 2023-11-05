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
        
    def legal_move(self,x,y):
        pass
    def make_move(self,x,y):
        pass
    def game_over(self):
        pass
    def play_game(self):
        pass
    def reset_game(self):
        pass
    def __repr__(self):
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
    def reset_game(self):
        self.board = []*self.size
        
        for i in range(0,self.size):
            temp=[]
            for j in range(0,self.size):
                temp.append("({},{})".format(i,j))
            self.board.append(temp)
    def legal_move(self,x,y):
        row=int(x)
        col=int(y)
        if (row >= self.size) or (row < 0):
            return False
        if (col >= self.size) or (col < 0):
            return False
        if (self.board[row][col] == "  X  " or self.board[row][col] == "  O  "):
            return False
        return True
    def make_move(self,x,y):
        row=int(x)
        col=int(y)
        
        self.board[row][col] = self.current_player
        self.num_moves += 1
        
        if (self.current_player == " X "):
            self.current_player = " O "
        else:
            self.current_player = " X "

    def play_game(self):
        print("*******************************\n\n")
        print(self)
        row_val = -1
        col_val = -1
        
        try:
            print("Please enter the row you wish to move in")
            row_input = input()
            print("Please enter the row you wish to move in")
            col_input = input()
            row_val = int(row_input)
            col_val = int(col_input)
        except ValueError as e:
            print("One of the values you entered was not an integer. Please try again")
            play_game()
        if (not (self.legal_move(row_val, col_val))): #If the coorindates entered are invalid targets
            print("You have entered an invalid row or column value")
            print("Please enter a value between 0 and " + str(self.size-1))
            self.play_game()
        else: #Needs to be in an else clause to prevent recursive badness!
            self.make_move(row_val, col_val)
            result = self.game_over()
            if (result == " X "):
                print("X has won the game!")
                self.X_score[0]+=1
                self.O_score[1]+=1
            elif (result == "  O  "):
                print("O has won the game!")
                self.X_score[1]+=1
                self.O_score[0]+=1
            elif (self.num_moves == (self.size ** 2)): # If our number of moves is equal to size^2 and no one has won, the game is a tie
                print("The game has ended in a tie!")
                self.X_score[2]+=1
                self.O_score[2]+=1
            else:
                self.play_game()
        
    def random_play_game(self,num):
        num_games = int(num)
        if (num_games < 10):
            num_games = 10
        elif (num_games > 1000):
            num_games = 1000
            
        print("Simulating " + str(num_games) + " number of random Tic-Tac-Toe games!")
        curr_games = 0
        game_won = False
        rand_x = 0
        rand_y = 0
        result = ""
        while (curr_games < num_games):
            self.reset_game()
            game_won = False
            result = "No winner"
            while (not game_won):
                rand_x = random.randint(0,self.size)
                rand_y = random.randint(0,self.size)
                print("player:",self.current_player,"move:",(rand_x,rand_y))
                if (self.legal_move(rand_x, rand_y)):
                    self.make_move(rand_x, rand_y)
                result = self.game_over()
                if (result == " X "):
                    print("X has won the game!")
                    self.X_score[0]+=1
                    self.O_score[1]+=1
                    game_won = True
                elif (result == "  O  "):
                    print("O has won the game!")
                    self.X_score[1]+=1
                    self.O_score[0]+=1
                    game_won = True
                elif (self.num_moves == (self.size ** 2)): # If our number of moves is equal to size^2 and no one has won, the game is a tie
                    print("The game has ended in a tie!")
                    self.X_score[2]+=1
                    self.O_score[2]+=1
                    game_won = True
                    
            curr_games+=1
            
        print("**************************\nTHE GAMES ARE OVER!\n\n");
        print("After " + str(num_games) + " we have the following records")
        result = "Player\tWins\tLosses\tTies\n";
        result += "X\t{0}\t{1}\t{2}\n".format(self.X_score[0],self.X_score[1],self.X_score[2])
        result += "O\t{0}\t{1}\t{2}\n".format(self.O_score[0],self.O_score[1],self.O_score[2])
        print(result)
    
    def game_over(self):
        i=0
        j=0
        #Horizontal check
        for i in range(0, self.size):
            all_same = True
            for j in range(0,self.size-1):
                if (self.board[i][j] != self.board[i][j+1]):
                    all_same = False
                    break
                
            if (all_same):
                return self.board[i][0]
        i=0
        j=0
        #Vertical check
        for j in range(0, self.size):
            all_same = True
            for i in range(0,self.size-1):
                if (self.board[i][j] != self.board[i+1][j]):
                    all_same = False
                    break
                
            if (all_same):
                return self.board[0][j]
        i=0
        #DIagonal check
        all_same = True
        for i in range(0, self.size-1):
            if (self.board[i][i] != self.board[i+1][i+1]):
                all_same = False
                break
        if (all_same):
            return self.board[0][0]
        i=0
        #Antidiagonal check
        all_same = True
        for i in range(0, self.size-1):
            if (self.board[i][self.size-1-i] != self.board[i+1][self.size-2-i]):
                all_same = False
                break
        if (all_same):
            return self.board[0][self.size-1]
        
        return "No Winner"
    
    def __repr__(self):
        result = "Current Game Stats\n"
        result += "Player\tWins\tLosses\tTies\n"
        result += "X\t{0}\t{1}\t{2}\n".format(self.X_score[0],self.X_score[1],self.X_score[2])
        result += "O\t{0}\t{1}\t{2}\n".format(self.O_score[0],self.O_score[1],self.O_score[2])
        result += "It is Player {}'s turn\n".format(self.current_player)
        result += "CURRENT BOARD\n"
        for i in range(0,self.size):
            for j in range(0,self.size):
                result += self.board[i][j] + "\t"
            result += "\n"
            
        return result

class TicTacToeTwo(TicTacToe):
    def __init__(self):
            pass

def main():
    pass

if __name__ == "__main__":
    tictactoe = TicTacToe(3)
    tictactoe.random_play_game(9)
    main()