import alu_instructions


"""

this methods takes line from asm file as an input 
and returns the specific command from that line
"""

def command(line)->str:
    pass


"""

dict {  offset : value offset:value da a.sh  }
list x0,x1,x2....................x11
"""

stack_pointer = {}
registers = [0,"ra",stack_pointer,"gp","tp"]
registers.extend([None] * (32 - len(registers)))

for i in alu_instructions.valid_register:
    registers[i] = 0

print(registers)