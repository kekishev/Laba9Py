import dataclasses
import uuid
from datetime import datetime
from io import UnsupportedOperation

from src.main.tasks.enums.Priority import Priority
from src.main.tasks.enums.Status import Status
from src.main.tasks.IllegalArgumentException import IllegalArgumentException


@dataclasses.dataclass
class Task:
    __slots__ = ["_id", "_description", "_priority", "_status", "_creation_time", "_payload"]

    _id: uuid.UUID
    _description: str
    _priority: Priority
    _status: Status
    _creation_time: datetime
    _payload: list[object]

    def __init__(self,
            description: str,
            priority: Priority,
            status: Status,
            payload: list[object]
    ):
        self._id = uuid.uuid4()
        self._description = description
        self._priority = priority
        self._status = status
        self._creation_time = datetime.now()
        self._payload = payload

    def __str__(self):
        return ("Task: id={0}; description={1}; priority={2}; status={3}; creation_time={4}".
                format(str(self._id), self._description, self._priority, self._status, self._creation_time))

    @property
    def is_ready_for_execution(self) -> bool:
        if self._status == Status.READY:
            return True
        else:
            return False

    @property
    def id(self) -> uuid.UUID:
        return self._id

    @property
    def description(self) -> str:
        return self._description

    @property
    def priority(self) -> Priority:
        return self._priority

    @property
    def status(self) -> Status:
        return self._status

    @property
    def creation_time(self) -> datetime:
        return self._creation_time

    @property
    def payload(self) -> list[object]:
        return self._payload

    @id.getter
    def id(self) -> uuid.UUID:
        return self._id

    @id.setter
    def id(self, *args, **kwargs):
        raise UnsupportedOperation("Setting creation_time is restricted")

    @description.getter
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, description: str) -> None:
        if not isinstance(description, str):
            raise IllegalArgumentException()
        self._description = description

    @priority.getter
    def priority(self) -> Priority:
        return self._priority

    @priority.setter
    def priority(self, priority: Priority) -> None:
        if not isinstance(priority, Priority):
            raise IllegalArgumentException()
        self._priority = priority

    @status.getter
    def status(self) -> Status:
        return self._status

    @status.setter
    def status(self, status: Status) -> None:
        if not isinstance(status, Status):
            raise IllegalArgumentException()
        self._status = status

    @creation_time.getter
    def creation_time(self) -> datetime:
        return self._creation_time

    @creation_time.setter
    def creation_time(self, *args, **kwargs) -> None:
        raise UnsupportedOperation("Setting creation_time is restricted")

    @payload.getter
    def payload(self) -> list[object]:
        return self._payload

    @payload.setter
    def payload(self, payload: list[object]):
        if not isinstance(payload, list):
            raise IllegalArgumentException()
        self._payload = payload


if __name__ == "__main__":
    t = Task("aaa", Priority.BLOCKING, Status.READY, list())
    print(t.is_ready_for_execution)
    t.status = Status.SUCCEEDED
    print(t.is_ready_for_execution)