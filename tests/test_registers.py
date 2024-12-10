from unittest import TestCase
from src.flow import *
from src.memory_class import *


def test_get_reg():

    a = get_register("x0")
    b = get_register("x2")
    c = get_register("sp")
    d = get_register("10(sp)")
    e = get_register("(x4)")

    assert a == 0
    assert b == 2
    assert c == 2
    assert d == 2
    assert e == 4