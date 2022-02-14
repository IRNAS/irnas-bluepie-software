from logging import Logger, Formatter
from rich.logging import RichHandler


class Logs(Logger):
    def __init__(self, enable: bool = False):

        """
        Initialises standard logging module with RichHandler for richer and
        prettier logging.

        Args:
            enabled (bool): whether the logging module will be enabled.
        """
        super().__init__("rich")
        super().setLevel("INFO")
        super().addHandler(RichHandler(rich_tracebacks=True))

        # This controls whether the logs will be enabled or not
        self.propagate = enable
