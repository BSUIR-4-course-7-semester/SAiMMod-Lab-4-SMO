class Task:
    def __init__(self):
        self.ticks = 0
        self.ticks_in_queue = 0

    def inc_tick(self):
        self.ticks += 1

    def inc_tick_in_queue(self):
        self.ticks_in_queue += 1