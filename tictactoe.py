"""
Tic Tac Toe Player
"""

import math
import copy
from typing import final

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
    count = 0
    for row in board:
        for square in row:
            if square is not EMPTY:
                count += 1
    return X if count % 2 == 0 else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise NameError("Illegal move")
    new_board = copy.deepcopy(board)
    turn = player(board)
    new_board[action[0]][action[1]] = turn
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    victor = winner(board)
    for row in board:
        for square in row:
            if square is not EMPTY:
                count += 1
    return True if count == 9 or victor is not None else False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    maximize = True if player(board) == X else False
    def action_value(board, maximize):
        util = utility(board)
        if terminal(board):
            return util
        moves = actions(board)
        move_utilities = []
        for move in moves:
            move_utilities.append(action_value(result(board, move), not maximize))
        return max(move_utilities) if maximize else min(move_utilities)
    moves = list(actions(board))
    values = []
    for move in moves:
        new_board = result(board, move)
        values.append(action_value(new_board, not maximize))
    return moves[values.index(max(values))] if maximize else moves[values.index(min(values))]
