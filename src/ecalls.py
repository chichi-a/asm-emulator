
""" ecall functions
used to print values or exit program
"""
def ecall_func(curr_cpu):

    x11_val = curr_cpu.registers[11]
    x10_val = curr_cpu.registers[10]

    if (x10_val == 1):
        print(x11_val)

    if (x10_val == 10):
        return True
    
    if (x10_val == 11):
        print(x11_val&0b11111111)


    return False