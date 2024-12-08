#if n is 0 this returns the rightmost byte
def nth_byte(value, n,len):
    if n>= len :
        raise ValueError("not enough length")
    mask = 0xFF << (8 * n)
    return ((value & mask) >> (8 * n))


def conc_two_values(a,b):
    return (a<<8) | b
    

#addi sp sp +-bytes
def add_to_sp(curr_cpu,bytes):

    curr_offset = curr_cpu.curr_offset_pointer

    #remove space on stack and go up the stack
    if bytes > 0:
        if curr_offset < bytes:
            raise ValueError("not enough space")
                 
        start_pos = curr_offset - bytes
        end_pos = curr_offset
        for i in range (start_pos,end_pos+1):
            curr_cpu.memory_blocks[i] = 0

        
        curr_cpu.curr_offset_pointer -= bytes

        return 

    # make space on stack to add new variables
    if bytes < 0:

        curr_cpu.curr_offset_pointer -= bytes
       
        return 


def store_word(val_register,src_register,add_mem,curr_cpu):
    address = curr_cpu.registers[src_register]
    address += add_mem

    if address + 3 > curr_cpu.total_size:
        raise ValueError("not enough space")

    value = curr_cpu.registers[val_register]

    #if i have value : 12345678
    #ill have to store : 78 56 34 12 

    curr_cpu.memory_blocks[address] = nth_byte(value,0,4)
    curr_cpu.memory_blocks[address+1] = nth_byte(value,1,4)
    curr_cpu.memory_blocks[address+2] = nth_byte(value,2,4)
    curr_cpu.memory_blocks[address+3]  = nth_byte(value,3,4)
    
def store_half(val_register,src_register,add_mem,curr_cpu):
    address = curr_cpu.registers[src_register]
    address += add_mem

    if address + 1 > curr_cpu.total_size:
        raise ValueError("not enough space")

    value = curr_cpu.registers[val_register]

    curr_cpu.memory_blocks[address] = nth_byte(value,0,2)
    curr_cpu.memory_blocks[address+1] = nth_byte(value,1,2)


def store_byte(val_register,src_register,add_mem,curr_cpu):
    address = curr_cpu.registers[src_register]
    address += add_mem

    if address  > curr_cpu.total_size:
        raise ValueError("not enough space")

    value = curr_cpu.registers[val_register]

    curr_cpu.memory_blocks[address]  = nth_byte(value,0,1)






