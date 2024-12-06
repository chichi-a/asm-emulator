


def add_to_sp(stack_pointer,curr_offset,bytes,stack_size):
    #remove space on stack and go up the stack
    if bytes > 0:
        if curr_offset < bytes:
            raise ValueError("not enough space")
            

        start_k = stack_size - bytes
        end_k = curr_offset
        max_of = 0

        for offset in list(stack_pointer.keys()):
            if offset in range(start_k,end_k+1):
                del stack_pointer[offset]
            else : max_of = max(max_of,offset)

    #    stack_size -= bytes
    #    curr_offset =  max_of
    #    now we can only accses stack_size - curr_offset bytes from 
    #    last offset

        bytes_in_lastOffs = stack_pointer[max_of][1]
        bytes_in_lastOffs = stack_size - bytes - max_of
        stack_pointer[max_of][1] = bytes_in_lastOffs

        return max_of

    # make space on stack to add new variables
    if bytes < 0:
        
        bytes_in_lastOffs = stack_pointer[curr_offset][1]
        if bytes_in_lastOffs > bytes:
            bytes_in_lastOffs -= bytes
            stack_pointer[curr_offset][1] = bytes_in_lastOffs
        
        # we get a new curr offset on stack
        return curr_offset + bytes

       
       


