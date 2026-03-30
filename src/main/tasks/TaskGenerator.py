import random

from src.main.tasks.enums.Priority import Priority
from src.main.tasks.enums.Status import Status
from src.main.tasks.Task import Task


"""
TaskGenerator generates Task for example logic
"""


class TaskGenerator:
    @staticmethod
    def generate() -> list[Task]:
        quantity_of_generating_tasks: int = random.randint(20, 50)
        list_of_tasks: list[Task] = list()
        for i in range(quantity_of_generating_tasks):
            payload: list[object] = list()

            if i % 2 == 0:
                payload.append(i // 2)
            else:
                payload.append("Does Samir approve this?")

            if i % 3 == 0:
                payload.append("I dont know...")
                payload.append(i * random.randint(10, 100))

            if i % 5 == 0:
                payload.append("I will hope this is at least 3.")
                payload.append(i * random.randint(50, 500))

            if i % 11 == 0:
                payload.append("This laboratory work is interesting. I'm starting to accept Python like it is.")
                payload.append("The way to handle fields in a class with __slots__ and @property make encapsulation possible in Python.")
                payload.append(i)

            list_of_tasks.append(Task(str(i), Priority(random.randint(0, 4)),
                                      Status(random.randint(-1, 3)), payload))

        return list_of_tasks
