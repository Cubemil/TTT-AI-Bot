from xxo_environment import check_game_status, tocode, after_action_state


def select_and_remove_state(todo_list):
    """
    Args:
        todo_list: list of states and paths to check
    Returns:
        removes and returns first list element

    """
    return todo_list.pop(0)


def expand_state(state, path):
    """
    Args:
        state: board state
        path: list of actions to reach this state
    Returns:
        List of all child nodes in custom order as list
    """
    expanded_states = []
    board, current_mark = state
    # Find empty positions on the board
    actions = [i for i, c in enumerate(board) if c == 0]

    # Look at possible actions
    for action in actions:
        # Apply each action to generate a new state
        new_state = after_action_state((board, current_mark), action)
        # Append new state and updated path (including current actions)
        expanded_states.append((new_state, path + [action]))

    return expanded_states


class SearchAgent:
    def __init__(self, mark):
        self.mark = mark

    def act(self, ava_actions, state):
        """
        Args:
            ava_actions: Available actions
            state: Current board state (tuple of board and mark)
        Returns:
            The first action in the solution path or None if no solution
        """
        # Initialise the first state to a list with the path
        todo_list = [(state, [])]
        visited = set()

        while todo_list:
            current_state, path = select_and_remove_state(todo_list)

            if self.is_solution(current_state[0]):
                # Return the path leading to this state (solution)
                return path[0] if path else None
            else:
                if current_state not in visited:
                    visited.add(current_state)
                    # Expand current state -> generate all possible next states
                    # and also the path to reach each state -> add to todo_list
                    expanded_states = expand_state(current_state, path)
                    todo_list.extend(expanded_states)

        return None

    def is_solution(self, board) -> bool:
        """
        Args:
            board: board state
        Returns:
            whether the board is a winning state for the agent's mark
        """
        return check_game_status(board) == tocode(self.mark)
