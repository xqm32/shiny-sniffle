import os
import sys
from a.b import SomeClass as SomeClassA

sys.path.append(os.path.dirname(__file__))

from b import SomeClass as SomeClassB


def SomeFunc():
    print(SomeClassA == SomeClassB)
