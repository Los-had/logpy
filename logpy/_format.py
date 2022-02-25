from typing import Optional


class LogParser:
    def __init__(self, log_format: Optional[str] = "") -> None:
        if log_format == "":
            self.log_format = "[{LEVEL}] {DATE} - {MSG}"
        else:
            self.log_format = log_format

    def _make_log(self, level: str, msg: str, date: str) -> str:
        """Make the log structure

        Args:
            level (str): log level
            msg (str): message
            date (str): date

        Returns:
            str: the log format
        """
        self.log_format = self.log_format.replace("{LEVEL}", level)
        self.log_format = self.log_format.replace("{DATE}", date)
        self.log_format = self.log_format.replace("{MSG}", msg)
        self.log_format += "\n"

        return self.log_format

    def __call__(self, level, msg, date) -> str:
        return self._make_log(level, msg, date)
