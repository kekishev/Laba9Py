import logging.config

from src.main.LogicExample import LogicExample
from src.main.config import LOGGING_CONFIG
from src.main.sources.JsonHandler import JsonHandler
from src.main.sources.XmlHandler import XmlHandler


class Dispatcher:
    """
    Centralized async entry point that orchestrates all handlers and catches top-level exceptions.

    Extend by adding new _execute_* methods and calling them from dispatch().
    """
    async def _execute_logic_example(self) -> None:
        await LogicExample.logic(XmlHandler())
        await LogicExample.logic(JsonHandler())

    async def dispatch(self) -> None:
        logging.config.dictConfig(LOGGING_CONFIG)

        try:
            await self._execute_logic_example()
        except Exception as e:
            logging.error(e)
