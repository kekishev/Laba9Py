from typing import Protocol, runtime_checkable

from src.main.tasks.Task import Task


"""
Example interface
"""


@runtime_checkable
class Executable(Protocol):
    async def execute(self, task: Task) -> None:
        ...
