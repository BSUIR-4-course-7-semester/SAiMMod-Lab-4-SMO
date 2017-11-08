from Task import Task


class Source:
    def __init__(self, probability, generator):
        self.probability = probability
        self.blocked = False
        self.blocked_task = None
        self.generator = generator

    def tick(self):
        ev = next(self.generator)
        if ev <= self.probability:
            return None
        else:
            return Task()

    def block(self, task):
        self.blocked = True
        self.blocked_task = task

    def unblock(self):
        self.blocked = False
        task = self.blocked_task
        self.blocked_task = None
        return task

    def __str__(self):
        return '1' if self.blocked else '0'
