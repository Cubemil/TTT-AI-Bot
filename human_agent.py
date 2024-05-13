# based on https://github.com/haje01/gym-tictactoe

class HumanAgent:
    def __init__(self, mark):
        self.mark = mark

    def act(self, ava_actions, state):
        while True:
            uloc = input("Enter location [1-9] or q to quit: ")
            if uloc.lower() == 'q':
                return None
            try:
                action = int(uloc) - 1
                if action not in ava_actions:
                    raise ValueError()
            except ValueError:
                print("Illegal location: '{}'".format(uloc))
            else:
                break

        return action
