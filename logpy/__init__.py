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

        self.name = name
        self.log_filename: str = "logs.log"
        self.log_path = os.path.join(log_path, self.log_filename)
    
    def __str__(self) -> str:
        if (self.save_log is not False) and (self.log_path != ""):
            return f"Logger: {self.name}\nSave logs: True\nPath: {self.log_path}"
        
        return self.name
    
    def critical(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")
        
        self.ftime = datetime.today.strftime(self.date_format)
        self.fmsg = f"{Fore.RED}[CRITICAL]{Fore.RESET} {self.ftime} - {msg}"

        if self.save_log is not False:
            try:
                with open(self.log_path, "a", encoding="utf8") as f:
                    f.write(self.fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")
            
            print(self.fmsg)
        else:
            print(self.fmsg)

    def warning(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")
        
        self.ftime = datetime.today.strftime(self.date_format)
        self.fmsg = f"{Fore.YELLOW}[WARNING]{Fore.RESET} {self.ftime} - {msg}"

        if self.save_log is not False:
            try:
                with open(self.log_path, "a", encoding="utf8") as f:
                    f.write(self.fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")
            
            print(self.fmsg)
        else:
            print(self.fmsg)

    def info(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")

        self.ftime = datetime.today.strftime(self.date_format)
        self.fmsg = f"{Fore.CYAN}[INFO]{Fore.RESET} {self.ftime} - {msg}"

        if self.save_log is not False:
            try:
                with open(self.log_path, "a", encoding="utf8") as f:
                    f.write(self.fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")
            
            print(self.fmsg)
        else:
            print(self.fmsg)

    def error(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")
        
        self.ftime = datetime.today.strftime(self.date_format)
        self.fmsg = f"{Fore.MAGENTA}[ERROR]{Fore.RESET} {self.ftime} - {msg}"

        if self.save_log is not False:
            try:
                with open(self.log_path, "a", encoding="utf8") as f:
                    f.write(self.fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")
            
            print(self.fmsg)
        else:
            print(self.fmsg)

    def success(self, msg: str) -> None:
        if msg == "":
            raise Exception("Empty message")
        
        self.ftime = datetime.today.strftime(self.date_format)
        self.fmsg = f"{Fore.GREEN}[SUCCESS]{Fore.RESET} {self.ftime} - {msg}"

        if self.save_log is not False:
            try:
                with open(self.log_path, "a", encoding="utf8") as f:
                    f.write(self.fmsg)
            except FileNotFoundError:
                raise FileNotFoundError(f"{self.log_path} does not exist")
            
            print(self.fmsg)
        else:
            print(self.fmsg)
    
