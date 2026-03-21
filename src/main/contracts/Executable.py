from typing import Protocol, runtime_checkable

from src.main.tasks.Task import Task


"""
Example interface
"""


@runtime_checkable
class Executable(Protocol):
    def execute(self, task: Task) -> None:
        ...
