"""
Tic Tac Toe Player
"""

import math
import random
from copy import deepcopy

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
    # Scan board for entries and determine next player:

    x_count = 0
    o_count = 0
    empty_count = 0

    for row in range(3):
        for c in range(3):
            if board[row][c] == "X":
                x_count += 1
            elif board[row][c] == "O":
                o_count += 1
            else:
                empty_count += 1
        # X_count += row.count(X)
        # O_count += row.count(O)
        # EMPTY_count += row.count(EMPTY)

    # If X has more squares than O, its O's turn:
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i represents the board row, j the board column, both 0, 1 or 2
    The actions are are represented as the tuple (i, j) where the piece can be placed.
    """

    moves = set()

    for i in range(3):
        for j in range(3):
            #go through the board and add the empty places in the list 'moves'.
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Make a deep copy of the board and update with the current player's move:
    board_copy = deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows:
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    # Check columns:
    for j in range(3):
        column = ''
        for i in range(3):
            column += str(board[i][j])

        if column == 'XXX':
            return X
        if column == 'OOO':
            return O

    # Check Diagonals:
    d1 = ''
    d2 = ''
    j = 2

    for i in range(3):
        d1 += str(board[i][i])
        d2 += str(board[i][j])
        j -= 1

    if d1 == 'XXX' or d2 == 'XXX':
        return X
    elif d1 == 'OOO' or d2 == 'OOO':
        return O

    # Otherwise no current winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Game is over if it is a winning board or all tiles are full (no actions):

    if winner(board) or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def Max_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None]
    v = float('-inf')
    for action in actions(board):
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        if test > v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def Min_Value(board, Max, Min):
    move = None
    if terminal(board):
        return [utility(board), None];
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        if Max >= Min:
            break
    return [v, move];

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    'X' Player is trying to maximise the score, 'O' Player is trying to minimise it
    """

    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

