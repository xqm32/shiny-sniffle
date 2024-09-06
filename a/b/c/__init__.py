import os
import sys
from a.b.c.d import SomeClass as SomeClassA

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from c.d import SomeClass as SomeClassB


def SomeFunc():
    print(SomeClassA == SomeClassB)
