from alu_instructions import *
from flow import *
from memory import *
from memory_class import *
from branch import *
from ecalls import *
import sys

branches = ["blt", "ble", "beq", "bne", "bgt", "bge"]
alu = ["add","addi","mul","muli","div"]
storage = ["sw","lw","sh","sb","lb","lh"]
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
labels(curr_cpu)
print(curr_cpu.label_ind)

for i in range (len(curr_cpu.commands)):
  lst = curr_cpu.commands[i]
  for parts in lst:
    
    if parts[0] in branches:
      pass
    
    elif parts[0] in alu:
      pass

    elif parts[0] in storage:
      pass

    elif parts[0] in flow:
      pass

    elif parts[0] == "ecall":
      pass
    