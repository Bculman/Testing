# Minesweeper Game 
import random
import re
import string

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs= num_bombs
        
        #create the board
        
        self.board= self.make_new_board() # making object in object 
        
        self.assign_values()
        
        
        #keep track of where we have dug
        self.dug = set() # 
        self.flag=set()
        
    def make_new_board(self):
        # makes new board based on the dim size and num bombs
        
        #makes new board
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        bombs_planted= 0 
        #plants the bombs randomly 
        while bombs_planted < 10 :
            locx = random.randint(0,10-1)
            locy = random.randint(0, 10-1)
            if board[locx][locy] == None :
                board[locx][locy]= '*'
                bombs_planted +=1
        return board

    def assign_values(self):
        # fills each square with the number of bombs that square is touching 
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c]=='*':
                    continue
                num_neigh_bomb=0    
                for ro in range(r-1, (r+1)+1):
                    for co in range(c-1, (c+2)):
                        if -1< ro < self.dim_size and -1< co < self.dim_size:
                            if self.board[ro][co] == '*':
                                num_neigh_bomb+=1
                    self.board[r][c]=num_neigh_bomb 
                
                
                
    def dig(self, row, col):
        # user selects where tehy want ot dig and then check if bomb and return the number of squares touching
        #if no neighboring bombs, keep checking neighbors 
        
        self.dug.add((row, col))
        
        
        if self.board[row][col] == '*': #if bomb retrun false so we know we lost 
            return False
        elif self.board[row][col] > 0:  # if greater than one then return true so can guess agian
            return True 
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)
                           
                           
        return True 
    
        
        
    
    def strpint(self,flagR, flagC, flag, newflag): #__str__(self):
        # prints out the board for the player
        #also allows the player to flag places where they think there is a bomb, 
        
        showBoard=[[ None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        
        if newflag > 0:
            self.flag.add((flagR,flagC))
           
        for row in range(self.dim_size): 
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    showBoard[row][col]=str(self.board[row][col])
                elif (row,col) in self.flag: 
                    showBoard[row][col]='X'
                else:
                    showBoard[row][col]=' '
                    
        print('    0','   1','   2','   3','   4','   5','   6','   7','   8','   9')    
        for i in range(self.dim_size):       
            print(i,showBoard[i])
     
    def lost(self):
        print('0','1','2','3','4','5','6','7','8','9')
        for i in range(self.dim_size):
            print(i,self.board[i])

def play(dim_size = 10, num_bombs=10):
    #step 1: creat board and plant bombs
    #step 2: show user board and ask for where they want to dig
    #step 3a: if location is bomb, show game over
    #step 3b: if location not a bomb show how many bombs its touching and dig recursively until each square is at least next to a bomb
    #step 4: repate step 2 and 3 untill no more places to dig
    board=Board(dim_size, num_bombs)
    flag=0
    flagR=-1
    flagC=-1
    newflag=0
    while len(board.dug)< board.dim_size **2 -num_bombs:
        board.strpint(flagR,flagC,flag,newflag) 
        print('you have flaged ' , flag,' bombs')
        flag_plant=input('would you like to flag a bomb y/n: ').upper()
        while flag_plant == 'Y':
            print('you have flaged ' , flag,' bombs')    
            flag_input= re.split(',(\\s)*', input("Flag Bomb row,col: "))
            flagR, flagC= int(flag_input[0]), int(flag_input[-1])
            flag+=1
            newflag=1
            board.strpint(flagR,flagC, flag,newflag)
            newflag=0
            flag_plant=input('would you like to flag a bomb y/n: ').upper()
        
        print('you have flaged ' , flag,' bombs')
        user_input= re.split(',(\\s)*', input("Dig row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        #add location validation
        
        safe = board.dig(row, col)
        if not safe:
            print("bomb")
            break
        #if flag == num_bombs:
            
    if safe:
         print("win")
    else:
        print("lost")
        board.lost()
        
    
    print(board)
    
    
    
play()    
    
    
    
    
    
    
    
    
