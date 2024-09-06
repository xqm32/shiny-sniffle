from a.b.c.d import SomeClass as SomeClassA
from b.c.d import SomeClass as SomeClassB


def SomeFunc():
    print(SomeClassA == SomeClassB)
