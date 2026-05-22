import asyncio
import logging.config

from src.main.LogicExample import LogicExample
from src.main.config import LOGGING_CONFIG
from src.main.sources.JsonHandler import JsonHandler
from src.main.sources.XmlHandler import XmlHandler

"""
class Main is the main entrypoint of the program.
"""


class Main:
    @staticmethod
    async def main() -> None:
        logging.config.dictConfig(LOGGING_CONFIG)
        await LogicExample.logic(XmlHandler())
        await LogicExample.logic(JsonHandler())


if __name__ == "__main__":
    asyncio.run(Main.main())
