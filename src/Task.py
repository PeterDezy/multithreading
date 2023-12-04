import json
import time

import numpy as np


class Task:

    def __init__(self, identifier, size):
        self.identifier = identifier
        self.size = size
        self.a = np.random.rand(size, size)
        self.b = np.random.rand(size)
        self.time = 0
        self.x = np.zeros(size)

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def to_json(self) -> str:
        data = {
            "identifier": self.identifier,
            "size": self.size,
            "a": self.a.tolist(),
            "b": self.b.tolist(),
            "x": self.x.tolist(),
            "time": self.time,
        }
        return json.dumps(data)

    @classmethod
    def from_json(cls, text: str) -> "Task":
        data = json.loads(text)

        task = cls(identifier=data["identifier"], size=data["size"])
        task.a = np.array(data["a"])
        task.b = np.array(data["b"])
        task.x = np.array(data["x"])
        task.time = data["time"]

        return task

    def __eq__(self, other: "Task") -> bool:
        if not isinstance(other, Task):
            return False

        if not (self.identifier == other.identifier
                and self.size == other.size
                and self.time == other.time):
            return False

        return (np.array_equal(self.a, other.a)
                and np.array_equal(self.b, other.b)
                and np.array_equal(self.x, other.x))


if __name__ == '__main__':
    a = Task(1, 100)
    txt = a.to_json()
    b = Task.from_json(txt)
    print(a == b)
