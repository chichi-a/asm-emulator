import alu_instructions
import flow
import memory
import memory_class
import branch
import ecalls

branches = ["blt", "ble", "beq", "bne", "bgt", "bge"]
alu = ["add","addi","mul","muli","div"]
storage = ["sw","lw"]
flow = ["jump","jalr","call"]
variable_byte_size = [1,2,4]

""" method command

this methods takes line from asm file as an input 
and returns the specific command from that line
"""

def command(line)->str:
    pass


curr_cpu = memory_class.CPU()


""" assembly file itteration
"""
path = 'data/asm_files/min.s'
with (open(path,'r')) as file:
     for line in file:
        # Print each line
        print(line.strip())




