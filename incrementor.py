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
        self.data = b''

    def set_data(self, data):
        self.data = bytes(data)
        self.hash = hash(data)

    def get_data(self):
        return self.data

    def __hash__(self):
        return self.hash
