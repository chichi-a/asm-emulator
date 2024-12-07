
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

#addi sp sp +-bytes
def add_to_sp(curr_cpu,bytes):

    curr_offset = curr_cpu.curr_offset

    #remove space on stack and go up the stack
    if bytes > 0:
        if curr_offset < bytes:
            raise ValueError("not enough space")
                 
        start_pos = curr_offset - bytes
        end_pos = curr_offset
        for i in range (start_pos,end_pos+1):
            curr_cpu.memory_pointer[i] = None

        
        curr_cpu.curr_offset -= bytes

        return 

    # make space on stack to add new variables
    if bytes < 0:

        curr_cpu.curr_offset += bytes
       
        return 

       

def store_word(value,dest_location,curr_cpu):
    memory_pointer = curr_cpu.memory_pointer
    curr_offset = curr_cpu.curr_offset
    stack_size = curr_cpu.curr_stack_size 

    pass




