from src.main.sources.XmlHandler import XmlHandler
from src.main.contracts.TaskHandling import TaskHandling
from src.main.sources.JsonHandler import JsonHandler


def test_json_handler_true():
    json_handler = JsonHandler()
    assert isinstance(json_handler, TaskHandling)


def test_json_handler_false():
    json_handler = JsonHandler()
    assert not isinstance(json_handler, XmlHandler)
