class Queue():

    def __init__(self):
        self.index = []

    def push(self, item):
        self.index.insert(0, item)

    def is_empty(self):
        return len(self.index) == 0

    def pop(self):
        return self.index.pop(len(self.index) - 1)

