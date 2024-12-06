import alu_instructions
import flow_and_memory
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



""" in this dict key is an offset in stack 
and value is a lsit containing two elements
where first is value and second is how many byte long
is this specific offset
"""
stack_pointer = {}

# how much space we have occupied on stack 
curr_stack_size = 0
# what offset of stack are we currently on
curr_offset = 0;


""" in the registers list
we have 31 registers
"""
registers = [0,"ra",stack_pointer,"gp","tp"]
registers.extend([None] * (32 - len(registers)))

for i in alu_instructions.valid_register:
    registers[i] = 0




