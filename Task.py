from time import perf_counter

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
        print("ID_Task=", self.identifier)
        start = perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        end = perf_counter()
        self.time = end - start
        print("Running time: ", self.time)


if __name__ == "main":
    Task_one = Task(1, 6000)
    Task_one.work()
