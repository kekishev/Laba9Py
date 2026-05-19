import types
from typing import Callable

import pytest

from src.main.tasks.IllegalArgumentException import IllegalArgumentException
from src.main.tasks.Task import Task
from src.main.tasks.TaskGenerator import TaskGenerator
from src.main.tasks.TaskQueue import TaskQueue
from src.main.tasks.enums.Priority import Priority
from src.main.tasks.enums.Status import Status


def _task(description = "test", priority: Priority = Priority.MEDIUM, status: Status = Status.READY) -> Task:
    return Task(description, priority, status, [])


def test_iter_returns_generator():
    queue = TaskQueue([_task()])

    assert isinstance(iter(queue), types.GeneratorType)


def test_next_yields_tasks_in_order():
    tasks = [_task(status=Status.READY), _task(status=Status.RUNNING)]
    queue = TaskQueue(tasks)
    it = iter(queue)

    assert next(it) is tasks[0]
    assert next(it) is tasks[1]


def test_stop_iteration_on_empty_queue():
    queue = TaskQueue()

    with pytest.raises(StopIteration):
        next(iter(queue))


def test_stop_iteration_after_exhaustion():
    queue = TaskQueue([_task()])
    it = iter(queue)
    next(it)

    with pytest.raises(StopIteration):
        next(it)


def test_for_loop():
    tasks = [_task(), _task()]
    queue = TaskQueue(tasks)
    seen = [t for t in queue]

    assert seen == tasks


def test_list_constructor():
    tasks = [_task(), _task()]
    queue = TaskQueue(tasks)

    assert list(queue) == tasks


def test_filter_by_status_returns_generator():
    queue = TaskQueue([_task()])

    assert isinstance(queue.filter_by_status(Status.READY), types.GeneratorType)


def test_filter_by_priority_returns_generator():
    queue = TaskQueue([_task()])

    assert isinstance(queue.filter_by_priority(Priority.MEDIUM), types.GeneratorType)

def test_filter_returns_generator():
    description: str = "some description"

    queue = TaskQueue([_task(description=description)])
    predicate: Callable[[Task], bool] = lambda t: t.description == description

    assert isinstance(queue.filter(predicate), types.GeneratorType)


def test_filter_by_status_correct_results():
    tasks = [
        _task(status=Status.READY),
        _task(status=Status.RUNNING),
        _task(status=Status.READY),
    ]

    queue = TaskQueue(tasks)
    result = list(queue.filter_by_status(Status.READY))

    assert len(result) == 2
    assert all(t.status == Status.READY for t in result)


def test_custom_filter():
    tasks = [
        _task(priority=Priority.CRITICAL, status=Status.READY),
        _task(priority=Priority.LOW, status=Status.READY),
        _task(priority=Priority.CRITICAL, status=Status.FAILED),
    ]

    queue = TaskQueue(tasks)
    result = list(queue.filter(
        lambda t: t.priority == Priority.CRITICAL and t.status == Status.READY
    ))

    assert len(result) == 1
    assert result[0].priority == Priority.CRITICAL
    assert result[0].status == Status.READY


def test_filter_by_priority_correct_results():
    tasks = [
        _task(priority=Priority.HIGH),
        _task(priority=Priority.LOW),
        _task(priority=Priority.HIGH),
    ]

    queue = TaskQueue(tasks)
    result = list(queue.filter_by_priority(Priority.HIGH))

    assert len(result) == 2
    assert all(t.priority == Priority.HIGH for t in result)


def test_filter_correct_results():
    description: str = "some description"

    queue = TaskQueue([_task(description=description)])
    predicate: Callable[[Task], bool] = lambda t: t.description == description
    result = list(queue.filter(predicate))

    assert len(result) == 1
    assert list(result)[0]._description == description


def test_add_task():
    queue = TaskQueue()
    task = _task()
    queue.add(task)

    assert len(queue) == 1
    assert list(queue)[0] is task


def test_add_invalid_raises():
    queue = TaskQueue()

    with pytest.raises(IllegalArgumentException):
        queue.add("not a task")


def test_len():
    queue = TaskQueue([_task(), _task(), _task()])

    assert len(queue) == 3


def test_large_volume_filter():
    tasks = TaskGenerator.generate()
    queue = TaskQueue(tasks)
    expected = [t for t in tasks if t.status == Status.READY]

    assert list(queue.filter_by_status(Status.READY)) == expected

