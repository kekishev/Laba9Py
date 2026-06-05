from src.main.contracts.TaskHandling import TaskHandling
from src.main.sources.JsonHandler import JsonHandler
from src.main.sources.XmlHandler import XmlHandler
from src.main.tasks.Task import Task
from src.main.tasks.TaskQueue import TaskQueue
from src.main.tasks.enums.Priority import Priority
from src.main.tasks.enums.Status import Status


def _task() -> Task:
    return Task("test", Priority.MEDIUM, Status.READY, [1, 2, 3])


def test_json_handler_true():
    assert isinstance(JsonHandler(), TaskHandling)


def test_json_handler_false():
    assert not isinstance(JsonHandler(), XmlHandler)


async def test_get_tasks_returns_list_of_tasks():
    handler = JsonHandler()
    tasks = await handler.get_tasks()

    assert isinstance(tasks, TaskQueue)
    assert len(tasks) > 0
    assert all(isinstance(t, Task) for t in tasks)


async def test_print_task_outputs_text(capsys):
    handler = JsonHandler()
    task = _task()
    await handler.print_task(task)

    captured = capsys.readouterr()
    assert "JsonHandler" in captured.out
    assert str(task) in captured.out


async def test_execute_processes_payload(capsys):
    handler = JsonHandler()
    task = _task()
    await handler.execute(task)

    captured = capsys.readouterr()
    assert "JsonHandler" in captured.out


async def test_context_manager_returns_handler_instance():
    async with JsonHandler() as h:
        assert isinstance(h, JsonHandler)


async def test_context_manager_get_tasks_inside_block():
    async with JsonHandler() as h:
        tasks = await h.get_tasks()
        assert isinstance(tasks, TaskQueue)
        assert len(tasks) > 0
