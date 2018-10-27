#Project5
#Graph User Interface
#Yuanqin Fan / 34137914
import tkinter
import Project5_Game_logic
import Project5_User_input
DEFAULT_FONT = ('Helvetica', 30)

class Othello_Dialog:
    def __init__(self):
        ''' Create an othello Dialog window to ask for some input
            which is important to create a game board
        '''

        self._init_window = tkinter.Tk()
        self._init_window.title('Init_Othello_FULL')
        
        self._init_window.rowconfigure(0 ,weight=1)
        self._init_window.rowconfigure(1 ,weight=1)
        self._init_window.rowconfigure(2 ,weight=1)
        self._init_window.rowconfigure(3 ,weight=1)
        self._init_window.rowconfigure(4 ,weight=1)
        self._init_window.rowconfigure(5 ,weight=1)
        self._init_window.columnconfigure(0 ,weight=1)
        self._init_window.columnconfigure(1 ,weight=1)
        
        self.Canvas()
        self.Labels_and_button()

        self._start_clicked = False
        self._Row = ''
        self._Column = ''
        self._FP = ''
        self._TP = ''
        self._Rule = ''

    def Canvas(self):
        ''' A canvas that contains several texts and labels
            and can be resized
        '''
        self._Canvas = tkinter.Canvas(
            master = self._init_window, width = 300, height = 100,
            background = '#618fd8')
        self._Canvas.grid(row = 0, column = 0, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._Canvas.bind('<Configure>', self._on_canvas_resized)

    def _on_canvas_resized(self, event:tkinter.Event):
        self._create_text()
        
    def _create_text(self):
        self._Canvas.delete(tkinter.ALL)
        width = self._Canvas.winfo_width()
        height = self._Canvas.winfo_height()
        self._Canvas.create_text(width * 0.5, height * 0.5,
                                 text='Othello',
                                 font = DEFAULT_FONT)

    def Labels_and_button(self):
        ''' Row,Columns,First player, Top left Player's label
            and entry space for them. Also the start button
            which in the button frame
        '''
        Rows_label = tkinter.Label(
            master = self._init_window, text = 'Row(4~16):',
            font = ('Helvetica', 18))
        Rows_label.grid(
            row = 1, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        Columns_label = tkinter.Label(
            master = self._init_window, text = 'Column(4~16):',
            font = ('Helvetica', 18))
        Columns_label.grid(
            row = 2, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        First_player_label = tkinter.Label(
            master = self._init_window, text = 'First Player(B or W):',
            font = ('Helvetica', 18))
        First_player_label.grid(
            row = 3, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)
        
        TL_player_label = tkinter.Label(
            master = self._init_window, text = 'TopLeft Player(B or W):',
            font = ('Helvetica', 18))
        TL_player_label.grid(
            row = 4, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        Rule_label = tkinter.Label(
            master = self._init_window, text = 'Rule(< or >):',
            font = ('Helvetica', 18))
        Rule_label.grid(
            row = 5, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

        self.Rows_entry = tkinter.Entry(
            master = self._init_window, width = 20, font = DEFAULT_FONT)
        self.Rows_entry.grid(
            row = 1, column = 1, pady = 10,
            sticky = tkinter.W + tkinter.E)

        self.Columns_entry = tkinter.Entry(
            master = self._init_window, width = 20, font = DEFAULT_FONT)
        self.Columns_entry.grid(
            row = 2, column = 1, pady = 10,
            sticky = tkinter.W + tkinter.E)

        self.First_Player_entry = tkinter.Entry(
            master = self._init_window, width = 20, font = DEFAULT_FONT)
        self.First_Player_entry.grid(
            row = 3, column = 1, pady = 10,
            sticky = tkinter.W + tkinter.E)

        self.TL_entry = tkinter.Entry(
            master = self._init_window, width = 20, font = DEFAULT_FONT)
        self.TL_entry.grid(
            row = 4, column = 1, pady = 10,
            sticky = tkinter.W + tkinter.E)

        self.Rule_entry = tkinter.Entry(
            master = self._init_window, width = 20, font = DEFAULT_FONT)
        self.Rule_entry.grid(
            row = 5, column = 1, pady = 10,
            sticky = tkinter.W + tkinter.E)
        
        button_frame = tkinter.Frame(master = self._init_window)
        button_frame.grid(
            row = 6, column = 1, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        Start_button = tkinter.Button(
            master = button_frame, text = 'Start', font  = ('Helvetica', 15),
            command = self._start_button_clicked)
        Start_button.grid(
            row = 0, column = 0, padx = 10, pady = 10)

        self.Exception_Frame = tkinter.Frame(master = self._init_window)
        self.Exception_Frame.grid(
            row = 6, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.W + tkinter.S)
        self.exception_label_1 = tkinter.Label(
            master = self.Exception_Frame, text = 'Invalid Row or Col',
            font = ('Helvetica', 15), foreground = 'red')
        self.exception_label_2 = tkinter.Label(
            master = self.Exception_Frame, text = 'Invalid Player or Rule',
            font = ('Helvetica', 15), foreground = 'red')
        

        
    def _start_button_clicked(self):
        ''' collect information from the entry space
             and check if these information are valid
             by using game logic. And then, open board
        '''
        self._Row = int(self.Rows_entry.get())
        self._Column = int(self.Columns_entry.get())
        self._FP = self.First_Player_entry.get()
        self._TP = self.TL_entry.get()
        self._Rule = self.Rule_entry.get()
        while True:
            try:
                Project5_User_input.ask_for_row(int(self._Row))
                Project5_User_input.ask_for_col(int(self._Column))
                Project5_User_input.ask_for_first_player(self._FP)
                Project5_User_input.ask_for_top_left_player(self._TP)
                Project5_User_input.ask_for_rule(self._Rule)
                
            except Project5_Game_logic.InvalidRowColumn:
                self.exception_label_2.grid_forget()
                self._Exception_Frame__1()
                break
            except:
                self.exception_label_1.grid_forget()
                self._Exception_Frame__2()
                break
            
            else:
                Game_board = Othello_Board(self)
                Game_board.show()
                break
            
    def _Exception_Frame__1(self):
        ''' A frame to raise exception whenever it has error'''
        self.exception_label_1.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

    def _Exception_Frame__2(self):
        ''' A frame to raise exception whenever it has error'''
        self.exception_label_2.grid(
            row = 0, column = 0,
            sticky = tkinter.N + tkinter.S + tkinter.W)

    def run(self):
        self._init_window.mainloop()

class Othello_Board:
    def __init__(self,Game_infor: Othello_Dialog):
        ''' Create a othello board by using information which
            is got from othello dialog. and start game
        '''
        self._Othello_window = tkinter.Toplevel()
        self._Othello_window.title('Othello_Game_Board')
        self._Othello_window.rowconfigure(0 ,weight=1)
        self._Othello_window.rowconfigure(1 ,weight=1)
        self._Othello_window.rowconfigure(2 ,weight=1)
        self._Othello_window.columnconfigure(0 ,weight=1)
        self._Othello_window.columnconfigure(1 ,weight=1)
        
        self._Game_infor = Game_infor
        self._othello = Project5_Game_logic.Othello(
            self._Game_infor._Row,
            self._Game_infor._Column,
            self._Game_infor._FP,
            self._Game_infor._TP,
            self._Game_infor._Rule)
        
        self.board = self._othello._create_new_board()
        
        self._Game_infor_Canvas()
        self._Game_board_Canvas()
        self._Game_button_Canvas()

    def _Game_infor_Canvas(self):
        ''' Game information canvas which contains whose turn,
            white and black's number and also the winner label
            when the game is over
        '''
        self._infor_Canvas = tkinter.Canvas(
            master = self._Othello_window, width = 500, height = 150,
            background = '#618fd8')
        self._infor_Canvas.grid(
            row = 0, column = 0, columnspan =2,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._infor_Canvas.bind('<Configure>', self._infor_canvas_resized)

    def _infor_canvas_resized(self,event:tkinter.Event):
        self._rewrite_information()

    def _rewrite_information(self, winner = ''):
        self._infor_Canvas.delete(tkinter.ALL)
        width = self._infor_Canvas.winfo_width()
        height = self._infor_Canvas.winfo_height()
        self._infor_Canvas.create_text(width * 0.5, height * 0.2,
                                        text = 'Othello_FULL' ,
                                        font = ('Helvetica', 25))
        self._infor_Canvas.create_text(width * 0.5, height * 0.5,
                                     text = 'Turn:' + self._othello._turn,
                                     font = ('Helvetica', 25))
        
        self._infor_Canvas.create_text(width * 0.25, height * 0.8,
                                     text = 'White:' + str(self._othello._print_discs_num(self.board)[1]),
                                     font = ('Helvetica', 25))
        self._infor_Canvas.create_text(width * 0.75, height * 0.8,
                                     text = 'Black:' + str(self._othello._print_discs_num(self.board)[0]),
                                     font = ('Helvetica', 25))
        self._infor_Canvas.create_text(width * 0.5, height * 0.8,
                    text = 'Winner: '+ winner,
                    font = ('Helvetica', 20))

    def _Game_board_Canvas(self):
        ''' Game board canvas is the real game board that
            we are playing right now
        '''
        self._board_Canvas = tkinter.Canvas(
            master = self._Othello_window, width = 500, height = 400)
        self._board_Canvas.grid(
            row = 1, column = 0, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        self._board_Canvas.bind('<Configure>', self._Draw_game_board)
        self._board_Canvas.bind('<Button-1>', self._Start_game_click)
        
    def _Draw_piece(self,a,b,c,d,e):
        if e == 'B':
            self._board_Canvas.create_oval(a,b,c,d,fill = 'Black')
        else:
            self._board_Canvas.create_oval(a,b,c,d,fill = 'White')
            
    def _Draw_game_board(self,event:tkinter.Event):
        ''' Draw the lines and dices when the game begin and
            update the dices while we are playing
        '''
        self._board_Canvas.delete(tkinter.ALL)
        width = self._board_Canvas.winfo_width()
        height = self._board_Canvas.winfo_height()
        Row = self._Game_infor._Row
        Col = self._Game_infor._Column
        self._cell_width = width / Col
        self._cell_height = height / Row
        
        for row in range(1, Row):
            self._board_Canvas.create_line(
                0,(row/Row)*height,
                width,(row/Row)*height)

        for col in range(1, Col):
            self._board_Canvas.create_line(
                (col/Col)*width,0,
                (col/Col)*width,height)

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != '.':
                    self._Draw_piece(c/Col*width,r/Row*height,(c+1)/Col*width,(r+1)/Row*height,
                                     self.board[r][c])

        
    def _Start_game_click(self,event:tkinter.Event):
        ''' Click the game board to play game and always
            check if the move is valid by using game logic
            and find out who is the winner in the end
        '''
        width = self._board_Canvas.winfo_width()
        height = self._board_Canvas.winfo_height()
        Row = self._Game_infor._Row
        Col = self._Game_infor._Column

        try:
            col =  int((event.x/width)*self._Game_infor._Column)+1
            row =    int((event.y/height)*self._Game_infor._Row)+1                    
            self._othello._check_player_has_move(self.board)
            move = str(row) +' '+ str(col)
            path = self._othello._check_move_path(self.board,move)
            self._othello._Reverse_the_path(self.board,path)
            self._othello._Reverse_the_move(self.board,move)
            for r,c in path:
                self._Draw_piece(c/Col*width,r/Row*height,
                                (c+1)/Col*width,(r+1)/Row*height,self._othello._turn)
            self._Draw_piece((col-1)/Col*width,(row-1)/Row*height,
                                col/Col*width,row/Row*height,self._othello._turn)
            self._othello._change_turn()
            self._rewrite_information()
            self._othello._check_has_winner(self.board)
        except Project5_Game_logic.InvalidMove:
            pass
        except Project5_Game_logic.Shift_Player:
            pass
        except Project5_Game_logic.Gameover:
            winner = self._othello._check_winner(self.board)
            self._rewrite_information(winner)

    def _Game_button_Canvas(self):
        ''' It contains a 'quit' button and its function
            is to close the game board window whenever we want
        '''
        Game_button_frame = tkinter.Frame(master = self._Othello_window)
        Game_button_frame.grid(
            row = 3, column = 0, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        Quit_button = tkinter.Button(
            master = Game_button_frame, text = 'Quit', font  = ('Helvetica', 18),
            command = self._Quit_Game)
        Quit_button.grid(
            row = 0, column = 0, padx = 10, pady = 10)

    def _Quit_Game(self):
        self._Othello_window.destroy()
        

    def show(self):
        self._Othello_window.grab_set()
        self._Othello_window.wait_window()

if __name__ == '__main__':
    othello = Othello_Dialog()
    othello.run()
