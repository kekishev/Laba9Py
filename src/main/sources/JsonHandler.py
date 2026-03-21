import logging

from src.main.tasks.Task import Task
from src.main.tasks.TaskGenerator import TaskGenerator


"""
JsonHandler represents the example JSON handler, which implements Executable, TaskHandling
"""


class JsonHandler:
    logger = logging.getLogger(__name__)

    def execute(self, task: Task) -> None:
        self.logger.info("Called execute")

        for i in task.payload:
            self.logger.info("Make some important stuff here; i=" + str(i))
            print("JsonHandler: Make some important stuff here; i=" + str(i))

    def get_tasks(self) -> list[Task]:
        self.logger.info("Called get_tasks")
        task_generator: TaskGenerator = TaskGenerator()
        return task_generator.generate()

    def print_task(self, task: Task) -> None:
        self.logger.info("Called print_tasks")
        print("JsonHandler: " + str(task))
