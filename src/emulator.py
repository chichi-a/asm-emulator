from src.alu_instructions import *
from src.flow import *
from src.memory import *
from src.memory_class import *
from src.branch import *
from src.ecalls import *
import sys


"""
lists containing command names of risc-v assembly
"""
branches = ["blt", "ble", "beq", "bne", "bgt", "bge"]
alu = ["add","addi","mul","muli","div","li","rem"]
storage = ["sw","lw","sh","sb","lb","lh"]
flow = ["jump","call","j"]
variable_byte_size = [1,2,4]



"""
  --------------- file itteration implementation below : -------------------------------------
"""



""" assembly file itteration
"""

path = str(sys.argv[1])

def file_read(curr_cpu):
  ans = []
  with (open(path,'r')) as file:
      for line in file:
        line = line.strip()
        if line:
          ans.append(line)
  return ans



""" method to parse through assembly file lines
used to make assembly command lines from file more
readable for my emulator
"""
def list_read(curr_cpu, lst) :
    for line in lst:
        if not isinstance(line, str):
            continue
            
        # Remove leading/trailing whitespace
        line = line.strip()
        
        # Skip empty lines and full-line comments
        if not line or line.startswith("#"):
            continue
        
        if "#" in line:
            line = line.split("#", 1)[0]
        line = line.replace(",", " ").lower().strip()
        if line:
            curr_cpu.commands.append(line)


""" itterating throug every line in asm commands
each asm command line we call apprpriate method
"""
def command_iteration(curr_cpu):
  
  while ( curr_cpu.pc < len(curr_cpu.commands)):
      lst = curr_cpu.commands[curr_cpu.pc]  
      if lst[0] in branches:
        if (len(lst) != 4):
          raise ValueError(" invalid branch")
        
        if lst[3] not in curr_cpu.label_ind:
          raise ValueError(" invalid label ")

        reg_a = get_register(lst[1])
        reg_b = get_register(lst[2])
        bool_check = if_statements(reg_a,reg_b,lst[0],curr_cpu)

        if (bool_check):
          curr_cpu.pc = curr_cpu.label_ind[lst[3]] 
          continue
        

      elif lst[0] in alu:
        alu_control(curr_cpu,curr_cpu.pc)
        
      elif lst[0] in storage:
        storage_control(curr_cpu,curr_cpu.pc)
        
      elif lst[0] in flow:
        command = lst[0]
        label = lst[1]
      
        curr_cpu.pc = flow_control(curr_cpu,curr_cpu.pc,command,label)
        continue

      elif lst[0] == "ecall":
        if ecall_func(curr_cpu):
          break

      elif lst[0] == "ret":
        curr_cpu.pc = curr_cpu.registers[1]
        continue 
      
      curr_cpu.pc += 1  

def build_commands(lst,curr_cpu):
  list_read(curr_cpu,lst)
  
  process_commands(curr_cpu)

  labels(curr_cpu)
 


"""
build our emulator program
"""
def run():
  curr_cpu = CPU()
  lst = file_read(curr_cpu)
  build_commands(lst,curr_cpu)
  command_iteration(curr_cpu)