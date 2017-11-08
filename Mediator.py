from collections import Counter

from Handler import Handler
from Lemer import LemerGenerator
from TaskQueue import TaskQueue
from Source import Source


class Mediator:
    def __init__(self, p = 0.75, p1 = 0.8, p2 = 0.5, iteration_count = 100000):
        self.current_tick = 0
        self.handled_tasks = []
        self.states = []
        self.iteration_count = iteration_count
        self.busy_count = 0

        self.source = Source(p, LemerGenerator(209715120, 3, 7))
        self.queue = TaskQueue(2)
        self.handlers = [Handler(p1, LemerGenerator(209715120, 3, 7)), Handler(p2, LemerGenerator(209715120, 3, 7))]

    def run(self):
        for i in range(self.iteration_count):
            self.tick()

        state_count = len(self.states)
        counter = Counter(self.states)

        for key in counter.keys():
            counter[key] = counter[key] / state_count
            print('P {0} = {1}'.format(key, counter[key]))

        print('Loch = {0}'.format(self.queue.sum_of_sizes / len(self.states)))
        print('A = {0}'.format(len(self.handled_tasks) / len(self.states)))
        print('Kkan = {0}'.format(self.busy_count / len(self.states)))

    def tick(self):
        self.current_tick += 1

        for handler in self.handlers:
            handler_result = handler.tick()
            if handler_result is not None:
                self.handled_tasks.append(handler_result)

        for handler in self.handlers:
            if len(self.queue) == 0:
                break
            if not handler.is_busy():
                task = self.queue.dequeue()
                handler.set_task(task)

        if not self.source.blocked:
            source_result = self.source.tick()
            if source_result is not None:
                if self.queue.has_place():
                    self.queue.enqueue(source_result)
                else:
                    self.source.block(source_result)
        else:
            if self.queue.has_place():
                task = self.source.unblock()
                self.queue.enqueue(task)

        for handler in self.handlers:
            if len(self.queue) == 0:
                break
            if not handler.is_busy():
                task = self.queue.dequeue()
                handler.set_task(task)

        self.queue.tick()

        if self.handlers[0].is_busy():
            self.busy_count += 1
        elif self.handlers[1].is_busy():
            self.busy_count += 1

        state = '{0}{1}{2}'.format(
            str(self.source),
            str(self.queue),
            ''.join(map(lambda h: str(h), self.handlers))
        )

        self.states.append(state)

        # print(state)
