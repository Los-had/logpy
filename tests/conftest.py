import pytest
import logpy


@pytest.fixture
def console():
    c = logpy.Logger(save_log=True, log_path="./", name="test console")

    return c
