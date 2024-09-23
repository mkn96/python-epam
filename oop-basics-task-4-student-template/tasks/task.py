class HistoryDict:
    def __init__(self, initial_dict):
        self.data = initial_dict
        self.history = []

    def set_value(self, key, value):
        self.data[key] = value
        if key in self.history:
            self.history.remove(key)
        self.history.append(key)
        if len(self.history) > 5:
            self.history.pop(0)

    def get_history(self):
        return self.history
