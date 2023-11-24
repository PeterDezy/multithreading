from Managers import QueueClient


class Minion:
    def __init__(self):
        self.client = QueueClient()

    def process_tasks(self):
        while True:
            print("Listening...")
            task = self.client.tasks.get()
            print("Received")
            task.work()
            self.client.results.put((task.identifier, task.time))
            print(f"Minion processed task {task.identifier} in {task.time:.4f} seconds")


if __name__ == "__main__":
    minion = Minion()
    minion.process_tasks()
