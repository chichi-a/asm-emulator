""" method process commands
parsing through the list of assembly lines we remove 
space characters and make a list containing list of commands
"""
def process_commands(curr_cpu):
    index = 0
    for line in curr_cpu.commands:
        parts = line.strip().split()
        if not parts:
            continue  # Skip empty lines
        
        curr_cpu.commands[index] = parts
        index += 1;
      
        
        