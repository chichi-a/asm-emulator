#if n is 0 this returns the rightmost byte
def nth_byte(value, n,len):
    if n>= len :
        raise ValueError("not enough length")
    mask = 0xFF << (8 * n)
    return ((value & mask) >> (8 * n))


def conc_two_values(a,b):
    return (a<<8) | b
    


""" same as addi sp sp bytes
used to change stack pointer
"""
def add_to_sp(curr_cpu,bytes):

    curr_offset = curr_cpu.registers[2]

    #remove space on stack and go up the stack
    if bytes > 0:
        if curr_offset + bytes >= curr_cpu.total_size:
            raise ValueError("not enough space")
                 
        start_pos = curr_offset
        end_pos = curr_offset + bytes
        for i in range (start_pos,end_pos+1):
            curr_cpu.memory_blocks[i] = 0

        
        curr_cpu.registers[2] += bytes
        
        return 

    # make space on stack to add new variables
    if bytes < 0:
        if curr_offset - bytes <= 0:
            raise ValueError("not enough space")
        curr_cpu.registers[2] += bytes
        
        return 

""" store 4 byte value
stores 4 byte value into memory block ( stack )
"""
def store_word(val_register,src_register,add_mem,curr_cpu):
    address = curr_cpu.registers[src_register]
    address += add_mem

    if address + 3 >= curr_cpu.total_size | address < 0:
        raise ValueError("not enough space")

    value = curr_cpu.registers[val_register]

    #if i have value : 12345678
    #ill have to store : 78 56 34 12 
    for i in range (0,4):
        curr_cpu.memory_blocks[address+i] = nth_byte(value,i,4)

""" store 2 byte value
stores 2 byte value into memory block ( stack )
""" 
def store_half(val_register,src_register,add_mem,curr_cpu):
    address = curr_cpu.registers[src_register]
    address += add_mem

    if address + 1 >= curr_cpu.total_size | address < 0:
        raise ValueError("not enough space")

    value = curr_cpu.registers[val_register]

    for i in range (0,2):
        curr_cpu.memory_blocks[address+i] = nth_byte(value,i,4)

""" store 1 byte value
stores 1 byte value into memory block ( stack )
""" 
def store_byte(val_register,src_register,add_mem,curr_cpu):
    address = curr_cpu.registers[src_register]
    address += add_mem

    if address  < 0 | address >= curr_cpu.total_size:
        raise ValueError("not enough space")

    value = curr_cpu.registers[val_register]

    curr_cpu.memory_blocks[address]  = nth_byte(value,0,1)

""" load value from src into val register
used to load 4 byte value from address written in dest_register
into register val_register
"""
def load_word(val_register,dest_register,add_mem,curr_cpu):
    address = curr_cpu.registers[val_register]
    address += add_mem

    if address + 3 >= curr_cpu.total_size| address < 0:
        raise ValueError("not enough space")
    
    values = []
    for i in range(0,4):
        values.append(curr_cpu.memory_blocks[address+i])

    ans = conc_two_values(values[3],values[2])
    ans = conc_two_values(ans,values[1])
    ans = conc_two_values(ans,values[0])

    curr_cpu.registers[dest_register] = ans

""" load value from src into val register
used to load 2 byte value from address written in dest_register
into register val_register
"""
def load_half(val_register,dest_register,add_mem,curr_cpu):
    address = curr_cpu.registers[val_register]
    address += add_mem

    if address + 1 >= curr_cpu.total_size | address < 0:
        raise ValueError("not enough space")
    
    values = []
    for i in range(0,2):
        values.append(curr_cpu.memory_blocks[address+i])

    ans = conc_two_values(values[1],values[0])
    curr_cpu.registers[dest_register] = ans

""" load value from src into val register
used to load 1 byte value from address written in dest_register
into register val_register
"""
def load_byte(val_register,dest_register,add_mem,curr_cpu):
    address = curr_cpu.registers[val_register]
    address += add_mem

    if address  < 0 | address >= curr_cpu.total_size:
        raise ValueError("not enough space")
    
    value = curr_cpu.memory_blocks[address]
    curr_cpu.registers[dest_register] = value
