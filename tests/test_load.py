from unittest import TestCase
from src.memory import *
from src.memory_class import *


def test_load_word():
    curr_cpu = CPU()
    dest_reg = 5
    val_reg = 0;
    curr_cpu.registers[val_reg] = 100

    result = 0x08090705
    curr_cpu.memory_blocks[110] = 5
    curr_cpu.memory_blocks[111] = 7
    curr_cpu.memory_blocks[112] = 9
    curr_cpu.memory_blocks[113] = 8

    load_word(val_reg,dest_reg,10,curr_cpu)
    assert curr_cpu.registers[5] == result


def test_load_half():
    curr_cpu = CPU()
    dest_reg = 5
    val_reg = 0;
    curr_cpu.registers[val_reg] = 100

    result = 0x08090705
    curr_cpu.memory_blocks[110] = 5
    curr_cpu.memory_blocks[111] = 7
    curr_cpu.memory_blocks[112] = 9
    curr_cpu.memory_blocks[113] = 8

    load_half(val_reg,dest_reg,10,curr_cpu)
    assert curr_cpu.registers[5] == 0x0705


def test_load_byte():
    curr_cpu = CPU()
    dest_reg = 5
    val_reg = 0;
    curr_cpu.registers[val_reg] = 100

    result = 0x0809
    curr_cpu.memory_blocks[108] = 9
    curr_cpu.memory_blocks[109] = 8

    load_byte(val_reg,dest_reg,8,curr_cpu)
    assert curr_cpu.registers[5] == 0x09
