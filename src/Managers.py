import multiprocessing
import os
from multiprocessing.managers import BaseManager

PORT = 50000
KEY = b'abc'


class QueueManager(BaseManager):
    pass


class QueueClient:
    """Base class for users of the Queue."""

    def __init__(self, manager_host="localhost"):
        QueueManager.register("get_tasks")
        QueueManager.register("get_results")

        manager = QueueManager(address=(manager_host, PORT), authkey=KEY)
        manager.connect()

        self.tasks = manager.get_tasks()
        self.results = manager.get_results()


if __name__ == "__main__":
    task_queue = multiprocessing.Queue()
    result_queue = multiprocessing.Queue()

    QueueManager.register("get_tasks", callable=lambda: task_queue)
    QueueManager.register("get_results", callable=lambda: result_queue)

    try:
        manager = QueueManager(address=("", PORT), authkey=KEY)
        server = manager.get_server()
        print(f"QueueManager server started successfully on port {PORT}.")
        server.serve_forever()

    finally:
        print(
            f"Exiting with approximately {task_queue.qsize()} items left in the task queue"
            f" and {result_queue.qsize()} items left in the result queue."
        )
