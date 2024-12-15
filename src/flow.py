from src.memory import *
from src.alu_instructions import *

""" method process commands
parsing through the list of assembly lines we remove 
space characters and make a list containing list of commands
"""
def process_commands(curr_cpu):
    index = 0
    for line in curr_cpu.commands:
        parts = line.strip().split()
        if not parts:
            continue  # Skip empty lines
        
        curr_cpu.commands[index] = parts
        index += 1;

""" store label indexes
given our processed command lines we store each label
with their given index/adress in code
"""
def labels(curr_cpu):
    for i, line in enumerate(curr_cpu.commands):

        if line[0].endswith(":"):
            curr_cpu.label_ind.append((line[0][:-1],i))
        elif ":" in line:
            curr_cpu.label_ind.append((line[0],i))            

""" get register index from string reg
return index of a register we are currently working on
"""
def get_register(reg):

    # dereference case :
    if  reg.count('(') == 1 and reg.count(')') == 1:
        inner_reg = reg.split("(")[1].strip(")")
        return get_register(inner_reg) 

    # normal register case :
    if reg.startswith("x"):
        reg_num = int(reg[1:]) 
        if not isinstance(reg_num,int):
            raise ValueError(f"Invalid register number: {reg}")
        if 0 <= reg_num <= 33:
            return reg_num
        else:
            raise ValueError(f"Invalid register number: {reg}")
    
    # normal stack poitner case : 
    if reg == "sp":
        return 2
    
    raise ValueError(f"Unrecognized register format: {reg}")


""" get register index and an offset number 
return index and an offset number of a register we are currently working on
"""
def get_storage(reg):
    if "(" in reg and ")" in reg:
      
        offset_part = reg.split("(")[0]
        inner_reg = reg.split("(")[1].strip(")")

        if offset_part.strip() == "":  
            return 0, get_register(inner_reg)
        try:
            offset = int(offset_part)
            return offset,get_register(inner_reg)
        
        except ValueError:
            raise ValueError(f"Invalid offset format: {offset_part}")
    else:
        raise ValueError(f"Register format does not contain offset: {reg}")


def storage_control(curr_cpu,index):
    
    curr_command = curr_cpu.commands[index][0]
    if (len(curr_cpu.commands[index]) != 3):
        raise ValueError("invalid command!")
    
    reg_1 = curr_cpu.commands[index][1]
    reg_2 = curr_cpu.commands[index][2]

    reg_1_ind = get_register(reg_1)
    offset,reg_2_ind = get_storage(reg_2)
    
    if curr_command == "sw":
        store_word(reg_1_ind,reg_2_ind,offset,curr_cpu)

    if curr_command == "sh":
        store_half(reg_1_ind,reg_2_ind,offset,curr_cpu)

    if curr_command == "sb":
        store_byte(reg_1_ind,reg_2_ind,offset,curr_cpu)

    if curr_command == "lw":
        load_word(reg_2_ind,reg_1_ind,offset,curr_cpu)

    if curr_command == "lh":
        load_half(reg_2_ind,reg_1_ind,offset,curr_cpu)

    if curr_command == "lb":
        load_byte(reg_2_ind,reg_1_ind,offset,curr_cpu)


"""

"""
def alu_control(curr_cpu,index) :
    curr_command = curr_cpu.commands[index][0]
    if (len(curr_cpu.commands[index]) != 4):
        raise ValueError("invalid command!")
    
    reg_1 = curr_cpu.commands[index][1]
    reg_2 = curr_cpu.commands[index][2]

    reg_1_ind = get_register(reg_1)
    reg_2_ind = get_register(reg_2)

    last_num = curr_cpu.commands[index][3]

    if curr_command == "add":
        reg_3_ind = get_register(last_num)
        add(reg_2_ind,reg_3_ind,reg_1_ind,curr_cpu)
     
    if curr_command == "addi":
        try:
            num = int(last_num) 
            addi(reg_2_ind,reg_1_ind,num,curr_cpu)
        except ValueError:
            print(f"Error: '{last_num}' is not a valid number.")
        
    if curr_command == "mul":
        reg_3_ind = get_register(last_num)
        mul(reg_2_ind,reg_3_ind,reg_1_ind,curr_cpu)
        pass

    if curr_command == "muli":
        try:
            num = int(last_num) 
            print(num)
            muli(reg_1_ind,reg_2_ind,num,curr_cpu)
        except ValueError:
            print(f"Error: '{last_num}' is not a valid number.")

    if curr_command == "div":
        reg_3_ind = get_register(last_num)
        mul(reg_1_ind,reg_2_ind,reg_3_ind,curr_cpu)
        

