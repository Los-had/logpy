def _save_log_in_file(log_path: str, msg: str) -> None:
    """_save_log_in_file function
    save the generated logs in a log file

    Args:
        msg (str): msg to be saved

    Raises:
        FileNotFoundError: error if log file was not created
    """
    try:
        with open(log_path, "a", encoding="utf8") as f:
            f.write(msg)
    except FileNotFoundError:
        raise FileNotFoundError("File not found, try running the init function.")
