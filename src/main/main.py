from LogicExample import LogicExample
from src.main.sources.JsonHandler import JsonHandler
from src.main.sources.XmlHandler import XmlHandler

"""
class Main is the main entrypoint of the program.
"""


class Main:
    @staticmethod
    def main() -> None:
        LogicExample.logic(XmlHandler())
        LogicExample.logic(JsonHandler())


if __name__ == "__main__":
    Main.main()
