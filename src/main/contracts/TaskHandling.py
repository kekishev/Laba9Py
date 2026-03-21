from typing import Protocol, runtime_checkable

from src.main.tasks.Task import Task


"""
Example interface
"""


@runtime_checkable
class TaskHandling(Protocol):
    def get_tasks(self) -> list[Task]:
        ...

    def print_task(self, task: Task) -> None:
        ...
