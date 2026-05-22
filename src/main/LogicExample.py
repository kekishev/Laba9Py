import logging

from main.contracts.AsyncHandling import AsyncHandling
from src.main.contracts.Executable import Executable
from src.main.contracts.TaskHandling import TaskHandling
from src.main.tasks.Task import Task

"""
LogicExample contains the example logic of the program
"""


class LogicExample:
    logger = logging.getLogger(__name__)

    @staticmethod
    async def logic(handler: object) -> None:
        if not isinstance(handler, TaskHandling):
            LogicExample.logger.info("LogicExample: TaskHandling not implemented")

        try:
            if not isinstance(handler, AsyncHandling):
                LogicExample.logger.info("LogicExample: AsyncHandler not implemented")
                return

            async with handler as h:
                tasks: list[Task] = await h.get_tasks()
                for task in tasks:
                    await h.print_task(task)

                if isinstance(h, Executable):
                    for task in tasks:
                        await h.execute(task)
        except Exception as e:
            LogicExample.logger.error("Error during task handling: %s", e)
