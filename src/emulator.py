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
flow = ["jump","jalr","call","j"]
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
i = 0
while ( i < len(curr_cpu.commands)):
    lst = curr_cpu.commands[i]  

    print(lst)
    if lst[0] in branches:
      if (len(lst) != 4):
        raise ValueError(" invalid branch")
      
      if lst[3] not in curr_cpu.label_ind:
        raise ValueError(" invalid label ")

      reg_a = get_register(lst[1])
      reg_b = get_register(lst[2])
      bool_check = if_statements(reg_a,reg_b,lst[0],curr_cpu)

      if (bool_check):
         i = labels[label] + 1  
         continue
      

    elif lst[0] in alu:
      alu_control(curr_cpu,i)
      
    elif lst[0] in storage:
      storage_control(curr_cpu,i)
      
    elif lst[0] in flow:
      command = lst[0]
      label = lst[1]
    
      i = flow_control(curr_cpu,i,command,label)
      continue

    elif lst[0] == "ecall":
      if ecall_func(curr_cpu):
        break

    elif lst[0] == "ret":
      i = curr_cpu.registers[1]
      continue 
    
    i+= 1  

