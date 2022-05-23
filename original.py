"""
Tic Tac Toe Player
"""

from json.encoder import INFINITY
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == X:
                x += 1
            elif board[row][column] == O:
                o += 1

    return X if x == o else O
    

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i= action[0]
    j= action[1]
    board1 = copy.deepcopy(board)
    board1[i][j] = player(board1)
    return board1
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if row(board,O) or column(board,O) or toptobottom(board,O) or bottomtotop(board,O):
        return O
    elif row(board,X) or column(board,X) or toptobottom(board,X) or bottomtotop(board,X):
        return X



def row(board,player):
    for row in range(len(board)):
        count = 0
        for column in  range(len(board[0])):
            if board[row][column] == player:
                count += 1
        if count == len(board[0]):
            return True
    return False

def column(board,player):
    for row in range(len(board)):
        count = 0
        for column in range(len(board[0])):
            if board[column][row] == player:
                count += 1
        if count == len(board[0]):
            return True
    return False

def toptobottom(board,player):
    count = 0 
    for row in range(len(board)):
        for column in range(len(board[0])):
            if row == column and board[row][column] == player:
                count += 1

    return count == len(board[0])

def bottomtotop(board,player):
    count = 0
    for row in range(len(board)):
        for column in range(len(board)):
            if (len(board)-row-1) == column and board[row][column] == player:
                count += 1

    return count == len(board[0])

def istie(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] is not EMPTY:
                return False
    return True

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if istie(board) or winner(board) == X or winner(board) == O:
        return True
    else:
        return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif player(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        array = []
        for action in actions(board):
            array.append([minvalue(result(board,actions)),action])
        return sorted(array, key=lambda x: x[0],reverse=True)[0][1]
    elif player(board) == O:
        array = []
        for action in actions(board):
            array.append([maxvalue(result(board,actions)),action])
        return sorted(array, key=lambda x: x[0])[0][1]

def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -1000
    for action in actions(board):
        v = max(v,minvalue(result(board,action)))
    return v
   

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = 1000
    for action in actions(board):
        v = min(v,maxvalue(result(board,action)))
    return v
