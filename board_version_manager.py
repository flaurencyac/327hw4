class Board_Version_Manager:
    def __init__(self):
        self._history = []

    def append_state(self, state):
        self._history.append(state)

    def update_history(self):
        pass

    def undo(self):
        pass

    def re_do(self):
        pass

    def next(self):
        pass

