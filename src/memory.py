
def first_n_bytes(value,n):
    shift = (4 - n) * 8
    shifted_value = value>>shift
    mask = (1 << ((4-n) * 8)) - 1
    extracted_bytes = shifted_value&mask
    return extracted_bytes

def last_n_bytes(value,n):
    mask = (1<< (n*8)) -1
    extracted_bytes = value&mask
    return extracted_bytes

def nth_byte(value,n):
    pass

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

    curr_cpu.memory_blocks[address]  = nth_byte(value,0)
    curr_cpu.memory_blocks[address]  = nth_byte(value,1)
    curr_cpu.memory_blocks[address]  = nth_byte(value,2)
    curr_cpu.memory_blocks[address]  = nth_byte(value,3)
    
    






