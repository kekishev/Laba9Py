import logging
from types import TracebackType

from src.main.tasks.Task import Task
from src.main.tasks.TaskGenerator import TaskGenerator


"""
XmlHandler represents the example XML handler, which implements TaskHandling
"""


class XmlHandler:
    _logger = logging.getLogger(__name__)

    async def get_tasks(self) -> list[Task]:
        self._logger.info("Called get_tasks")
        task_generator: TaskGenerator = TaskGenerator()
        return task_generator.generate()

    async def print_task(self, task: Task) -> None:
        self._logger.info("Called print_tasks")
        print("XmlHandler: " + str(task))

    async def __aenter__(self) -> "XmlHandler":
        self._logger.info("%s: opening XML resource (e.g. file/connection)", type(self).__name__)
        return self

    async def __aexit__(
            self,
            exc_type: type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None,
    ) -> None:
        self._logger.info("%s: closing XML resource", type(self).__name__)