import numpy as np
from src.game import TicTacToe

def minimax(state, depth, alpha, beta, player):
    max_player = 1  # We are maximizing for 'X'
    other_player = -1  # We are minimizing for 'O'

    if state.current_winner == other_player:
        return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}

    elif not state.empty_squares():
        return {'position': None, 'score': 0}

    if player == max_player:
        best = {'position': None, 'score': -np.inf}
    else:
        best = {'position': None, 'score': np.inf}

    for possible_move in state.available_moves():
        state.make_move(possible_move, player)
        sim_score = minimax(state, depth + 1, alpha, beta, other_player)

        state.board[possible_move] = 0
        state.current_winner = None
        sim_score['position'] = possible_move

        if player == max_player:
            if sim_score['score'] > best['score']:
                best = sim_score
            alpha = max(alpha, sim_score['score'])
        else:
            if sim_score['score'] < best['score']:
                best = sim_score
            beta = min(beta, sim_score['score'])

        if beta <= alpha:
            break

    return best

def get_ai_move(game):
    if len(game.available_moves()) > 0:
        return minimax(game, 0, -np.inf, np.inf, 1)['position']
    return None
