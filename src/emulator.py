from alu_instructions import *
from flow import *
from memory import *
from memory_class import *
from branch import *
from ecalls import *
import sys

branches = ["blt", "ble", "beq", "bne", "bgt", "bge"]
alu = ["add","addi","mul","muli","div"]
storage = ["sw","lw"]
flow = ["jump","jalr","call"]
variable_byte_size = [1,2,4]



"""
  --------------- file itteration implementation below : -------------------------------------
"""

curr_cpu = CPU()


""" assembly file itteration
"""
path = 'data/asm_files/min.s'

with (open(path,'r')) as file:
     for line in file:
      
      line = line.strip()
      
      if line.startswith("#"):
        continue
      
      if "#" in line:
        line = line.split("#", 1)[0]
      
      line = line.replace(",", "")
      line = line.lower()
      line = line.strip()
      if line:
        curr_cpu.commands.append(line)

process_commands(curr_cpu)
print(curr_cpu.commands)








