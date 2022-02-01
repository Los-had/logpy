from datetime import datetime
from typing import Optional
import colorama
from colorama import Fore, Back, Style
import os

colorama.init(autoreset=True)
__version__ = "0.0.1"

# TODO: add formating feature for custom logs
class Logger:
    def __init__(self, save_log: Optional[bool] = False, date_format: Optional[str] = "", log_path: Optional[str] = r"", name: Optional[str] = "") -> None:
        self.save_log = save_log
        
        if date_format == "":
            self.date_format = "%Y-%m-%d"
        else:
            self.date_format = date_format

        self.log_path = log_path
        self.name = name
    
    def __str__(self) -> str:
        if (self.save_log is not False) and (self.log_path != ""):
            return f"Logger: {self.name}\nSave logs: True\nPath: {self.log_path}"
        
        return self.name
    
    def critical(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")

    def warning(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")

    def info(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")

    def error(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")

    def success(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")
