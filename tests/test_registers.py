from unittest import TestCase
from src.flow import *
from src.memory_class import *


def test_get_reg():

    a = get_register("x0")
    b = get_register("x2")
    c = get_register("sp")
    d = get_register("10(sp)")
    e = get_register("(x4)")
    r = get_register("ra")

    assert r == 1
    assert a == 0
    assert b == 2
    assert c == 2
    assert d == 2
    assert e == 4


def test_storage():

    a,b = get_storage("(x2)")
    assert a == 0
    assert b == 2

    c,d = get_storage("10(sp)")
    assert c == 10
    assert d == 2

