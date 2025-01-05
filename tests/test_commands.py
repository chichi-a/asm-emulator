from src.memory import *
from src.alu_instructions import *
from src.emulator import*



def test_alu_flow():
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

def test_branch():
    curr_cpu = CPU()
    lst = ["addi x10 x10 10","addi x11 x11 30", " bgt x10 x11 rame","ecall","rame : ","addi x11 x11 11"]
    build_commands(lst,curr_cpu)
    command_iteration(curr_cpu)


    index = curr_cpu.pc
    assert index == 3

    curr_cpu1 = CPU()
    lst = ["addi x10 x10 10","addi x11 x11 30", " ble x10 x11 rame","ecall","rame : ","addi x11 x11 11"]
    build_commands(lst,curr_cpu1)
    command_iteration(curr_cpu1)


    index = curr_cpu1.pc
    assert index == 6 #last ind is 5 but we make i bigger at the end of for




