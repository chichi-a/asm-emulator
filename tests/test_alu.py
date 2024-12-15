from unittest import TestCase
from src.memory_class import *
from src.alu_instructions import *


def test_bytes():

    num1 = (123.5)
    num2 = (10103013)

    assert is_within_4_bytes(num1) == True
    assert is_within_4_bytes(num2) == True


def test_alu_op():

    curr_cpu = CPU()

    curr_cpu.registers[10] = 4
    curr_cpu.registers[3] = 5

    add(10,3,10,curr_cpu)

    assert curr_cpu.registers[10] == 9

    addi(10,10,30,curr_cpu)

    assert curr_cpu.registers[10] == 39

    mul(3,10,10,curr_cpu)
    assert curr_cpu.registers[10] == 195

    div(10,10,3,curr_cpu)
    assert curr_cpu.registers[10] == 39