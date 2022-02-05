import pytest
from typing import List
from logpy import __version__
import os


@pytest.mark.skip(reason="not implemented yet")
def test_critical(console):
    pass


@pytest.mark.skip(reason="not implemented yet")
def test_error(console):
    pass


@pytest.mark.skip(reason="not implemented yet")
def test_warning(console):
    pass


@pytest.mark.skip(reason="not implemented yet")
def test_info(console):
    pass


@pytest.mark.skip(reason="not implemented yet")
def test_success(console):
    pass


@pytest.mark.skip(reason="not implemented yet")
def test_log(console):
    pass


@pytest.mark.skip(
    reason="Always fail in the CI server, because all the tests run in an async way"
)
def test_resume_addon(console, resume_addon):
    console.critical("1")
    console.error("2")
    console.warning("3")
    console.info("4")
    console.success("5")
    r_val = resume_addon.resume()

    assert r_val == {"critical": 1, "error": 1, "warning": 1, "info": 1, "success": 1}


def test_log_save(console):
    console.info("hi")

    assert os.path.exists("./logs.log")


def test_line_breaks_in_log_file(console):
    def open_log_file() -> List[str]:
        try:
            f = open("./logs.log", "r")
            ctx = f.readlines()

            return ctx
        finally:
            f.close()

    console.critical("1")
    console.error("2")
    console.warning("3")
    console.info("4")
    console.success("5")

    try:
        line_count = open_log_file()
    except IOError:
        console.init()
        line_count = open_log_file()
    except FileNotFoundError:
        console.init()
        line_count = open_log_file()

    assert len(line_count) > 1
    assert os.path.exists("./logs.log")


def test_version():
    assert __version__ == "0.0.1"
