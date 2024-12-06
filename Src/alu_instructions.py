
"""
temporary registers : x5-x7 and x28-x31
function value registers : x10-x17
"""
valid_register = [5,6,7,10,11,12,13,14,15,16,17,28,29,30,31]

""" add method
in reg[register_1] we write reg[register_1] + reg[register_2]
"""
def add(register_1,register_2,stack_pointer):
    if (register_1 in valid_register) & (register_2 in valid_register):
        stack_pointer[register_1] += stack_pointer[register_2]
    else:
        raise ValueError("Use a valid register for your assembly code")
    
""" add method
in reg[register_1] we write reg[register_1] + literal_value
"""
def addi(register_1,literal_value):
    pass


def rame():
    print("yleoa")