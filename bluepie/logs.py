from logging import Logger, Formatter
from rich.logging import RichHandler


class Logs(Logger):
    def __init__(self, level: str = "INFO", enable: bool = False):

        """
        Initialises standard logging module with RichHandler for richer and
        prettier logging.

        Args:
            enabled (bool): whether the logging module will be enabled.
            level (bool): logging level, possible options are:
                - "CRITICAL"
                - "ERROR"
                - "WARNING"
                - "INFO"
                - "DEBUG"
                more about logging levels in on this link:
                https://docs.python.org/3/howto/logging.html#logging-levels
        """
        super().__init__("rich")
        super().setLevel(level)
        super().addHandler(RichHandler(rich_tracebacks=True))

        # This controls whether the logs will be enabled or not
        self.propagate = enable
