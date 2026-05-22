from typing import Generator, AsyncGenerator, Callable

from src.main.tasks.IllegalArgumentException import IllegalArgumentException
from src.main.tasks.Task import Task
from src.main.tasks.enums.Priority import Priority
from src.main.tasks.enums.Status import Status

"""
Taskqueue realizes custom queue for Task class
"""


class TaskQueue:
    __slots__ = ["_sources"]

    _sources: list[Task]

    """
    Initialize TaskQueue only if provided argument is a list of tasks or it is None.
    
    @param tasks: list of tasks. The argument can be None.
    """
    def __init__(self, tasks: list[Task] = None):
        if tasks is None:
            self._sources = []
            return

        if not isinstance(tasks, list):
            raise IllegalArgumentException()

        for i in tasks:
            if not isinstance(i, Task):
                raise IllegalArgumentException()

        self._sources = tasks

    def add(self, task: Task) -> None:
        if not isinstance(task, Task):
            raise IllegalArgumentException()
        self._sources.append(task)

    def __iter__(self) -> Generator[Task, None, None]:
        yield from iter(self._sources)

    async def __aiter__(self) -> AsyncGenerator[Task, None]:
        for task in self._sources:
            yield task

    def __len__(self) -> int:
        return len(self._sources)

    def filter_by_status(self, status: Status) -> Generator[Task, None, None]:
        return (task for task in self if task.status == status)

    def filter_by_priority(self, priority: Priority) -> Generator[Task, None, None]:
        return (task for task in self if task.priority == priority)

    def filter(self, predicate: Callable[[Task], bool]) -> Generator[Task, None, None]:
        return (task for task in self if predicate(task))