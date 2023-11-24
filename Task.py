import time

import numpy as np


class Task:

    def __init__(self, identifier, size):
        self.identifier = identifier
        self.size = size
        self.a = np.random.rand(size, size)
        self.b = np.random.rand(size)
        self.time = 0
        # Initialiser x comme un vecteur nul
        self.x = np.zeros(size)

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start
        print("Running time: ", self.time)


if __name__ == '__main__':
    Task_one = Task(1, 6000)
    Task_one.work()
