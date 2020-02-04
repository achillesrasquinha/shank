# imports - module imports
from shank.cli.util   import *
from shank.cli.parser import get_args
from shank.util._dict import merge_dict
from shank.util.types import get_function_arguments

def command(fn):
    args    = get_args()
    
    params  = get_function_arguments(fn)

    params  = merge_dict(params, args)
    
    def wrapper(*args, **kwargs):
        return fn(**params)

    return wrapper