#Project5
#Game_logic
#Yuanqin Fan / 34137914

Min_rowcol = 4
Max_rowcol = 16
Black = 'B'
White = 'W'
Coordinate = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]

class InvalidRowColumn(Exception):
    '''
    Raised whenever an invalid row or column number is entered
    '''
    pass

class InvalidMove(Exception):
    '''
    Raised whenever an invalid move is made
    '''
    pass

class Gameover(Exception):
    '''
    Raised whenever Game is over
    '''
    pass

class InvalidInput(Exception):
    '''
    Raised whenever an Invalid input is made
    '''
    pass

class Shift_Player(Exception):
    '''
    Raised whenever it need to shift to another player
    '''
    pass

class Othello:
    def __init__(self,row,col,first_player,top_left_player,rule):
        self._row = row
        self._col = col
        self._Topleft = top_left_player
        self._winrule = rule
        self._turn = first_player

    def _create_new_board(self):
        '''
        Create a new game board which can be used in the following function
        '''    
        gameboard = []
        for _ in range(self._row):
            gameboard.append(['.']*self._col)

        if self._Topleft == Black:
            another = White
            
        else:
            another = Black

        top_left_R = (self._row//2) - 1
        top_left_C = (self._col//2) - 1
        
        gameboard[top_left_R][top_left_C] = self._Topleft
        gameboard[top_left_R+1][top_left_C] = another
        gameboard[top_left_R][top_left_C+1] = another
        gameboard[top_left_R+1][top_left_C+1] = self._Topleft

        return gameboard

    def _print_board(self,board):
        '''
        Make the game board looks like a real game board(not lists)
        '''
        _rows = ''
        for row in range(len(board)):
            for col in range(len(board[row])):
                _rows += board[row][col] + '  '
            _rows += '\n'


        return _rows       

    def _print_discs_num(self,board):
        '''
        Counting Black and White dics number
        '''
        b_num = 0
        w_num = 0
        for row in board:
            for col in row:
                if col == Black:
                    b_num +=1
                if col == White:
                    w_num +=1
        return (b_num,w_num)

    def _get_the_other_player(self):
        '''
        Change player to another one
        '''
        if self._turn == Black:
            return White
        else:
            return Black

    def _change_turn(self):
        '''
        Change Turn to another player
        '''
        self._turn = self._get_the_other_player()

    def _check_move_path(self,board,move):
        '''
        To check if this move has valid path or not.
        Also check the situation that both player have
        no valid path and check the winner.
        '''
        row = int((move.split())[0])-1
        col = int((move.split())[1])-1
        space_list = self._get_available_space(board)
        if move not in space_list:
            raise InvalidMove
        another = self._get_the_other_player()
        path = []
        for x_dir,y_dir in Coordinate:
            X = row + x_dir
            Y = col + y_dir
            
            if self._check_dics_location(X,Y) == False:
                continue
            while board[X][Y] == another:
                X += x_dir
                Y += y_dir
                if not self._check_dics_location(X,Y):
                    break
            if self._check_dics_location(X,Y) == False:
                continue                             
            if board[X][Y] == self._turn:
                while not (X == row and Y == col):
                    X -= x_dir
                    Y -= y_dir
                    if board[X][Y] == another:
                        path.append([X,Y])

        if len(path) == 0:
            self._check_has_winner(board)
            raise InvalidMove
        return path

    def _check_dics_location(self,row,col):
        '''
        To check if this dics is on the board
        '''
        if (0<=row<self._row) and (0<=col<self._col):
            return True
        else:
            return False
    
    def _Reverse_the_path(self,board,path):
        '''
        Reverse the valid path which means change color
        of another's dics on this path
        '''
        for x,y in path:
            board[x][y] = self._turn
            
    def _Reverse_the_move(self,board,move):
        '''
        Change move point's color to current player
        '''
        row = int((move.split())[0])-1
        col = int((move.split())[1])-1        
        
        board[row][col] = self._turn        

    def _check_has_winner(self,board):
        '''
        If they are no empty space, game is over and we
        need to check winner
        '''
        space_list = self._get_available_space(board)

        if len(space_list) == 0:
            raise Gameover

    def _check_player_has_move(self,board):
        '''
        To check current player has valid move to reverse
        the valid path
        '''
        self._check_has_winner(board)
        
        space_list = self._get_available_space(board)
        for move in space_list:
            try:
                path = self._check_move_path(board,move)
                return True
            
            except:
                continue
        
        self._turn = self._get_the_other_player()
        
        for move in space_list:
            try:
                path = self._check_move_path(board,move,self._turn)
            
            except:
                continue
            
            else:
                raise Shift_Player
        

    def _get_available_space(self,board):
        '''
        To get empty space
        '''
        space = []
        for row in range(len(board)):
            for col in range(len(board[row])):               
                if board[row][col] == '.':                   
                    space.append('{0} {1}'.format(row+1,col+1))
        return space

    def _check_winner(self,board):
        '''
        According to the rule, get the winner
        '''
        B = self._print_discs_num(board)[0]
        W = self._print_discs_num(board)[1]
        if B == W:
            winner = 'NONE'
            return winner
                       
        if self._winrule == '>':
            if B > W:
                winner = Black
                return winner
            else:
                winner = White
                return winner
        if self._winrule == '<':
            if B < W:
                winner = Black
                return winner
            else:
                winner = White
                return winner
