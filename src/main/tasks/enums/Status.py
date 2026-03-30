from enum import Enum


class Status(Enum):
    FAILED = -1
    READY = 0
    PENDING = 1
    RUNNING = 2
    SUCCEEDED = 3
