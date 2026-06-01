import logging

from src.main.contracts.AsyncHandling import AsyncHandling
from src.main.contracts.Executable import Executable
from src.main.contracts.TaskHandling import TaskHandling
from src.main.tasks.TaskQueue import TaskQueue

class LogicExample:
    """Demonstrates async task processing using TaskHandling and AsyncHandling protocols."""
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
                queue: TaskQueue = await h.get_tasks()
                async for task in queue:
                    await h.print_task(task)

                if isinstance(h, Executable):
                    async for task in queue:
                        try:
                            await h.execute(task)
                        except Exception as e:
                            LogicExample.logger.error("Error executing task %s: %s", task.id, e)
        except Exception as e:
            LogicExample.logger.error("Error during task handling: %s", e)
