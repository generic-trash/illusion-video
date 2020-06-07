class Noob(object):
    def __init__(self):
        self.val = 0

    def increment(self):
        self.val += 1


class Blob(object):
    def __init__(self):
        self.data = b''

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data
