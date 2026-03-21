from src.main.tasks.TaskGenerator import TaskGenerator


def test_task_generator_true():
    assert len(TaskGenerator.generate()) >= 20
    assert len(TaskGenerator.generate()) <= 50


def test_task_generator_false():
    assert not len(TaskGenerator.generate()) < 20
    assert not len(TaskGenerator.generate()) > 50
