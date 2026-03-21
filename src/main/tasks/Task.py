import dataclasses
import uuid
from io import UnsupportedOperation


@dataclasses.dataclass
class Task:
    __slots__ = ["__id", "__payload"]

    __id: uuid.UUID
    __payload: list[object]

    def __init__(self, payload: list[object]):
        self.__id = uuid.uuid4()
        self.__payload = payload

    def __str__(self):
        return "Task with id=" + str(self.__id)

    @property
    def id(self) -> uuid.UUID:
        return self.__id

    @property
    def payload(self) -> list[object]:
        return self.__payload

    @id.getter
    def id(self) -> uuid.UUID:
        return self.__id

    @id.setter
    def id(self, *args, **kwargs):
        raise UnsupportedOperation("Setting id is unsupported")

    @payload.getter
    def payload(self) -> list[object]:
        return self.__payload

    @payload.setter
    def payload(self, payload: list[object]):
        self.__payload = payload
