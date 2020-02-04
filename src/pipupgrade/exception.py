# imports - standard imports
import subprocess as sp

class ShankError(Exception):
    pass

class PopenError(ShankError, sp.CalledProcessError):
    pass