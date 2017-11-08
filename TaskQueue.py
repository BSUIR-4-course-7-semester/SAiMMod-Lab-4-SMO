class TaskQueue:
    def __init__(self, size):
        self.size = size
        self.tasks = []
        self.sum_of_sizes = 0

    def tick(self):
        self.sum_of_sizes += len(self.tasks)

    def enqueue(self, task):
        if len(self.tasks) == self.size:
            raise Exception('Queue is full')
        else:
            self.tasks.append(task)

    def dequeue(self):
        task = self.tasks[-1]
        self.tasks = self.tasks[0:-1]
        return task

    def has_place(self):
        return len(self.tasks) < self.size

    def __len__(self):
        return len(self.tasks)

    def __str__(self):
        # return '0' * self.size - len(self.tasks) + '1' * len(self.tasks)
        return str(len(self))