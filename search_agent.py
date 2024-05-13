from typing import List
from xxo_environment import check_game_status, tocode


class SearchAgent:
    def __init__(self, mark):
        # Initialisiert den Agenten mit einem gegebenen Mark 'X' oder 'O'
        self.mark = mark

    def act(self, ava_actions, board_state):
        raise NotImplementedError
