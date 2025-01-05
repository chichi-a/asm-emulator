
""" ecall functions
used to print values or exit program
"""
def ecall_func(curr_cpu):

    x11_val = curr_cpu.registers[11]
    x10_val = curr_cpu.registers[10]

    if (x10_val == 1):
        print(x11_val,end="")

    if (x10_val == 10):
        return True
    
    if x10_val == 11: 
        if x11_val == 32:  # ASCII for space
            print(" ", end="")
        else:
            print(chr(x11_val & 0xFF), end="")  


    return False