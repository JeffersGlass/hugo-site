class Register():
    def __init__(self, data):
        self._data = data

    def set(self, data):
        self._data = data

    def get(self):
        return self._data