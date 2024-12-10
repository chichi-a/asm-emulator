"""method if_statements
takes the command from assembly code 
which is a branch and we reeturn true 
if this command is correct
"""
def if_statements(reg_a,reg_b,brnch,curr_cpu)->bool:
    a = curr_cpu.registers[reg_a]
    b = curr_cpu.registers[reg_b]
    
    if brnch == "blt":
        return a<b
    elif brnch == "ble":
        return a<=b
    elif brnch == "beq":
        return a==b
    elif brnch == "bne":
        return a!=b
    elif brnch == "bgt":
        return a>b
    elif brnch == "bge":
        return a>=b
    
    return 0