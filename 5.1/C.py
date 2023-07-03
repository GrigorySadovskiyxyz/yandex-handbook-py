class RedButton:

    def __init__(self, init_val=0):
        self.counter = init_val
 
    def click(self):
        print("Тревога!")
        self.counter += 1
 
    def count(self):
        return self.counter

