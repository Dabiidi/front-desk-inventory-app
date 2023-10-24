# box.py

class Box:
    def __init__(self, size):
        self.size = size
        self.is_stored = False

    def store(self):
        self.is_stored = True

    def retrieve(self):
        self.is_stored = False
