import struct

def is_within_4_bytes(value):
    if isinstance(value, int):
        if value.bit_length() <= 32:
            return True
        else:
            raise ValueError(f"Integer {value} exceeds 4-byte size (32 bits).")
    
    elif isinstance(value, float):
        packed = struct.pack('f', value) 
        unpacked = struct.unpack('f', packed)[0] 
        if unpacked == value:
            return True
        else:
            raise ValueError(f"Float {value} cannot be represented as a 4-byte float.")
    
    else:
        raise ValueError(f"Unsupported type: {type(value)}")

"""
temporary registers : x5-x7 and x28-x31
function value registers : x10-x17
"""
valid_register = list(range(33))

""" add method
in reg[register_0] we write reg[register_1] + reg[register_2]
"""
def add(register_1, register_2, register_0, curr_cpu):
    if (register_0 in valid_register):
        reg_val1 = int(curr_cpu.registers[register_1])
        reg_val2 = int(curr_cpu.registers[register_2])
        ans = reg_val1 + reg_val2
        is_within_4_bytes(ans)
        curr_cpu.registers[register_0] = ans
    else:
        raise ValueError("Use a valid register for your assembly code")

""" add method
in reg[register_0] we write reg[register_1] + literal_value
"""
def addi(register_1, register_0, literal_value, curr_cpu):
    if (register_1 in valid_register):
        reg_val = int(curr_cpu.registers[register_1])
        ans = reg_val + literal_value
        is_within_4_bytes(ans)
        curr_cpu.registers[register_0] = ans
    else:
        raise ValueError("Use a valid register for your assembly code")

""" mul method
in reg[register_0] we write reg[register_1] * reg[register_2]
"""
def mul(register_1, register_2, register_0, curr_cpu):
    if (register_0 in valid_register):
        reg_val1 = int(curr_cpu.registers[register_1])
        reg_val2 = int(curr_cpu.registers[register_2])
        ans = reg_val1 * reg_val2
        is_within_4_bytes(ans)
        curr_cpu.registers[register_0] = ans
    else:
        raise ValueError("Use a valid register for your assembly code")

""" muli method
in reg[register_0] we write reg[register_1] * literal_value
"""
def muli(register_0, register_1, literal_value, curr_cpu):
    if (register_0 in valid_register):
        reg_val = int(curr_cpu.registers[register_1])
        ans = reg_val * literal_value
        is_within_4_bytes(ans)
        curr_cpu.registers[register_0] = ans
    else:
        raise ValueError("Use a valid register for your assembly code")

""" div method
in reg[register_0] we write reg[register_1] / reg[register_2]
"""
def div(register_0, register_1, register_2, curr_cpu):
    if (register_0 in valid_register):
        reg_val1 = int(curr_cpu.registers[register_1])
        reg_val2 = int(curr_cpu.registers[register_2])
        if reg_val2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        ans = reg_val1 // reg_val2  # Use integer division
        is_within_4_bytes(ans)
        curr_cpu.registers[register_0] = ans
    else:
        raise ValueError("Use a valid register for your assembly code")
