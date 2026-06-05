from src.main.contracts.TaskHandling import TaskHandling
from src.main.sources.JsonHandler import JsonHandler
from src.main.sources.XmlHandler import XmlHandler
from src.main.tasks.Task import Task
from src.main.tasks.TaskQueue import TaskQueue
from src.main.tasks.enums.Priority import Priority
from src.main.tasks.enums.Status import Status


def _task() -> Task:
    return Task("test", Priority.MEDIUM, Status.READY, [])


def test_xml_handler_true():
    assert isinstance(XmlHandler(), TaskHandling)


def test_xml_handler_false():
    assert not isinstance(XmlHandler(), JsonHandler)


async def test_get_tasks_returns_list_of_tasks():
    handler = XmlHandler()
    tasks = await handler.get_tasks()

    assert isinstance(tasks, TaskQueue)
    assert len(tasks) > 0
    assert all(isinstance(t, Task) for t in tasks)


async def test_print_task_outputs_text(capsys):
    handler = XmlHandler()
    task = _task()
    await handler.print_task(task)

    captured = capsys.readouterr()
    assert "XmlHandler" in captured.out
    assert str(task) in captured.out


async def test_context_manager_returns_handler_instance():
    async with XmlHandler() as h:
        assert isinstance(h, XmlHandler)


async def test_context_manager_get_tasks_inside_block():
    async with XmlHandler() as h:
        tasks = await h.get_tasks()
        assert isinstance(tasks, TaskQueue)
        assert len(tasks) > 0
