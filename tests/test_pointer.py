from unittest import TestCase
from src.memory import *
from src.memory_class import *

def test_sp_del():
    curr_cpu = CPU()
    curr_cpu.registers[5] = 0x01050907
    curr_cpu.registers[0] = 100
    store_word(5,0,0,curr_cpu) 
    
    assert curr_cpu.memory_blocks[100] == 7
    assert curr_cpu.memory_blocks[101] == 9


    # chaiwera 100,101,102,103 ze

    curr_cpu.curr_offset_pointer = 100
    bytes_to_del = 10

    add_to_sp(curr_cpu,bytes_to_del)

    assert curr_cpu.curr_offset_pointer == 110
    assert curr_cpu.memory_blocks[102] == 0
    assert curr_cpu.memory_blocks[101] == 0       
    assert curr_cpu.memory_blocks[100] == 0


def test_sp_add():
    curr_cpu = CPU()
    curr_cpu.curr_offset_pointer = 100
    bytes_to_add = -10
    add_to_sp(curr_cpu,bytes_to_add)
    assert curr_cpu.curr_offset_pointer == 90