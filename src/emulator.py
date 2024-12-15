from alu_instructions import *
from flow import *
from memory import *
from memory_class import *
from branch import *
from ecalls import *
import sys
import struct

branches = ["blt", "ble", "beq", "bne", "bgt", "bge"]
alu = ["add","addi","mul","muli","div"]
storage = ["sw","lw","sh","sb","lb","lh"]
flow = ["jump","jalr","call","ret"]
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


""" itterating throug every line in asm commands
"""
for i in range (len(curr_cpu.commands)):
  lst = curr_cpu.commands[i]    
  if lst[0] in branches:
    pass

  elif lst[0] in alu:
    alu_control(curr_cpu,i)
  

  elif lst[0] in storage:
    pass
    #storage_control(curr_cpu,i)
    
  elif lst[0] in flow:
    pass

  elif lst[0] == "ecall":
    pass
