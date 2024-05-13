import random


class RandomAgent:
    def __init__(self, mark):
        self.mark = mark

    def act(self, ava_actions, state):
        return random.choice(ava_actions)
