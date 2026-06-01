import asyncio

from main.Dispatcher import Dispatcher

class Main:
    """Main is the main entry point of the application."""
    @staticmethod
    async def main() -> None:
        dispatcher: Dispatcher = Dispatcher()
        await dispatcher.dispatch()


if __name__ == "__main__":
    asyncio.run(Main.main())
