import logging

from src.main.contracts.Executable import Executable
from src.main.contracts.TaskHandling import TaskHandling
from src.main.tasks.Task import Task

"""
LogicExample contains the example logic of the program
"""


class LogicExample:
    logger = logging.getLogger(__name__)

    @staticmethod
    def logic(handler: object) -> None:
        if not isinstance(handler, TaskHandling):
            LogicExample.logger.error("LogicExample: TaskHandling not implemented")

        tasks: list[Task] = handler.get_tasks()
        for task in tasks:
            handler.print_task(task)

        if isinstance(handler, Executable):
            for task in tasks:
                handler.execute(task)
