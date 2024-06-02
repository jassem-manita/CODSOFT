# app.py

import streamlit as st
import numpy as np
from src.game import TicTacToe

def main():
    st.title("Tic-Tac-Toe with AI")
    
    game = TicTacToe()
    
    if 'board' not in st.session_state:
        st.session_state.board = game.board
    if 'current_winner' not in st.session_state:
        st.session_state.current_winner = None
    if 'player_turn' not in st.session_state:
        st.session_state.player_turn = 1  # 'X' starts

    def reset_game():
        st.session_state.board = np.zeros((3, 3), dtype=int)
        st.session_state.current_winner = None
        st.session_state.player_turn = 1

    st.button("Reset Game", on_click=reset_game)

    for row in range(3):
        cols = st.columns(3)
        for col in range(3):
            if st.session_state.board[row, col] == 1:
                cols[col].button("X", key=f"{row}-{col}", disabled=True)
            elif st.session_state.board[row, col] == -1:
                cols[col].button("O", key=f"{row}-{col}", disabled=True)
            else:
                if cols[col].button("", key=f"{row}-{col}"):
                    st.session_state.board[row, col] = st.session_state.player_turn
                    if game.winner((row, col), st.session_state.player_turn):
                        st.session_state.current_winner = st.session_state.player_turn
                    st.session_state.player_turn *= -1  # Switch turns
                    if st.session_state.player_turn == -1:  # AI turn
                        ai_move = game.get_ai_move()
                        if ai_move:
                            st.session_state.board[ai_move] = -1
                            if game.winner(ai_move, -1):
                                st.session_state.current_winner = -1
                        st.session_state.player_turn = 1  # Back to human turn

    if st.session_state.current_winner is not None:
        st.write(f"Player {'X' if st.session_state.current_winner == 1 else 'O'} wins!")
    elif not game.empty_squares():
        st.write("It's a tie!")

if __name__ == "__main__":
    main()
