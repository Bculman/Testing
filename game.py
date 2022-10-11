from lib2to3.pytree import LeafPattern
from random import gammavariate
from player import HumanPlayer, RandomComputerPlayer, Gcomp

class TicTacToe:
    def __init__(self):
        self.board=[ ' ' for _ in range(9)]
        self.current_winner = None 

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) +'  |')


    @staticmethod
    def print_board_nums():
        # 0|1|2 ect
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) +'  |')

    def availabe_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
       # moves=[]
       # for (i,spot) in enumerate(self.board):
       #     if x == ' ':
       #         moves.append(i) 
       # return moves

    def empty_squares(slef):
        return ' ' in slef.board

    def num_empty_squares(slef):
        return slef.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square]= letter
            if self.winner(square, letter):
                self.current_winner= letter
            return True
        else:
            False
    def winner(self, square, letter):
        row_ind = square // 3 
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diag1= [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diag1]):
                return True
            diag2= [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diag2]):
                return True
        return False


def play(game, xp, op, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' 
    while game.empty_squares():
        if letter == 'O':
            square = op.get_move(game)
        else:
            
            square = xp.get_move(game)
            

        if game.make_move(square, letter):
            if print_game:
                print( letter + f' makes a move to squre {square}')
                game.print_board()
                print('')
            if game.current_winner:
                if print_game:
                    print( letter + ' Wins')
                return letter


            letter = 'O' if letter == 'X' else 'X'
            

    if print_game:
        print('Its a tie')

if __name__== '__main__':
    xp= HumanPlayer('X')       
    op= Gcomp('O')
    t = TicTacToe()
    play(t, xp, op, print_game=True)
