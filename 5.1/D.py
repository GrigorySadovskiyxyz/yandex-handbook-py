class Programmer:
    def __init__(self, name, level, salary=0, totalM=0, totalT=0, counter=0):
        self.name = name
        self.level = level
        self.totalM = totalM
        self.totalT = totalT
        self.counter = 0
        if self.level == "Junior":
            self.salary = 10
        elif self.level == "Middle":
            self.salary = 15
        elif self.level == "Senior":
            self.salary = 20

    def work(self, time=0):
        self.time = time
        self.totalM += (self.salary + self.counter) * self.time
        self.totalT += time

    def rise(self):
        if self.level == "Junior":
            self.level = "Middle"
            self.salary = 15
        elif self.level == "Middle":
            self.level == "Senior"
            self.salary = 20
        elif self.level == "Senior":
            self.salary = self.salary
            self.counter += 1

    def info(self):
        return f"{self.name} {self.totalT}ч. {self.totalM}тгр."

