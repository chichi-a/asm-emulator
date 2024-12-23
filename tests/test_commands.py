from src.memory import *
from src.alu_instructions import *
from src.emulator import*



def test_r():
    curr_cpu = CPU()
    lst = ["addi x10 x10 300","addi x10 x10 -8", "muli x13 x10 1","addi x3 x3 2","div x14 x13 x3"]
    build_commands(lst,curr_cpu)
    com = curr_cpu.commands

    assert com[0][0] == "addi"
    assert com[0][3] == "300"

    command_iteration(curr_cpu)

    assert curr_cpu.registers[10] == 292
    assert curr_cpu.registers[13] == 292
    assert curr_cpu.registers[14] == (292/2)

    