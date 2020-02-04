# imports - standard imports
import subprocess as sp

# imports - module imports
from shank.util.system import popen
from shank.exception   import (
    shankError,
    PopenError
)

# imports - test imports
import pytest

def test_shank_error():
    with pytest.raises(shankError):
        raise shankError

def test_popen_error():
    with pytest.raises(PopenError):
        popen("python -c 'raise TypeError'")

    assert isinstance(
        PopenError(0, "echo foobar"),
        (shankError, sp.CalledProcessError)
    )
    assert isinstance(shankError(), Exception)