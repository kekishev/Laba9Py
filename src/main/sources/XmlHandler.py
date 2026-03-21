import logging

from src.main.tasks.Task import Task
from src.main.tasks.TaskGenerator import TaskGenerator


"""
XmlHandler represents the example XML handler, which implements TaskHandling
"""


class XmlHandler:
    logger = logging.getLogger(__name__)

    def get_tasks(self) -> list[Task]:
        self.logger.info("Called get_tasks")
        task_generator: TaskGenerator = TaskGenerator()
        return task_generator.generate()

    def print_task(self, task: Task) -> None:
        self.logger.info("Called print_tasks")
        print("XmlHandler: " + str(task))
