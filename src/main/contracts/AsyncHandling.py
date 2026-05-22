from typing import runtime_checkable, Protocol


@runtime_checkable
class AsyncHandling(Protocol):
    """Acquire handler resources (connections, file handles, etc.)."""
    async def __aenter__(self) -> AsyncHandling:
        ...

    """Release handler resources."""
    async def __aexit__(
            self,
            exc_type: type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: object,
    ) -> None:
        ...
