from os import urandom
from base64 import b32encode


class Noob(object):
    def __init__(self):
        self.val = 0

    def increment(self):
        self.val += 1


class Blob(object):
    def __init__(self):
        self.id = b32encode(urandom(32)).decode()
        self.hash = 0

    def set_data(self, data):
        data = bytes(data)
        self.hash = hash(data)
        with open(self.id, 'wb+') as file:
            file.write(data)

    def get_data(self):
        with open(self.id, 'rb') as file:
            return file.read()

    def __hash__(self):
        return self.hash
