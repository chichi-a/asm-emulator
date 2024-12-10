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
        
def get_register(reg):

    if  reg.count('(') == 1 and reg.count(')') == 1:
        inner_reg = reg.split("(")[1].strip(")")
        return get_register(inner_reg) 

    if reg.startswith("x"):
        reg_num = int(reg[1:]) 
        if not isinstance(reg_num,int):
            raise ValueError(f"Invalid register number: {reg}")
        if 0 <= reg_num <= 33:
            return reg_num
        else:
            raise ValueError(f"Invalid register number: {reg}")

    if reg == "sp":
        return 2
    
    raise ValueError(f"Unrecognized register format: {reg}")


def storage_control(curr_cpu,index):
    
    curr_command = curr_cpu.commands[index][0]
    if (len(curr_cpu.commands[index]) != 3):
        raise ValueError("invalid command!")
    
    reg_1 = curr_cpu.commands[index][1]
    reg_2 = curr_cpu.commands[index][2]
    
    if curr_command == "sw":
        pass

    if curr_command == "sh":
        pass

    if curr_command == "sb":
        pass
    if curr_command == "lw":
        pass

    if curr_command == "lh":
        pass

    if curr_command == "lb":
        pass