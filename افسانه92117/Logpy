import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional
from ._format import LogParser
from ._utils import _save_log_in_file


__version__: str = "0.0.1"


class Logger:
    """Logger class

    all logging methods are implemented inn this class
    """

    def __init__(
        self,
        save_log: Optional[bool] = False,
        date_format: Optional[str] = "",
        log_path: Optional[str] = r"",
        name: Optional[str] = "",
        log_format: Optional[str] = "",
    ) -> None:
        """Logger class default values

        Args:
            save_log (Optional[bool], optional): [description]. Defaults to False.
            date_format (Optional[str], optional): [description]. Defaults to "".
            log_path (Optional[str], optional): [description]. Defaults to r"".
            name (Optional[str], optional): [description]. Defaults to "".
        """
        self.save_log = save_log

        if date_format == "":
            self.date_format = "%Y-%m-%d"
        else:
            self.date_format = date_format

        self.name = name
        self.log_filename: str = "logs.log"
        if log_path == "":
            self.log_path = "."

        self.log_path = os.path.join(log_path, self.log_filename)
        self.app_logger = LogParser(log_format)

    def __str__(self) -> str:
        """__str__ method for Logger class

        Returns:
            str: value to be printed on the screen
        """
        if (self.save_log is not False) and (self.log_path != ""):
            return f"Logger: {self.name}\nSave logs: True\nPath: {self.log_path}"

        return self.name

    def init(self) -> None:
        """init function
        create the needed log files
        """

        self._c_p = Path(self.log_path)
        self._c_p.touch(exist_ok=True)

    def critical(self, msg: str) -> None:
        """Critical log

        Args:
            msg (str): log message

        Raises:
            Exception: error for empty messages
            FileNotFoundError: error if log file does not exist or was not found
        """
        if msg == "":
            raise Exception("Empty message")

        self.ftime = datetime.today().strftime(self.date_format)
        self.level = "CRITICAL"
        self._fmsg = self.app_logger(self.level, msg, self.ftime)

        if self.save_log is not False:
            try:
                _save_log_in_file(self.log_path, self._fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")

            print(self._fmsg)
        else:
            print(self._fmsg)

    def warning(self, msg: str) -> None:
        """Warning log

        Args:
            msg (str): log message

        Raises:
            Exception: error for empty messages
            FileNotFoundError: error if log file does not exist or was not found
        """
        if msg == "":
            raise Exception("Empty message")

        self.ftime = datetime.today().strftime(self.date_format)
        self.level = "WARNING"
        self._fmsg = self.app_logger(self.level, msg, self.ftime)

        if self.save_log is not False:
            try:
                _save_log_in_file(self.log_path, self._fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")

            print(self._fmsg)
        else:
            print(self._fmsg)

    def info(self, msg: str) -> None:
        """Info log

        Args:
            msg (str): log message

        Raises:
            Exception: error for empty messages
            FileNotFoundError: error if log file does not exist or was not found
        """
        if msg == "":
            raise Exception("Empty message")

        self.ftime = datetime.today().strftime(self.date_format)
        self.level = "INFO"
        self._fmsg = self.app_logger(self.level, msg, self.ftime)

        if self.save_log is not False:
            try:
                _save_log_in_file(self.log_path, self._fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")

            print(self._fmsg)
        else:
            print(self._fmsg)

    def error(self, msg: str) -> None:
        """Error log

        Args:
            msg (str): log message

        Raises:
            Exception: error for empty messages
            FileNotFoundError: error if log file does not exist or was not found
        """
        if msg == "":
            raise Exception("Empty message")

        self.ftime = datetime.today().strftime(self.date_format)
        self.level = "ERROR"
        self._fmsg = self.app_logger(self.level, msg, self.ftime)

        if self.save_log is not False:
            try:
                _save_log_in_file(self.log_path, self._fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")

            print(self._fmsg)
        else:
            print(self._fmsg)

    def success(self, msg: str) -> None:
        """Success log

        Args:
            msg (str): log message

        Raises:
            Exception: error for empty messages
            FileNotFoundError: error if log file does not exist or was not found
        """
        if msg == "":
            raise Exception("Empty message")

        self.ftime = datetime.today().strftime(self.date_format)
        self.level = "SUCCESS"
        self._fmsg = self.app_logger(self.level, msg, self.ftime)

        if self.save_log is not False:
            try:
                _save_log_in_file(self.log_path, self._fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")

            print(self._fmsg)
        else:
            print(self._fmsg)

    @staticmethod
    def log(msg: str) -> None:
        """Default log function [DEPRECATED]

        Args:
            msg (str): log message

        Raises:
            Exception: error for empty messages
        """
        if msg == "":
            raise Exception("Empty message")

        ftime = datetime.today().strftime("Y%-%m-%d")
        _fmsg = f"[{ftime}] - {msg}"
        print(_fmsg)


class ResumeAddon(Logger):
    """Resume addon for logpy default Logger class

    resume the logs for you

    Args:
        Logger (Logger): inherits the Logger class
    """

    def __init__(self) -> None:
        super().__init__()

    def resume(self) -> Dict[str, int]:
        """resume function

        the main function to the ResumeAddon class

        Raises:
            FileNotFoundError: if the log file does not exist

        Returns:
            Dict[str, int]: logs resume
        """
        if os.path.exists(self.log_path):
            with open(self.log_path, "r", encoding="utf-8") as f:
                ctx = f.read()

            self.res_c = {
                "critical": ctx.count("[CRITICAL]"),
                "error": ctx.count("[ERROR]"),
                "warning": ctx.count("[WARNING]"),
                "info": ctx.count("[INFO]"),
                "success": ctx.count("[SUCCESS]"),
            }

            return self.res_c

        else:
            raise FileNotFoundError(
                "The log file does not exist, try running the init method of the Logger class"
            )


if __name__ == "__main__":
    pass
