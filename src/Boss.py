import time
from Task import Task
from Managers import QueueClient


class Boss:
    def __init__(self):
        self.client = QueueClient()

    def add_task(self, identifier, size=None):
        task = Task(identifier, size)

        self.client.tasks.put(task)

        print(f"Boss added task {identifier} to the queue.")


if __name__ == "__main__":
    boss = Boss()

    while True:
        try:
            task_count = int(input("Enter the number of tasks to add (0 to quit): "))

            if task_count == 0:
                break

            for i in range(task_count):
                boss.add_task(i, 4000)

        except ValueError:
            print("Please enter a valid number.")

