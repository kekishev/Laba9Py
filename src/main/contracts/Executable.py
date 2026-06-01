from typing import Protocol, runtime_checkable

from src.main.tasks.Task import Task


@runtime_checkable
class Executable(Protocol):
    """Protocol for handlers that can execute a single Task."""
    async def execute(self, task: Task) -> None:
        ...
