from Managers import QueueClient
from Task import Task


class Boss:
    def __init__(self):
        self.queue = QueueClient()

    def createTask(self, task):
        self.queue.tasks.put(task)

    def lookForAResult(self):
        queue = self.queue.getResult()
        result = queue.get()
        print(result)


if __name__ == "__main__":
    b = Boss()
    t = Task("000", 100)
    for i in range(10):
        b.createTask(t)
    while 1:
        b.lookForAResult()
