from unittest import TestCase
from src.memory import *
from src.memory_class import *


def test_store_word():
    curr_cpu = CPU()
    curr_cpu.registers[5] = 0x01050907
    curr_cpu.registers[0] = 100
    store_word(5,0,3,curr_cpu) 
    assert 7 == curr_cpu.memory_blocks[103]
    assert 9 == curr_cpu.memory_blocks[104]
    assert 5 == curr_cpu.memory_blocks[105]
    assert 1 == curr_cpu.memory_blocks[106]

    curr_cpu.registers[4] = 0x010708
    store_word(4,0,0,curr_cpu)
    assert 8 == curr_cpu.memory_blocks[100]
    assert 7 == curr_cpu.memory_blocks[101]
    assert 1 == curr_cpu.memory_blocks[102]
    assert 0 == curr_cpu.memory_blocks[103]


def test_store_half():
    curr_cpu = CPU()
    curr_cpu.registers[5] = 0x010506
    curr_cpu.registers[0] = 100
    store_half(5,0,3,curr_cpu) 
    assert 6 == curr_cpu.memory_blocks[103]
    assert 5 == curr_cpu.memory_blocks[104]

def test_store_byte():
    curr_cpu = CPU()
    curr_cpu.registers[5] = 0x010506
    curr_cpu.registers[0] = 10000
    store_byte(5,0,0,curr_cpu) 
    assert 6 == curr_cpu.memory_blocks[10000]


