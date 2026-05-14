from typing import Generator, Callable

from src.main.tasks.IllegalArgumentException import IllegalArgumentException
from src.main.tasks.Task import Task
from src.main.tasks.enums.Priority import Priority
from src.main.tasks.enums.Status import Status

"""
Taskqueue realizes custom queue for Task class
"""


class TaskQueue:
    __slots__ = ["_tasks", "_index"]

    _tasks: list[Task]
    _index: int

    """
    Initialize TaskQueue only if provided argument is a list of tasks or it is None.
    
    @param tasks: list of tasks. The argument can be None.
    """
    def __init__(self, tasks: list[Task] = None):
        if tasks is None:
            self._tasks: list[Task] = []
            self._index = 0
            return

        if not isinstance(tasks, list):
            print(type(tasks))
            raise IllegalArgumentException()

        for i in tasks:
            if not isinstance(i, Task):
                raise IllegalArgumentException()

        self._tasks: list[Task] = tasks
        self._index: int = 0

    def add(self, task: Task) -> None:
        if not isinstance(task, Task):
            raise IllegalArgumentException()
        self._tasks.append(task)

    def __iter__(self) -> TaskQueue:
        self._index = 0
        return self

    def __next__(self) -> Task:
        if self._index >= len(self._tasks):
            raise StopIteration
        task = self._tasks[self._index]
        self._index += 1

        return task

    def __len__(self) -> int:
        return len(self._tasks)

    def filter_by_status(self, status: Status) -> Generator[Task, None, None]:
        return (task for task in self._tasks if task.status == status)

    def filter_by_priority(self, priority: Priority) -> Generator[Task, None, None]:
        return (task for task in self._tasks if task.priority == priority)

    def filter(self, predicate: Callable[[Task], bool]) -> Generator[Task, None, None]:
        return (task for task in self._tasks if predicate(task))