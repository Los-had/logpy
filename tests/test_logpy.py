import pytest
from logpy import __version__, Logger
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

def test_log_save(console):
    console.info("hi")
    assert os.path.exists("./logs.log")

def test_version():
    assert __version__ == '0.0.1'
