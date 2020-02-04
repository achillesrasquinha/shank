# imports - compatibility imports
from shank._compat import HTTPError

# imports - test imports
import pytest

# imports - standard imports
from shank         import request as req
from shank._compat import string_types

def test_get():
    res  = req.get("https://httpbin.org/get")
    assert res.ok
    assert res.status_code == 200
    
    json = res.json() 
    assert all(k in json for k in ("url", "origin", "headers", "args"))

    res.raise_for_status()
    
    res  = req.get("http://httpbin.org/status/404")
    assert not res.ok
    assert res.status_code == 404

    with pytest.raises(HTTPError):
        res.raise_for_status()

    assert string_types(res) == "<Response [{code}]>".format(
        code = 404
    )

def test_post():
    res  = req.post("https://httpbin.org/post")
    assert res.ok
    assert res.status_code == 200
    
    json = res.json() 
    assert all(k in json for k in ("url", "origin", "headers", "args"))

    res.raise_for_status()
    
    res  = req.post("http://httpbin.org/status/404")
    assert not res.ok
    assert res.status_code == 404

    with pytest.raises(HTTPError):
        res.raise_for_status()

    assert string_types(res) == "<Response [{code}]>".format(
        code = 404
    )