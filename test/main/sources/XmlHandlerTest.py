from src.main.contracts.TaskHandling import TaskHandling
from src.main.sources.JsonHandler import JsonHandler
from src.main.sources.XmlHandler import XmlHandler


def test_xml_handler_true():
    xml_handler = XmlHandler()
    assert isinstance(xml_handler, TaskHandling)


def test_xml_handler_false():
    xml_handler = XmlHandler()
    assert not isinstance(xml_handler, JsonHandler)
