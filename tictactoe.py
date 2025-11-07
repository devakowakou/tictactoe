"""
Tic Tac Toe Player
Implementation of Minimax algorithm for optimal play
"""

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
    X plays first, then alternates.
    """
    # Count number of X and O on the board
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # If X has played as many or more times than O, it's O's turn
    # Otherwise it's X's turn
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    Returns a set of tuples (i, j) representing empty cells.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    Creates a deep copy of the board and applies the action.
    """
    i, j = action

    # Check that the action is valid
    if board[i][j] != EMPTY:
        raise ValueError(f"Cell ({i}, {j}) already occupied")

    if i not in range(3) or j not in range(3):
        raise ValueError(f"Action ({i}, {j}) out of bounds")

    # Create a deep copy of the board
    new_board = copy.deepcopy(board)

    # Apply the action for the current player
    current_player = player(board)
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Checks rows, columns, and diagonals.
    """
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]

    # Check main diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]

    # Check anti-diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    # No winner
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    The game is over if there is a winner or if the board is full.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if the board is full
    for row in board:
        if EMPTY in row:
            return False

    # The board is full and there is no winner
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    This function should only be called on a terminal board.
    """
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Uses the Minimax algorithm to determine the best move.
    """
    # If the board is terminal, return None
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        # X wants to maximize the score
        _, best_action = max_value(board)
        return best_action
    else:
        # O wants to minimize the score
        _, best_action = min_value(board)
        return best_action


def max_value(board):
    """
    Helper function for Minimax: returns the maximum possible score.
    Returns (value, action)
    """
    # Base case: terminal board
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_action = None

    # Explore all possible actions
    for action in actions(board):
        # Compute the minimum value that the opponent can achieve
        min_val, _ = min_value(result(board, action))

        # Keep the maximum
        if min_val > v:
            v = min_val
            best_action = action

            # Optimization: if a winning move is found, stop searching
            if v == 1:
                break

    return v, best_action


def min_value(board):
    """
    Helper function for Minimax: returns the minimum possible score.
    Returns (value, action)
    """
    # Base case: terminal board
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_action = None

    # Explore all possible actions
    for action in actions(board):
        # Compute the maximum value that the opponent can achieve
        max_val, _ = max_value(result(board, action))

        # Keep the minimum
        if max_val < v:
            v = max_val
            best_action = action

            # Optimization: if a winning move for O is found, stop searching
            if v == -1:
                break

    return v, best_action
