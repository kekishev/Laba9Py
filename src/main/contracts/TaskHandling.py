from typing import Protocol, runtime_checkable

from src.main.tasks.Task import Task
from src.main.tasks.TaskQueue import TaskQueue


@runtime_checkable
class TaskHandling(Protocol):
    """Protocol for handlers that retrieve and display tasks."""
    async def get_tasks(self) -> TaskQueue:
        ...

    async def print_task(self, task: Task) -> None:
        ...
