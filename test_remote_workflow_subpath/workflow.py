

from kfp import dsl
from mlrun.platforms import auto_mount
import os
import sys
import mlrun

funcs = {}


def kfpipeline(x):
    add_1 = mlrun.run_function('add-1',params={'x':x},outputs=['return'])
    
    add_2 = mlrun.run_function('add-2',params={'x':add_1.outputs['return']})
