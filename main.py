# based on https://github.com/haje01/gym-tictactoe
import sys

from human_agent import HumanAgent
from random_agent import RandomAgent
from xxo_environment import TicTacToeEnv, agent_by_mark


def play(show_number=None):
    env = TicTacToeEnv(show_number=show_number)
    agents = [RandomAgent('O'),
              HumanAgent('X')]
    episode = 0
    while True:
        state = env.reset()
        _, mark = state
        done = False
        env.render()
        while not done:
            agent = agent_by_mark(agents, mark)
            env.show_turn(True, mark)
            ava_actions = env.available_actions()
            action = agent.act(ava_actions, state)
            if action is None:
                sys.exit()

            state, reward, done, info = env.step(action)

            print('')
            env.render()
            if done:
                env.show_result(True, mark, reward)
                break
            else:
                _, mark = state
        episode += 1


if __name__ == '__main__':
    play()
