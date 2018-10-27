#Project5
#User_input
#Yuanqin Fan / 34137914
import Project5_Game_logic


def ask_for_row(row:int):
    '''
    To get a valid row number between maximum and minimun
    '''

    if not Project5_Game_logic.Min_rowcol<=row<=Project5_Game_logic.Max_rowcol:
        raise Project5_Game_logic.InvalidRowColumn
    return row


def ask_for_col(col:int):
    '''
    To get a valid column number between maximum and minimum
    '''

    if not Project5_Game_logic.Min_rowcol<=col<=Project5_Game_logic.Max_rowcol:
        raise Project5_Game_logic.InvalidRowColumn
    return col


def ask_for_first_player(first_player:str):
    '''
    To get a valid first player(B or W)
    '''

    if (first_player == 'W') or (first_player == 'B'):
        return first_player
    else:
        raise Project5_Game_logic.InvalidInput


def ask_for_top_left_player(top_left_player:str):
    '''
    To get a valid top left player(B or W)
    '''

    if top_left_player == 'B' or top_left_player == 'W':
        return top_left_player
    else:
        raise Project5_Game_logic.InvalidInput


def ask_for_rule(rule: '< or >'):
    '''
    To get a valid rule (> or <)
    '''
    if rule == '>' or rule == '<':
        return rule
    else:
        raise Project5_Game_logic.InvalidInput

def ask_for_move():
    '''
    To get a valid move
    '''
    while True:
        move = input()
        try:
            row = int((move.split())[0])-1
            col = int((move.split())[1])-1
            return move
        except: 
            print('Invalid move. Try again.')
            continue


