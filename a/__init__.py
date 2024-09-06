import os
import sys

sys.path.append(os.path.dirname(__file__))

from a.b import SomeClass as SomeClassA
from b import SomeClass as SomeClassB


def SomeFunc():
    print(SomeClassA == SomeClassB)
